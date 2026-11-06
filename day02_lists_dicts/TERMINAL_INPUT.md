# Reading input from the terminal

There are three ways to get input into a Python script. Work through them in order, typing each demo yourself. It takes about 20 minutes.

---

## 1. `sys.argv`: arguments typed after the script name

This is what `word_freq.py` uses.

Create `argv_demo.py`:
```python
import sys

print(sys.argv)
print("how many:", len(sys.argv))
```

Run it a few different ways and look at what prints each time:
```bash
python argv_demo.py
# ['argv_demo.py']                    count = 1

python argv_demo.py alice.txt
# ['argv_demo.py', 'alice.txt']       count = 2

python argv_demo.py alice.txt 10
# ['argv_demo.py', 'alice.txt', '10'] count = 3
```

Three facts to remember:
1. `sys.argv[0]` is **always** the script name, so your first real argument is `sys.argv[1]`.
2. Every argument is a **string**, so `"10"` is not `10`. Convert it with `int(sys.argv[2])`.
3. Spaces separate arguments. A filename with a space in it needs quotes: `python x.py "my book.txt"`.

### Handling optional arguments and bad input
```python
import sys

if len(sys.argv) < 2:
    print("Usage: python argv_demo.py FILE [N]")
    sys.exit(1)          # a non-zero exit code means "failed"

path = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
print(f"file={path}  n={n}")
```
Try running it with no arguments, with `alice.txt`, with `alice.txt 3`, and with `alice.txt abc`. The last one crashes with a `ValueError`. **Exercise:** catch that error with `try`/`except ValueError` and print a friendly message instead.

---

## 2. `input()`: ask the user while the script is running

```python
name = input("What's your name? ")
age = int(input("Age? "))     # input() also returns a string, so convert it
print(f"Hi {name}, next year you'll be {age + 1}")
```
This is good for interactive tools, but bad for anything you want to automate. You can't loop it over 100 files, so `sys.argv` is the better choice for `word_freq.py`.

---

## 3. `argparse`: the professional version of `sys.argv`

Real ML training scripts look like `python train.py --epochs 20 --lr 0.001`. That's `argparse`:
```python
import argparse

parser = argparse.ArgumentParser(description="Count words in a file")
parser.add_argument("path", help="text file to read")
parser.add_argument("-n", "--top", type=int, default=10, help="how many words")
args = parser.parse_args()

print(args.path, args.top)    # args.top is already an int
```
```bash
python demo.py alice.txt --top 5
python demo.py --help          # you get a free help screen
```
It handles type conversion, defaults, errors and `--help` for you.

**Plan:** write `word_freq.py` with `sys.argv` first so you understand what's going on underneath. Then the stretch goal is to switch it to `argparse`.

---

## Bonus: reading from a pipe (`sys.stdin`)
```python
import sys
text = sys.stdin.read()
print(len(text.split()), "words")
```
```bash
cat alice.txt | python count.py    # Linux and macOS
type alice.txt | python count.py   # Windows
```
You'll see this in data-processing scripts. You don't need it for today.

---

## Check yourself
- [ ] What is `sys.argv[0]`?
- [ ] What type is `sys.argv[2]`, and why does that matter?
- [ ] When would you choose `input()` over `sys.argv`?
- [ ] What three things does `argparse` give you for free?
