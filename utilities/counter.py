def counter(words):
    dict_word = {}
    for word in words:
        dict_word[word] = dict_word.get(word, 0) + 1
        print("asdfads")
    return dict_word