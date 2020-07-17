def no_dups(x):
    words = x.split()

    words_seen = {}
    results = []

    for w in words:
        if w not in words_seen:
            results.append(w)
            words_seen[w] = True                


    return " ".join(list(dict.fromkeys(x.split())))



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))