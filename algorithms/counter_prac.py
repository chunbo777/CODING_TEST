from collections import Counter

def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter]+=1
    return counter
countLetters("helloworld!")

Counter("helloworld!")

def find_max(word):
    counter = Counter(word)
    max_count=-1
    if counter[letter]>max_count:
        max_count =count[letter]
        max_letter = letter
    return max_letter, max_count

find_max("helloworld!")
Counter('hello world').most_common() 