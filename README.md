# Fortune Cookie Wisdom for Developers

[![make.fun](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/khususcrypto0000-coder/fortune-cookie-dev-makefun/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/khususcrypto0000-coder/fortune-cookie-dev-makefun/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

An entry for the [Fortune Cookie Wisdom for Developers](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44) bounty on [make.fun](https://make.fun).

This entry is a single original fortune-cookie line for a software developer, written for a tired senior engineer who has reviewed other people's code for twenty years and still reads every line. It takes something every developer has felt — running git blame on a strange line and bracing for a stranger's name — and turns it around: the name it shows is never a stranger at all, only an earlier version of the reader. The line lands in one breath, and on a second read it quietly asks who the reader will be when the next blame lands.

## How it works

`main.py` is a small standard-library-only Python program. It holds the entry as a string constant, checks it against the competition gate (one line, 1–120 characters, not only whitespace), and writes it to `entry.txt` inside the output directory — `/output` by default, or `$MAKEFUN_OUTPUT_DIR` when that is set.

```sh
python3 main.py
```

The program exits 0 on success and writes exactly one line of text with no
trailing newline inside the line itself. Running it twice produces
byte-identical output, so the result is fully deterministic.

## Files

- `main.py` — the entry program (Python 3, standard library only)
- `LICENSE` — MIT license
- `output/entry.txt` — the generated entry, produced by running `main.py`

