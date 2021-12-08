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
  boards_in_play = []
  current_board = []
  last_score = None
  with open("data-1.txt", "r") as data_file:
    for line in data_file.readlines():
      if number_draws is None:
        number_draws = line.split(',')
      elif line == '\n':
        if current_board:
          boards_in_play.append(current_board)
        current_board = []
      else:
        current_board.append(line.split())

    if current_board:
      boards_in_play.append(current_board)

    for value in number_draws:
      if len(boards_in_play) == 0:
        return last_score

      boards_in_play_next_round = []
      for board in boards_in_play:
        board_victory = False
        for row_num in range(len(board)):
          if value in board[row_num]:
            board[row_num] = [n if value != n else '' for n in board[row_num]]
            if check_board(board):
              board_victory = True
              break

        if not board_victory:
          boards_in_play_next_round.append(board)
        else:
          last_score = calculate_score(board, int(value))

      boards_in_play = boards_in_play_next_round

print(winning_bingo_board_score())
