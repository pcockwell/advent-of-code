def check_board(board):
  empty_columns = [0, 1, 2, 3, 4]
  for r_idx, row in enumerate(board):
    row_victory = True
    for idx in range(5):
      if row[idx] != '':
        row_victory = False
        if idx in empty_columns:
          empty_columns.remove(idx)
    if row_victory:
      break

  col_victory = len(empty_columns) > 0
  return col_victory or row_victory


def calculate_score(board, last_num_called):
  sum_of_unmarked_numbers = 0
  for row in board:
    for val in row:
      if val != '':
        sum_of_unmarked_numbers += int(val)

  return sum_of_unmarked_numbers * last_num_called


def winning_bingo_board_score():
  number_draws = None
  boards = []
  current_board = []
  with open("data-1.txt", "r") as data_file:
    for line in data_file.readlines():
      if number_draws is None:
        number_draws = line.split(',')
      elif line == '\n':
        if current_board:
          boards.append(current_board)
        current_board = []
      else:
        current_board.append(line.split())

    if current_board:
      boards.append(current_board)

    for value in number_draws:
      for board_idx, board in enumerate(boards):
        for row_num in range(len(board)):
          if value in board[row_num]:
            board[row_num] = [n if value != n else '' for n in board[row_num]]
            if check_board(board):
              return calculate_score(board, int(value))

print(winning_bingo_board_score())
