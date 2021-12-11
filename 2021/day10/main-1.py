OPENING_CHARS = ["[", "(", "{", "<"]
CLOSING_CHARS = ["]", ")", "}", ">"]
SYNTAX_SCORE_VALUES = {
  "]": 57,
  ")": 3,
  "}": 1197,
  ">": 25137
}

def validate_line(line):
  stack = []
  for char in line:
    if char in OPENING_CHARS:
      stack.append(char)
    elif char in CLOSING_CHARS:
      last_open_tag = stack.pop()
      if last_open_tag == "[" and char != "]":
        return False, char
      if last_open_tag == "(" and char != ")":
        return False, char
      if last_open_tag == "{" and char != "}":
        return False, char
      if last_open_tag == "<" and char != ">":
        return False, char

  if stack:
    return False, stack.pop()

  return True, None

syntax_error_score = 0
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    valid, offending_char = validate_line(line)
    if not valid and offending_char in SYNTAX_SCORE_VALUES:
      syntax_error_score += SYNTAX_SCORE_VALUES[offending_char]

print(syntax_error_score)
