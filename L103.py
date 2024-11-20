#Authors are Aliza Litvak & Mac Weber-Hess
cpsc_names = ["aliza", "litvak", "mac", "weber-hess", "olivia", "beck", "rylee", "taylor", "colleen", "hand", "serenity", "schuler"]
def frequency(mylist):
    d = dict()
    for name in mylist[1::2]:
        if name[0] not in d:
            d[name[0]] = 1
        else:
            d[name[0]] += 1
    return d

