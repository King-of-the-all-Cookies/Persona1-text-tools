import codecs

def load_encoding_table(file_path):
    """
    Loads the encoding table from a file and returns a dictionary mapping hex codes to characters or commands.

    Args:
        file_path (str): Path to the encoding table file.

    Returns:
        dict: Dictionary mapping hex codes to characters or commands.
    """
    encoding_table = {}
    with codecs.open(file_path, 'r', encoding='utf_8') as file:
        for line in file:
            line = line.strip()
            if line and '=' in line:
                hex_code, char = line.split('=')
                encoding_table[hex_code.strip()] = char.strip()
    return encoding_table

# Mapping of commands used in the game
commands = [
    '[wait]', '[end]', '[nl]'
]

# Mapping of Russian characters to their byte values
russian = [
    'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', '¨', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î',
    'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß'
]

# Mapping of hex strings to binary strings
hex_from_str = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
    '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}
