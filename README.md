# Python Fundamentals — Practice Assignment

A structured collection of 30 Python exercises covering numbers, strings, loops, and pattern printing. Each exercise is implemented as a standalone script with a clearly defined function, following explicit constraints (e.g. no `max()`, no `dictionaries`, no `split()`) to reinforce core logic-building over reliance on built-in shortcuts.

---

## Table of Contents

- [Function Index](#function-index)
- [Topics Covered](#topics-covered)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Design Notes & Restrictions](#design-notes--restrictions)
- [Requirements](#requirements)
- [License](#license)

---

## Function Index

### Section A — Numbers & Functions

| # | File | Function(s) | Description |
|---|------|-------------|-------------|
| 01 | `01_check_even_odd.py` | `check_even_odd(n)` | Determines whether a number is even or odd |
| 02 | `02_check_number.py` | `check_number(n)` | Classifies a number as positive, negative, or zero |
| 03 | `03_find_largest_two.py` | `find_largest(S, T)` | Returns the larger of two numbers |
| 04 | `04_find_largest_three.py` | `find_Boro_number(a, b, c)` | Returns the largest of three numbers *(no `max()`)* |
| 05 | `05_sum_natural.py` | `sum_natural(n)` | Sums natural numbers from 1 to n using a `for` loop |
| 06 | `06_multiplication_table.py` | `multiplication_table(n)` | Prints the multiplication table of n |
| 07 | `07_factorial.py` | `factorial(n)` | Computes factorial iteratively *(no recursion)* |
| 08 | `08_count_digits.py` | `count_digits(n)` | Counts digits using a `while` loop |
| 09 | `09_reverse_number.py` | `reverse_number(n)` | Reverses a number using `%` and `//` |
| 10 | `10_check_prime.py` | `check_prime(n)` | Checks primality using a loop |

### Section B — String Basics

| # | File | Function(s) | Description |
|---|------|-------------|-------------|
| 11 | `11_count_characters.py` | `count_characters(text)` | Counts characters *(no `len()`)* |
| 12 | `12_count_vowels.py` | `count_vowels(text)` | Counts vowels in a string |
| 13 | `13_count_consonants.py` | `count_consonants(text)` | Counts consonants in a string |
| 14 | `14_count_vowels_consonants.py` | `count_vowels_consonants(text)` | Counts vowels and consonants separately |
| 15 | `15_reverse_string.py` | `reverse_string_loop(text)` / `reverse_string_slicing(text)` | Reverses a string — loop and slicing approaches |
| 16 | `16_check_palindrome.py` | `check_palindrome(text)` | Checks if a string is a palindrome |
| 17 | `17_count_words.py` | `count_words(text)` | Counts words *(no `split()`)* |
| 18 | `18_character_frequency.py` | `character_frequency(text, ch)` | Finds frequency of a character *(no `count()`)* |
| 19 | `19_remove_spaces.py` | `remove_spaces(text)` | Removes all spaces using a loop |
| 20 | `20_convert_uppercase.py` | `convert_upperc_builtin(text)` / `convert_upperc_loop(text)` | Converts to uppercase — built-in and loop-based |

### Section C — Strings + Loops

| # | File | Function(s) | Description |
|---|------|-------------|-------------|
| 21 | `21_count_case.py` | `count_case(text)` | Counts uppercase, lowercase, digits, and spaces |
| 22 | `22_first_character.py` | `first_character(text)` | Finds the first character using a loop and `break` |
| 23 | `23_last_character.py` | `last_ch_indexing(text)` / `last_ch_loop(text)` | Finds the last character — indexing and loop approaches |
| 24 | `24_display_characters.py` | `display_characters(text)` | Prints each character on a new line |
| 25 | `25_display_position.py` | `display_position(text)` | Prints each character with its index position |
| 26 | `26_remove_vowels.py` | `remove_vowels(text)` | Removes vowels *(no `replace()`)* |
| 27 | `27_find_longest_word.py` | `longest(text)` / `length(word)` | Finds the longest word *(no `max()`, no dictionaries)* |
| 28 | `28_count_each_vowel.py` | `count_each_vowel(text)` | Counts occurrences of each vowel individually |

### Section D — Loops & Patterns

| # | File | Function(s) | Description |
|---|------|-------------|-------------|
| 29 | `29_star_pattern.py` | `star_p(n)` | Prints a star pattern using nested loops |
| 30 | `30_number_pattern.py` | `number_p(n)` | Prints a number pattern using nested loops |

---

## Topics Covered

- Function design and return values
- Conditional logic (`if` / `elif` / `else`)
- Iteration (`for`, `while`, `break`)
- Manual string traversal and manipulation
- Numeric manipulation using `%` and `//`
- Nested loops for pattern generation

## Project Structure

```
Python Assignment/
├── 01_check_even_odd.py
├── 02_check_number.py
├── 03_find_largest_two.py
├── 04_find_largest_three.py
├── ...
├── 29_star_pattern.py
└── 30_number_pattern.py
```

## Getting Started

Each script is self-contained and can be run independently:

```bash
python 01_check_even_odd.py
```

Most scripts prompt for input directly in the terminal (e.g. `input("Enter a sentence: ")`) — run the file and follow the prompt.

## Design Notes & Restrictions

Several exercises intentionally forbid built-in shortcuts to reinforce manual problem-solving:

- **No `max()`** — comparisons are done explicitly with `if` / `else`
- **No dictionaries** — counters and lookups use plain variables and loops
- **No `split()` / `count()` / `replace()`** — string operations are implemented via character-by-character traversal
- **No recursion** for factorial — implemented iteratively

Files 15, 20, and 23 include two implementations of the same problem — one restricted (loop-based) and one idiomatic (built-in/slicing) — for side-by-side comparison.

## Requirements

- Python 3.x
- No external dependencies

## License

This project is free to use, fork, and adapt for personal learning or coursework.
