import sys
import csv
import fuzzy
from Levenshtein import distance
from unidecode import unidecode

if len(sys.argv) < 2:
    print("usage: %s <max-edit-distance>" % sys.argv[0])
    sys.exit(1)
max_edit_distance = int(sys.argv[1])

dmeta = fuzzy.DMetaphone()


def dm(word):
    return dmeta(word)[0].decode()


def distances(word1, word2):
    w1, w2 = unidecode(word1), unidecode(word2)
# soundex is broken per https://github.com/yougov/fuzzy/issues/14
#    d1 = 0
#    s1, s2 = None, None
#    try:
#        s1 = soundex(word1)
#        s2 = soundex(word2)
#        d1 = distance(s1, s2)
#    except UnicodeDecodeError as e:
#        print(e, repr(word1.encode()), repr(word2.encode()))
    d2 = distance(dm(w1), dm(w2))
    d3 = distance(fuzzy.nysiis(w1), fuzzy.nysiis(w2))
    return [d2, d3]


pairs = []
with open('pairs.csv') as f:
    for pair in csv.reader(f):
        pair.extend(distances(pair[2], pair[3]))
        pairs.append(pair)

pairs = sorted(pairs, key=lambda x: x[4] + x[5] / 2.0)

for p in pairs:
    if p[4] + p[5] > max_edit_distance:
        break
    print(p)
