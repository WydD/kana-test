import romkan
import random
import gzip
import readline

words = list(gzip.open("hira.list.gz", mode="rt"))

while True:
    i = random.randint(0, len(words))
    to_write = words[i]
    roma = romkan.to_roma(to_write).strip()
    tries = 0
    while tries < 3:
        answer = input(to_write)
        if answer.strip() == roma:
            print("\tcorrect!")
            break
        else:
            print("\tWRONG!")
            if tries == 2:
                print("\tAnswer was "+roma)
            tries += 1
