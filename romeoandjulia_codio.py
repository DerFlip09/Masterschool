from romeo_and_juliet import PLAY


def get_words(text):
    lowercase_text = text.lower()
    list_of_lowercase_words = lowercase_text.split()
    return list_of_lowercase_words


def get_rid_of_punctuation(text):
    text_without_punctuation = ""
    for char in text:
        if char not in ".,!?-_&@%/":
            text_without_punctuation += char
    return text_without_punctuation


def word_frequency(list_of_words):
    words_with_appearances = {}
    for word in list_of_words:
        if word not in words_with_appearances:
            words_with_appearances[word] = 0
        words_with_appearances[word] += 1
    return words_with_appearances


# Sort key
def value_getter(item):
    return item[1]


def top_n_words(freq, n):
    sorted_list_of_appearances = sorted(freq.items(), key=value_getter, reverse=True)  # sorts
    for i in range(n):
        word, appearance = sorted_list_of_appearances[i]
        print(f"{word}: {appearance}")


def main():
    text_without_special_char = get_rid_of_punctuation(PLAY)
    list_of_words = get_words(text_without_special_char)
    dict_of_words = word_frequency(list_of_words)
    top_n_words(dict_of_words, 50)


if __name__ == "__main__":
    main()

################################### MASTERSCHOOL SOLUTION ##########################################
# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-03-22 19:29:35
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-03-31 22:01:31

"""
Romeo and Juliet

Find the most common words in the play Romeo and Juliet.
"""
'''import string

from romeo_and_juliet import PLAY

TOP_N = 52


def get_words(text):
    """
    Returns list of all the words in given text

    Words are case-sensitive
    """
    # create translation table to remove punctuation
    translation_table = str.maketrans("", "", string.punctuation)
    # remove punctuation in text based on translation table created
    cleaned_text = text.translate(translation_table)
    # return a list of words by splitting cleaned text by space characters
    # (" ", "\t", "\n", "\r", "\v", "\f")
    return cleaned_text.split()


def get_frequencies(words):
    """
    Returns dict with the frequency of each word in given list of words
    """
    # get unique words in lowercase
    words_in_lowercase = set()
    for word in words:
        words_in_lowercase.add(word.lower())

    # get frequencies
    frequencies = {}
    for word_in_lowercase in words_in_lowercase:
        frequencies[word_in_lowercase] = sum(
            1 for word in words if word.lower() == word_in_lowercase
        )
    return frequencies


def print_top_n_words(frequencies, n):
    """
    Prints the top n words from given dict of word and its frequency
    """
    # sort words in given dict by frequecy in the order of descending frequency
    sorted_words = sorted(frequencies, key=lambda word: (frequencies[word], word),
                          reverse=True)

    # print top n words
    print(f"Top {n} most frequent words:")
    for word in sorted_words[:n]:
        print(f"{word}: {frequencies[word]}")


def main():
    """
    Main function
    """
    words = get_words(PLAY)
    frequencies = get_frequencies(words)
    print_top_n_words(frequencies, TOP_N)


if __name__ == "__main__":
    main()
'''