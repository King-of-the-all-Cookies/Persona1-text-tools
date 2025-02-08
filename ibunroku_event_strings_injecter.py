import os
import struct
import codecs
import json
from ibunroku_settings import load_encoding_table, commands, russian, hex_from_str

def from_hex_str(s):
    """Converts a hex string to an integer."""
    bin_ = ''.join(hex_from_str[v] for v in s)
    bin_ = bin_[8:] + bin_[:8]
    return int(bin_, 2)

def inject_event_strings(bin_file_path, json_file_path, tbl_path):
    """
    Injects event strings from a JSON file into a binary file.

    Args:
        bin_file_path (str): Path to the original binary file.
        json_file_path (str): Path to the JSON file containing parsed strings.
        tbl_path (str): Path to the encoding table file.
    """
    encoding_table = load_encoding_table(tbl_path)

    with open(bin_file_path, 'rb') as binfile:
        binfile_data = binfile.read()

    with codecs.open(json_file_path, 'r', encoding='utf_8') as jsonfile:
        json_data = json.load(jsonfile)

        # Extract header information
        header_size = json_data["Header"]["Header Size"]
        file_size = json_data["Header"]["File Size"]
        music = json_data["Header"]["Music"]
        end_text_table = json_data["Header"]["End of Text Table"]
        unk_pointer1 = json_data["Header"]["Unknown Pointer 1"] - end_text_table
        unk_pointer2 = json_data["Header"]["Unknown Pointer 2"] - end_text_table
        unk_pointer3 = json_data["Header"]["Unknown Pointer 3"] - end_text_table
        script_table_pointer = json_data["Header"]["Script Table Pointer"]
        text_table_pointer = json_data["Header"]["Text Table Pointer"]
        data_after = json_data["Other Data"]

        # Prepare kanji dictionary
        kanji = {v: k for k, v in encoding_table.items()}

        # Convert strings and update pointers
        textblock = b''
        new_pointers = [text_table_pointer]
        text_pointer = text_table_pointer

        for s in json_data["Parsed strings"]:
            converted_s = b''
            i = 0
            while i < len(json_data["Parsed strings"][s]):
                char_s = json_data["Parsed strings"][s][i]
                if char_s in russian:
                    converted_s += struct.pack('B', russian.index(char_s))
                    i += 1
                elif char_s in encoding_table.values():
                    char_hex_code = [k for k, v in encoding_table.items() if v == char_s][0]
                    converted_s += struct.pack('B', int(char_hex_code, 16))
                    i += 1
                elif char_s == "|":
                    kanji_hex_code = json_data["Parsed strings"][s][i+1:i+5]
                    converted_s += struct.pack('H', from_hex_str(kanji_hex_code))
                    i += 5
                elif char_s == '[':
                    command = ''
                    j = 1
                    while ']' not in command:
                        command += json_data["Parsed strings"][s][i+j]
                        j += 1
                    if '=' in command:
                        command = command.split('=')
                        command_index = commands.index(f'[{command[0]}]')
                        if command[0] == "WAIT":
                            converted_s += b'\xFF' + struct.pack('B', command_index) + struct.pack('B', int(command[1].rstrip(']'))) + b'\x00'
                        else:
                            converted_s += b'\xFF' + struct.pack('B', command_index) + struct.pack('B', int(command[1].rstrip(']')))
                    else:
                        converted_s += b'\xFF' + struct.pack('B', commands.index(f'[{command}]'))
                    i += j
                else:
                    kanji_hex_code = kanji[char_s]
                    converted_s += struct.pack('>H', from_hex_str(kanji_hex_code))
                    i += 1
            text_pointer += len(converted_s)
            new_pointers.append(text_pointer)
            textblock += converted_s

        # Update file size and pointers
        file_size = text_table_pointer + len(textblock) + len(data_after)
        end_text_table = text_table_pointer + len(textblock)
        unk_pointer1 += end_text_table
        unk_pointer2 += end_text_table
        unk_pointer3 += end_text_table

        # Update text pointers in the binary file
        new_table = binfile_data[:text_table_pointer+8]
        for i, s in enumerate(json_data["Parsed strings"]):
            new_table = new_table[:int(s)+8] + struct.pack('<H', new_pointers[i]) + new_table[int(s)+10:]
        new_table = new_table[script_table_pointer:]

        # Inject data into the new binary file
        with open(bin_file_path + "_", 'wb') as f2:
            f2.write(struct.pack('<H', header_size) + b'\x10\x80')
            f2.write(struct.pack('<H', file_size) + b'\x10\x80')
            f2.write(binfile_data[8:10])
            f2.write(struct.pack('<H', music))
            f2.write(binfile_data[12:60])
            f2.write(struct.pack('<H', end_text_table) + b'\x10\x80')
            f2.write(binfile_data[64:68])
            f2.write(struct.pack('<H', unk_pointer1) + b'\x10\x80')
            f2.write(binfile_data[72:76])
            f2.write(struct.pack('<H', unk_pointer2) + b'\x10\x80')
            f2.write(binfile_data[80:84])
            f2.write(struct.pack('<H', unk_pointer3) + b'\x10\x80')
            f2.write(binfile_data[88:104])
            f2.write(struct.pack('<H', script_table_pointer) + b'\x10\x80')
            f2.write(binfile_data[108:script_table_pointer])
            f2.write(new_table)
            f2.write(textblock)
            f2.write(bytes(data_after))

        print(f'Exported: {bin_file_path}_')

if __name__ == '__main__':
    while True:
        bin_file = input("Enter the path to the original bin file: ")
        json_file = input("Enter the path to the JSON file: ")
        tbl_file = input("Enter the path to the encoding table file: ")
        if os.path.isfile(bin_file) and os.path.isfile(json_file) and os.path.isfile(tbl_file):
            inject_event_strings(bin_file, json_file, tbl_file)
            break
