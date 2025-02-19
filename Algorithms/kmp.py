import nltk.data
import os
import pathlib
import glob

# *Method Definitions


def KMP(pat: str, text: str, indexes: list):
    # *KMP search implementation
    N = len(text)
    M = len(pat)
    lps = [0] * M  # longest prefix that is also a suffix
    computeLPS(lps, pat, M)

    i = 0
    j = 0
    while (N - i) >= (M - j):  # stop when pattern does not fit in the text
        if text[i] == pat[j]:  # if pattern match at index, increment to check next one
            i += 1
            j += 1

        if j == M:  # if j reaches end of pattern, pattern has been found
            indexes.append(i-j)
            j = lps[j-1]

        elif i < N and pat[j] != text[i]:  # mismatch
            if j != 0:
                # rollback using lps if not on first letter of pattern
                j = lps[j-1]
            else:
                i += 1  # else, go on to the next one without updating j


def computeLPS(lps: list, pat: str, M: int):
    # *longest proper prefix preprocessing

    len_lps = 0  # length of the longest prefix suffix value
    lps[0] = 0
    i = 1

    while i < M:
        if pat[i] == pat[len_lps]:
            len_lps += 1
            lps[i] = len_lps
            i += 1
        elif len_lps != 0:
            len_lps = lps[len_lps-1]
        else:
            lps[i] = 0
            i += 1

# *main


def runKMP(src_file_path, sus_file_path):
    """
    Run KMP on a suspected plagiarised text against a source text.

   :param str src_file: The source file from which text was plagiarised
   :param str sus_file: The file suspected of plagiarism
   """
    src_file = open(src_file_path, encoding="utf-8")
    sus_file = open(sus_file_path, encoding="utf-8")

    src_contents = src_file.read().lower()
    sus_contents = sus_file.read().lower()

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    sentences = tokenizer.tokenize(src_contents)
    src_sentences = []
    for sentence in sentences:
        src_sentences.append(sentence)

    indexes = []

    for src_sentence in src_sentences:
        KMP(src_sentence, sus_contents, indexes)

    for index in indexes:
        print(f"Found plagiarism at index {index}")

# *Sources
# The following online resources were used in researching the KMP algorithm for this implementation

# Bari, A. (2018, March 25). 9.1 Knuth-Morris-Pratt KMP string matching algorithm. YouTube. Retrieved March 22, 2023, from https://www.youtube.com/watch?v=V5-7GzOfADQ

# GeeksforGeeks. (2022, December 1). KMP algorithm for pattern searching. GeeksforGeeks. Retrieved March 22, 2023, from https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

# Hule, V. (2022, January 19). Python list files in directory with extension TXT. PYnative. Retrieved March 22, 2023, from https://pynative.com/python-list-files-in-directory-with-extension-txt/

# Wikimedia Foundation. (2023, January 19). Knuth–Morris–Pratt algorithm. Wikipedia. Retrieved March 22, 2023, from https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
