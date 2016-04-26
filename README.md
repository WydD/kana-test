# kana-test
Command line utility to test your kana reading capability. Program choses a random word from a japanese dictionary and
you have to translate its hira or kata form in romanji (hepburn).

To run this you must have python3.

```pip install romkan```

Then, you can just.
```python kana-test.py hira 3```
To launch a test for hiragana reading with 3 tries allowed.

## If you want to generate *.list.gz
Download edict2 from http://www.edrdg.org/jmdict/edict.html uncompress it then run gen-hira.py

## Sample
Hira
```
~> python kana-test.py hira 2
まちぜんたい
> machizentai
	correct!
したぞり
> shitazori
	correct!
ろんりしふと
> ronrishifuto
	correct!
じんみんせんせん
> jinhinsensen
	WRONG!
じんみんせんせん
> jinhensensen
	WRONG!
	Answer was jin mi nsensen
	You wrote: jin[he]nsensen
```

Kata
```
~> python kana-test.py kata 1
キキツタエル
> kikitsutaeru
	correct!
シメシアワス
> shinoshiawasu
	WRONG!
	Answer was shi me shiawasu
	You wrote: shi[no]shiawasu
```