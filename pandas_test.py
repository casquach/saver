import pandas as pd
import math
import operator
import random
import collections

#reviews = pd.read_csv("spending.csv")
reviews = pd.read_csv("restaurant.csv")
# info takes data set and column name
# weighted average entropy
# patrons should be picked
# p is probability distribution


def entropy(p):
    logs = []
    prob_dist = p
    for prob in prob_dist:
        if prob == 0:
            logs.append(0)
        else:
            logs.append(prob * math.log(prob, 2))
    return (-1)*sum(logs)

# a = dictionary of info, tuple of Y/N
# a = {None: (0, 2), Some: (4, 0), Full: (2/4)}


def info(a):
    infoes = []
    attributes = a
    print(attributes)
    vals = list(attributes.values())
    numer = [sum(tup) for tup in vals]
    denom = sum(map(sum, zip(*vals)))
    for att in vals:
        p = [att[0]/float(sum(att)), att[1]/float(sum(att))]
        n = numer[vals.index(att)]
        d = float(denom)
        a = n/d
        e = entropy(p)
        infoes.append(a*e)
    return sum(infoes)

def info_list():
    info_gain = {}
    will_wait = reviews.iloc[:,reviews.shape[1]-1]
    d = {}
    x = 0
    atts = reviews.iloc[:,0:reviews.shape[1]-1]
    for l in atts:
        for i in atts[l]:
            if i in d.keys():
                if will_wait[x] == "Yes":
                    d[i][0]+=1
                if will_wait[x] == "No":
                    d[i][1]+=1
            else:
                d[i] = [0,0]
                if will_wait[x] == "Yes":
                    d[i][0]+=1
                if will_wait[x] == "No":
                    d[i][1]+=1
            x+=1
        info_gain[l] = info(d)
        d = {}
        x = 0
    info_gain = dict(sorted(info_gain.items(), key=operator.itemgetter(1)))
    return info_gain

def probs(a):
    probs = {}
    attributes = a
    vals = list(attributes.values())
    for att in vals:
        p = [att[0]/float(sum(att)), att[1]/float(sum(att))]
        probs[att] = p
    return probs

info_gain = info_list()
print(info_gain)
