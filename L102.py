#Authors are ALiza Litvak & Mac Weber-hess
def classnames(mydict):
    d = dict()
    for lastname in mydict:
        if mydict[lastname] not in d:
            d[mydict[lastname]] = 1
        else:
            d[mydict[lastname]] += 1
    return d

def frequency(mydict):
    def classmates(mydict):
        d = dict()
        for lastname in mydict:
            if mydict[lastname] not in d:
                d[mydict[lastname]] = 1
            else:
                d[mydict[lastname]] += 1
        return d
    mydict = classmates(mydict)

    def inverse_dict(d):
        inverse = dict()
        for key in d:
            val = d[key]
            if val not in inverse:
                inverse[val] = [key]
            else:
                inverse[val].append(key)
        return inverse
    result = inverse_dict(mydict)
    print(result)
