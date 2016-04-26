import romkan
import random
import gzip
import readline
import sys

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

words = list(gzip.open("hira.list.gz", mode="rt", encoding="utf-8"))


def find_error(answer, roma):
    current = None
    result = answer+"*"
    correct = roma
    for i in range(0, min(len(answer), len(roma))):
        if answer[i] == roma[i]:
            continue
        if current is None:
            current = [i, i]
            result = answer[:i]
            correct = roma[:i]
        elif i - 1 == current[1]:
            current[1] = i
        else:
            result += "[" + answer[current[0]:(current[1] + 1)] + "]" + answer[(current[1] + 1):i]
            correct += " " + roma[current[0]:(current[1] + 1)] + " " + roma[(current[1] + 1):i]
            current = [i, i]
    if current is not None:
        result += "["+answer[current[0]:(current[1]+1)]+"]"+answer[(current[1]+1):]
        correct += " "+roma[current[0]:(current[1]+1)]+" " + roma[(current[1]+1):]
    return result, correct

while True:
    i = random.randint(0, len(words))
    to_write = words[i]
    roma = romkan.to_roma(to_write).strip()
    if mode == 2:
        to_write = romkan.to_katakana(roma)+"\n"
    tries = 0
    while tries < max_tries:
        answer = input(to_write+"> ").strip()
        if answer == roma:
            print("\tcorrect!")
            break
        else:
            print("\tWRONG!")
            tries += 1
            if tries == max_tries:
                errors, correct = find_error(answer, roma)
                print("\tAnswer was "+correct+"\n\tYou wrote: "+errors)
