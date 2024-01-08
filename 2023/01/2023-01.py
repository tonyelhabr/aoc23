# %%
from aocd import get_data
from dotenv import load_dotenv
import re

load_dotenv()
d = get_data(day=1, year=2023)
lines = d.splitlines()

# %%
## don't use \d to match 0
DIGIT_PATTERN = "1|2|3|4|5|6|7|8|9"


def extract_first_digit(x: str) -> str:
    match = re.search(r"(" + DIGIT_PATTERN + r")", x)
    return match.group()


def extract_last_digit(x: str) -> str:
    rev_x = x[::-1]
    return extract_first_digit(rev_x)


# %%
combined_digits = [int(extract_first_digit(l) + extract_last_digit(l)) for l in lines]
sum(combined_digits)  ## first answer
# 56042

# %%
word_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
DIGIT_OR_DIGITLIKE_WORD_PATTERN = DIGIT_PATTERN + r"|" + r"|".join(word_to_digit.keys())


# %%
def extract_nth_digit_or_digitlike_word(x: str, n: int) -> str:
    matches = re.findall(r"(" + DIGIT_OR_DIGITLIKE_WORD_PATTERN + r")", x)
    nth_match = matches[n]
    return str(word_to_digit.get(nth_match, nth_match))


def extract_first_digit_or_digitlike_word(x: str) -> str:
    return extract_nth_digit_or_digitlike_word(x, n=0)


def extract_last_digit_or_digitlike_word(x: str) -> str:
    return extract_nth_digit_or_digitlike_word(x, n=-1)


# %%
combined_digits = [
    int(
        extract_first_digit_or_digitlike_word(l)
        + extract_last_digit_or_digitlike_word(l)
    )
    for l in lines
]
sum(combined_digits)  ## second answer
# 55362
# answer should be 55358

# %%
