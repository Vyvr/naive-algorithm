# ----Finds if pattern matches text, starting from index----#
def matchesAt(text, index, pattern):
    if len(text) < len(pattern):
        return False
    for i in range(0, len(pattern)):
        if text[index + i] != pattern[i]:
            return False
    return True

# ----Adds to array indexes where pattern matches text----#
def report(index, matchedIndexes):
    matchedIndexes.append(index)


def main():
    text = 'acbabadababbdbabac'
    pattern = 'babac'
    # text = 'ABABBCAACCAWACACAWCCA'
    # pattern = 'BCAACCA'
    # text = 'abbababbabababb'
    # pattern = 'abb'
    matchedIndexes = []
    for i in range(0, (len(text) - len(pattern)) + 1):
        if matchesAt(text, i, pattern):
            report(i, matchedIndexes)

    print(matchedIndexes)


if __name__ == "__main__":
    main()
