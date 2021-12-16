from pprint import pprint

def parse_hex_packet(hex_code):
  binary_number = bin(int(hex_code, 16))[2:]
  num_zeroes_to_add = (4 - (len(binary_number) % 4)) % 4
  return binary_number.zfill(len(binary_number) + num_zeroes_to_add)

def parse_binary_packet(packet):
  version = int(packet[0:3], 2)
  packet_type = int(packet[3:6], 2)
  packet_contents = packet[6:]

  parsed_packet = {
    "version": version,
    "type": packet_type,
    "value": None,
    "operator": None,
    "subpackets": []
  }

  # Literal
  if packet_type == 4:
    binary_number = ''
    continue_processing = True
    while continue_processing:
      continue_processing = packet_contents[0] == '1'
      binary_number += packet_contents[1:5]
      if len(packet_contents) > 5:
        packet_contents = packet_contents[5:]
      else:
        packet_contents = ''

    parsed_packet["value"] = int(binary_number, 2)

  else:
    length_type = packet_contents[0]
    subpacket_contents = []

    if length_type == '0':
      length_of_subpackets = int(packet_contents[1:16], 2)
      packet_contents = packet_contents[16:]

      length_processed = 0
      while length_processed < length_of_subpackets:
        subpacket, residue = parse_binary_packet(packet_contents)
        subpacket_contents.append(subpacket)
        length_processed += (len(packet_contents) - len(residue))
        packet_contents = residue

    elif length_type == '1':
      num_subpackets = int(packet_contents[1:12], 2)
      packet_contents = packet_contents[12:]

      while len(subpacket_contents) < num_subpackets:
        subpacket, packet_contents = parse_binary_packet(packet_contents)
        subpacket_contents.append(subpacket)

    parsed_packet["operator"] = packet_type
    parsed_packet["subpackets"] = subpacket_contents

  return parsed_packet, packet_contents

def sum_of_versions(packet):
  version_sum = packet['version']
  for subpacket in packet['subpackets']:
    version_sum += sum_of_versions(subpacket)

  return version_sum

with open("data-1.txt", "r") as data_file:
  packet_binary = parse_hex_packet(data_file.readline().strip())

packet, residue = parse_binary_packet(packet_binary)
print(sum_of_versions(packet))

