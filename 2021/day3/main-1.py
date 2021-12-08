bit_sums = {}
num_lines = 0
num_digits = None
gamma_rate = []
epsilon_rate = []
with open("data-1.txt", "r") as data_file:
  for line in data_file.readlines():
    num_lines += 1
    num_digits = len(line.strip())
    for idx in range(num_digits):
      if idx not in bit_sums:
        bit_sums[idx] = 0
      bit_sums[idx] += int(line[idx])
  for idx in range(num_digits):
    if bit_sums[idx] > num_lines / 2.0:
      gamma_rate.append(1)
      epsilon_rate.append(0)
    else:
      gamma_rate.append(0)
      epsilon_rate.append(1)

print(gamma_rate)
print(epsilon_rate)
gamma_rate = int(''.join([str(i) for i in gamma_rate]), 2)
epsilon_rate = int(''.join([str(i) for i in epsilon_rate]), 2)

power_consumption = gamma_rate * epsilon_rate
print(power_consumption)
