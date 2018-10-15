def word_count_engine(document):
    pass  # your code goes here
    """
    All unique words
    Decending order of occurances, Order in original sentence
    Case insensitive
    """

    # Edge Case
    if not document:
        return []

    document = document.lower()

    mem = {}
    occurance = 0
    word = ""
    for char in document:
        if ord("a") <= ord(char) <= ord("z"):
            word += char
        else:
            if word != "":
                if word in mem:
                    mem[word][0] += 1
                else:
                    mem[word] = [1, occurance]
                    occurance += 1
                word = ""
    if word:
        if word in mem:
            mem[word][0] += 1
        else:
            mem[word] = [1,occurance]

    mem2 = {}
    for word, items in mem.items():
        if items[0] in mem2:
            mem2[items[0]].append([word,items[1]])
        else:
            mem2[items[0]] = [[word,items[1]]]

    for count,item in mem2.items():
        mem2[count] = [record[0] for record in sorted(mem2[count],key = lambda element:element[1],reverse=True)]

    res = []
    for key in sorted(mem2.keys(),reverse=True):
        for rec in mem2[key]:
            res.append([rec,key])
    return res

    # mem2 = {}
    # for word,
    # word_freq = [(word, freq[0], freq[1]) for word, freq in mem.items()]
    # result = sorted(word_freq, key=lambda item: (item[1], item[2]), reverse=True)
    # result = [item[0],item[1] for item in result]
    # return result


document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
print(word_count_engine(document))

