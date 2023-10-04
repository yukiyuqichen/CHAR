import os
import msgpack

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
data_dir = os.path.join(parent_dir, 'data')

class CharConverter:
    def __init__(self, option='v2s'):
        """
        Initialize the converter with a option format.

        :param option: option format, either 'v2s' (simplified) or 'v2t' (traditional).
        """
        if option not in ['v2s', 'v2t']:
            raise ValueError("Option must be either 'v2s' (simplified) or 'v2t' (traditional).")
        mapping_file_path = os.path.join(data_dir, f"{option}.msgpack")
        with open(mapping_file_path, 'rb') as f:
            self.mapping = msgpack.unpack(f, raw=False)

    def convert(self, text):
        """
        Convert the text based on the mapping.

        :param text: The input text.
        :return: Converted text.
        """
        converted_text = [self.mapping.get(char, [char])[0] for char in text]
        return ''.join(converted_text)
