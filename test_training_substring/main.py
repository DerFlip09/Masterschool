'''def first_substr(word, char):
    if type(char) is not str or type(word) is not str:
        return None
    elif len(char) > 1 or len(word) < 3:
        return None
    elif char in word:
        for index in range(len(word)):
            if word[index] == char and index + 2 <= len(word):
                return word[index: index + 3]
    return None
'''


def first_substr(word, char):
    if not isinstance(char, str) or not isinstance(word, str) or len(char) != 1 or len(word) < 3:
        return None

    index = word.find(char)
    if index != -1 and index + 3 <= len(word):
        return word[index: index + 3]

    return None
