import re
import romkan

entries = set()
for i, entry in enumerate(open("edict2", encoding="euc-jp")):
    if i == 0:
        continue
    m = re.search("^[^/]*\\[([ぁ-んァ-ン]*)\\]", entry)
    if not m:
        continue
    entries.add(romkan.to_hiragana(romkan.to_roma(m.groups(1)[0])))

w = open("./hira.list", "w")
for e in entries:
    w.write(e+"\n")
w.close()
