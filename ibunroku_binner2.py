import os
import struct

def from_bin(file_path):
    """
    Extracts binary files from a BIN file.

    Args:
        file_path (str): Path to the BIN file.
    """
    CHUNK = 2048
    pointers = [0]
    folder_name = file_path.rstrip(".BIN") + "/"

    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

    with open(file_path, 'rb') as f:
        data = f.read()
        i = 0
        while True:
            pointer = struct.unpack('<H', data[i:i+2])[0] * CHUNK
            if i > 0:
                pointer += 154
            pointers.append(pointer)
            i += 2
            if data[i:i+2] == b'\x00\x00':
                break

        for p in range(1, len(pointers) - 1):
            file_start = pointers[p]
            file_end = file_start + struct.unpack('<H', data[pointers[p]+4:pointers[p]+6])[0] + 8
            with open(f'{folder_name}{p}.bin', 'wb') as f2:
                f2.write(data[file_start:file_end])
                print(f'{p}.bin extracted!')

def to_bin(folder_path):
    """
    Assembles binary files into a BIN file.

    Args:
        folder_path (str): Path to the folder containing binary files.
    """
    CHUNK = 2048
    header = b'\x01\x00'
    bytestream = b''
    bin_name = folder_path.rstrip("/") + ".BIN"

    with open(bin_name, 'wb') as f:
        i = 1
        size = CHUNK
        while True:
            file_path = f'{folder_path}/{i}.bin'
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f2:
                    data = f2.read()
                    while len(data) % CHUNK != 0:
                        data += b'\x00'
                    size += len(data)
                    if i == 1:
                        data += b'\x00' * 154
                    bytestream += data
                    header += struct.pack('<H', size // CHUNK)
                    i += 1
            else:
                break
        header += b'\x00' * (CHUNK - len(header))
        f.write(header)
        f.write(bytestream)

    print(f'{i-1} files imported!')
    print(f'{bin_name} assembled!')

if __name__ == "__main__":
    def main():
        """Main function to handle user input and execute bin operations."""
        print("Ibunroku Binner")
        while True:
            print("Usage:")
            print("To import into BIN file: [import] [folder path]")
            print("To export from BIN to files: [export] [file path]")
            user_input = input()
            try:
                command, path = user_input.split(" ")
                if command == "import":
                    to_bin(path)
                elif command == "export":
                    from_bin(path)
            except ValueError:
                print("Invalid input. Please try again.")

    main()
