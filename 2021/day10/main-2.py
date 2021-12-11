import math

OPENING_CHARS = ["[", "(", "{", "<"]
CLOSING_CHARS = ["]", ")", "}", ">"]
SYNTAX_SCORE_VALUES = {
  "]": 57,
  ")": 3,
  "}": 1197,
  ">": 25137
}
COMPLETION_SCORE_VALUES = {
  "[": 2,
  "(": 1,
  "{": 3,
  "<": 4
}

def offending_chars(line):
  stack = []
  for char in line:
    if char in OPENING_CHARS:
      stack.append(char)
    elif char in CLOSING_CHARS:
      last_open_tag = stack.pop()
      if last_open_tag == "[" and char != "]":
        return [char]
      if last_open_tag == "(" and char != ")":
        return [char]
      if last_open_tag == "{" and char != "}":
        return [char]
      if last_open_tag == "<" and char != ">":
        return [char]

  if stack:
    return stack

syntax_error_score = 0
auto_complete_scores = []
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    chars = offending_chars(line)
    if chars[0] in SYNTAX_SCORE_VALUES:
      syntax_error_score += SYNTAX_SCORE_VALUES[chars[0]]
    else:
      cur_score = 0
      for char in chars[::-1]:
        cur_score = (cur_score * 5) + COMPLETION_SCORE_VALUES[char]
      auto_complete_scores.append(cur_score)

num_auto_complete_scores = len(auto_complete_scores)
middle_score = sorted(auto_complete_scores)[int(math.floor(num_auto_complete_scores / 2))]

print(syntax_error_score)
print(middle_score)
