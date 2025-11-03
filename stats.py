def get_num_words(book_text):
    words = book_text.split()
    return len(words)


def get_char_count_lower(book_text):
    charlist = list(book_text)
    chardict = {}
    for c in charlist:
        if c.lower() not in chardict:
            chardict[c.lower()] = 1
        else:
            chardict[c.lower()] += 1
    return chardict


def get_char_count(book_text):
    charlist = list(book_text)
    chardict = {}
    for c in charlist:
        if c not in chardict:
            chardict[c] = 1
        else:
            chardict[c] += 1
    return chardict


def sort_on(items):
    return items["num"]


def sort_dict(charlist):
    sorted_dict = []
    for letter in charlist:
        if letter.isalpha():
            dataIn = {
                "char": letter,
                "num": charlist[letter]
            }
            # print(dataIn)
            sorted_dict.append(dataIn)
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict
