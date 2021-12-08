def decode_output_values(mapping, output_values):
  output = ''
  for value in output_values.split():
    sorted_value = ''.join(sorted(value))
    output += str(mapping[sorted_value])
  return int(output)

sum_of_outputs = 0
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    signal_patterns, output_values = line.split(' | ')
    signal_patterns_by_length = {}
    mapping = {}
    for value in signal_patterns.split():
      sorted_value = ''.join(sorted(value))
      value_length = len(sorted_value)
      if value_length not in signal_patterns_by_length:
        signal_patterns_by_length[value_length] = []
      signal_patterns_by_length[value_length].append(sorted_value)

    display_one = signal_patterns_by_length[2][0]
    mapping[display_one] = 1

    display_four = signal_patterns_by_length[4][0]
    mapping[display_four] = 4

    display_seven = signal_patterns_by_length[3][0]
    mapping[display_seven] = 7

    display_eight = signal_patterns_by_length[7][0]
    mapping[display_eight] = 8

    display_four_without_one = ''.join([char for char in display_four if char not in display_one])

    display_zero = None
    display_six = None
    display_nine = None
    for signal in signal_patterns_by_length[6]:
      if set(signal) >= set(display_four):
        display_nine = signal
      elif set(signal) >= set(display_four_without_one):
        display_six = signal

    display_zero = next(signal for signal in signal_patterns_by_length[6] if signal not in [display_six, display_nine])
    mapping[display_zero] = 0
    mapping[display_six] = 6
    mapping[display_nine] = 9

    display_two = None
    display_three = None
    display_five = None
    for signal in signal_patterns_by_length[5]:
      if set(signal) >= set(display_one):
        display_three = signal
      elif set(display_six) >= set(signal):
        display_five = signal

    display_two = next(signal for signal in signal_patterns_by_length[5] if signal not in [display_three, display_five])
    mapping[display_two] = 2
    mapping[display_three] = 3
    mapping[display_five] = 5

    sum_of_outputs += decode_output_values(mapping, output_values)

print(sum_of_outputs)
