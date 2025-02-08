import os
import struct
import codecs
import json
from ibunroku_settings import load_encoding_table, commands

def parse_event_strings(file_path, tbl_path):
    """
    Parses event strings from a binary file and saves the output to text and JSON files.

    Args:
        file_path (str): Path to the binary file.
        tbl_path (str): Path to the encoding table file.
    """
    encoding_table = load_encoding_table(tbl_path)

    with open(file_path, 'rb') as f:
        data = f.read()

        # Unpack header information
        header_size = struct.unpack('<H', data[:2])[0]
        file_size = struct.unpack('<H', data[4:6])[0]
        data = data[header_size:]

        # Extract pointers and other data
        music = struct.unpack('<H', data[2:4])[0]
        end_text_table_pointer = struct.unpack('<H', data[52:54])[0]
        other_data = data[end_text_table_pointer:file_size]
        unk_pointer1 = struct.unpack('<H', data[60:62])[0]
        unk_pointer2 = struct.unpack('<H', data[68:70])[0]
        unk_pointer3 = struct.unpack('<H', data[76:78])[0]
        table_pointer = struct.unpack('<H', data[96:98])[0]

        # Extract raw strings
        raw_strings = []
        i = table_pointer
        while data[i+2:i+4] != b'\x10\x80':
            i += 2
        text_table_pointer = struct.unpack('<H', data[i:i+2])[0]

        while i < text_table_pointer:
            if data[i+2:i+4] == b'\x10\x80' and data[i-4:i] == b'\xFF\x55\x00\x00':
                reader = struct.unpack('<H', data[i:i+2])[0]
                string = b''
                while data[reader:reader+2] != b'\xFF\x01':
                    string += struct.pack('B', data[reader])
                    reader += 1
                string += b'\xFF\x01\x00\x00'
                raw_strings.append((i, string))
                i += 4
            else:
                i += 4

        # Prepare header JSON
        header_json = {
            'Header Size': header_size,
            'File Size': file_size,
            'Music': music,
            'End of Text Table': end_text_table_pointer,
            'Unknown Pointer 1': unk_pointer1,
            'Unknown Pointer 2': unk_pointer2,
            'Unknown Pointer 3': unk_pointer3,
            'Script Table Pointer': table_pointer,
            'Text Table Pointer': text_table_pointer
        }

        # Decode strings using character dictionary
        strings = {}
        with codecs.open('output.txt', 'w', encoding="utf_8") as txt:
            for raw in raw_strings:
                decoded_string = ''
                i = 0
                while i < len(raw[1]):
                    char = raw[1][i]
                    if char < 0x80:
                        decoded_string += encoding_table.get(f'{char:02X}', f'[kana={char}]')
                        i += 1
                    elif char >= 0x80 and char < 0xFF:
                        char = int.from_bytes(raw[1][i:i+2], 'big')
                        char_hex = f'{char:04X}'
                        decoded_string += encoding_table.get(char_hex, f'|{char_hex}')
                        i += 2
                    else:
                        command = raw[1][i+1]
                        if command == 5:
                            wait = int.from_bytes(raw[1][i+2:i+3], 'big')
                            decoded_string += f'[WAIT={wait}]'
                            i += 4
                        elif command == 6:
                            color = raw[1][i+2]
                            decoded_string += f'[COLOR={color}]'
                            i += 3
                        elif command == 14:
                            something = raw[1][i+2]
                            decoded_string += f'[SOMETHING={something}]'
                            i += 3
                        else:
                            try:
                                decoded_string += commands[command]
                            except IndexError:
                                print(f'Unknown command {command} in file {file_path}')
                            i += 2
                strings[str(raw[0])] = decoded_string
                txt.write(f'{str(raw[0])}:\t{decoded_string}\n')

        # Save other data and strings to JSON
        with codecs.open('output.json', 'w', encoding='utf_8') as jsonf:
            json.dump({'Header': header_json, 'Parsed strings': strings, 'Other Data': list(other_data)}, jsonf, indent=4, ensure_ascii=False)
