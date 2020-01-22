def straight(ranks):
    if len(set(ranks))==5 and (max(ranks)-min(ranks)==4):
        return True
    return False

def flush(suits):
    if len(set(suits)==1):
        return True
    return False

def kind(n,ranks):
    for r in ranks:
        if ranks.count(r)==n :
            return r
        return None

def two_pair(ranks):
    hicard=kind(2,ranks)
    locard=kind(2,reversed(ranks))

    if hicard!= locard:
        return (hicard,locard)
    return None

if __name__ == "__main__" :
    assert(straight([6,5,4,3,2])== True)
    assert(straight([6,5,5,3,2])== False)



