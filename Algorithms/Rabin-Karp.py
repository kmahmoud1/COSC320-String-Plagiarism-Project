# Rabin Karp Algorithm, as seen in CLRS book
# d is the number of characters in the input alphabet
d = 256


from time import time
import sys


def search(pat, text, q):
    m = len(pat)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    for i in range(m - 1):
        h = (h * d) % q

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(text[i])) % q

    # Find the match
    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pat[j]:
                    break

            j += 1
            if j == m:
                print("Pattern is found at position: " + str(i + 1))

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q

            if t < 0:
                t = t + q

    # Driver Code


if __name__ == "__main__":
    src = open("Dataset/plagiarism_source_2.txt", encoding="utf-8")
    sus = open("Dataset/plagiarism_sus_2.txt", encoding="utf-8")

    txt = src.read().lower()
    pat = sus.read().lower()

    txt = " ".join(txt.split("\n"))
    pat = " ".join(pat.split("\n"))

    # A prime number used for hashing
    q = 101

    # Function Call
    t0 = time()
    search(pat, txt, q)
    t1 = time()

    print(f"Ran Rabin-Karp in {t1-t0} seconds")
