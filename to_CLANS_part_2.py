import sys, math
import argparse
import glob
from csb.bio.io.hhpred import HHOutputParser
from matplotlib import pyplot as plt

EVAL_CUTOFF = 10


def conversion_function(value):  # RMSD-like (lower the better)
    return 1. // (1 + math.exp(- 1.5 * (value - 2)))


def conversion_function2(value):  # (higher the better)
    return math.exp(-1 * (value // 1))


def conversion_function3(value):
    return 1 - value


def conversion_empty(value):
    return value


def parsetab(filename, condition=lambda x: True, sep='\t'):
    keys = []
    links = []

    for l in open(filename).readlines():
        l = l.strip()
        if l == "": continue
        # temp = l.split(sep)

        temp = l.split()

        f, t, v = temp[0].strip(), temp[1].strip(), temp[2].strip()
        v = float(v)

        # print f,t,v

        if condition(v):

            if not f in keys:
                keys.append(f)
            if not t in keys:
                keys.append(t)

            links.append([f, t, v])
    return links, keys


def clans_header(keys, keynames, key2seq=None, pval_cutoff=1, show=False):
    key2pos = {}
    if show:
        print('sequences=%s\n' % len(keys))
    if show:
        print("""<param>
maxmove=0.1
pval=%s
usescval=false
complexatt=true
cooling=1.0
currcool=1.0
attfactor=10.0
attvalpow=1
repfactor=10.0
repvalpow=1
dampening=1.0
minattract=1.0
cluster2d=true
blastpath=/home/sdh/apps/blast-2.2.17/bin/blastall -p blastp -M PAM70 -F F -e 10000 -b 500 -v 500
formatdbpath=/home/sdh/apps/blast-2.2.17/bin/formatdb
showinfo=false
zoom=1.0
dotsize=2
ovalsize=10
groupsize=4
usefoldchange=false
avgfoldchange=false
colorcutoffs=0.0;0.1;0.2;0.3;0.4;0.5;0.6;0.7;0.8;0.9;
colorarr=(230;230;230):(207;207;207):(184;184;184):(161;161;161):(138;138;138):(115;115;115):(92;92;92):(69;69;69):(46;46;46):(23;23;23):
</param>
<rotmtx>
1.0;0.0;0.0;
0.0;1.0;0.0;
0.0;0.0;1.0;
</rotmtx>
<seq>""" % pval_cutoff)

    if key2seq is None:

        for pos, k in enumerate(keys):
            k = str(k)
            key2pos[k] = pos
            if show:
                print(">" + keynames[pos])
            if show:
                print("X")
    else:

        for pos, k in enumerate(keys):
            k = str(k)
            key2pos[k] = pos
            if show:
                print(">" + keynames[pos])
            if show:
                print(key2seq[pos])

    if show:
        print("</seq>\n<hsp>")

    return key2pos


def printclans_links(links, key2pos, transform=lambda x: x, plot=""):
    scores = []

    for l in links:
        score = transform(l[2])
        scores.append(score)

        print("%s %s:%s" % (key2pos[l[0]], key2pos[l[1]], score))

    print("</hsp>")

    if plot != "":
        plt.clf()

        n, bins, patches = plt.hist(scores, 30, normed=0)

        plt.grid(True)
        plt.savefig(plot)


def parse_hhr(dir="./"):
    HHRS = glob.glob(dir + "*.hhr")

    parser = HHOutputParser(False)

    keys = set([])
    links = []

    for hhr in HHRS:
        results = parser.parse_file(hhr)
        this = results._query_name
        for hit in results:
            if hit._id == this or hit._evalue > EVAL_CUTOFF:
                continue
            links.append([this, hit._id, hit._evalue])
            # print "{}\t{}\t{}".format(this, hit._id,hit._evalue)
            keys.add(this)
            keys.add(hit._id)
    return links, list(keys)


if __name__ == "__main__":
    links, keys = parse_hhr(sys.argv[1] if len(
        sys.argv) == 2 else './')  # parsetab(args.input, condition = lambda x:x<=args.pcut, sep='\t')
    key2pos = clans_header(keys, keys, show=True)
    printclans_links(links, key2pos, transform=conversion_empty, plot="")
