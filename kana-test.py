import romkan
import random
import gzip
import readline
import sys

words = list(gzip.open("hira.list.gz", mode="rt", encoding="utf-8"))

if len(sys.argv) != 3:
    print("Usage: python kana-test.py {hira|kata} max_tries")
    exit(1)

mode = None
if sys.argv[1] == "hira":
    mode = 1
elif sys.argv[1] == "kata":
    mode = 2
if mode is None:
    print("Usage: python kana-test.py {hira|kata} max_tries")
    exit(1)
max_tries = int(sys.argv[2])

while True:
    i = random.randint(0, len(words))
    to_write = words[i]
    roma = romkan.to_roma(to_write).strip()
    if mode == 2:
        to_write = romkan.to_katakana(roma)+"\n"
    tries = 0
    while tries < max_tries:
        answer = input(to_write)
        if answer.strip() == roma:
            print("\tcorrect!")
            break
        else:
            print("\tWRONG!")
            tries += 1
            if tries == max_tries:
                print("\tAnswer was "+roma)