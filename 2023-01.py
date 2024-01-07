#%%
from aocd import get_data
from dotenv import load_dotenv
import re

load_dotenv()
d = get_data(day=1, year=2023)
lines = d.splitlines()

#%%
def extract_first_digit(x: str) -> str:
    match = re.search(r'\d', x)
    return match.group() if match else None

def extract_last_digit(x: str) -> str:
    rev_x = x[::-1]
    return extract_first_digit(rev_x)

#%%
combined_digits = [int(extract_first_digit(l) + extract_last_digit(l)) for l in lines]
sum(combined_digits) ## first answer
# 56042

#%%
word_to_digit = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}
DIGIT_OR_DIGITLIKE_WORD_PATTERN = r'(\d|' + '|'.join(word_to_digit.keys()) + r')'

#%%
def extract_nth_digit_or_digitlike_word(x: str, n: int) -> str:
    matches = re.findall(DIGIT_OR_DIGITLIKE_WORD_PATTERN, x)
    ntch_match = matches[n]
    return str(word_to_digit.get(ntch_match, ntch_match))

def extract_first_digit_or_digitlike_word(x: str) -> str:
    return extract_nth_digit_or_digitlike_word(x, n=0)

def extract_last_digit_or_digitlike_word(x: str) -> str:
    return extract_nth_digit_or_digitlike_word(x, n=-1)

#%%
combined_digits = [int(extract_first_digit_or_digitlike_word(l) + extract_last_digit_or_digitlike_word(l)) for l in lines]
sum(combined_digits) ## first answer
# 55362

#%%
