# algorithm designed to encode a string of characters into a binary code
# using huffman coding


# class representing frequency of a character in a string. Here just to substitute usage of tuples
# and to practice a little bit of OOP

class Frequency:
    def __init__(self, char, fr) -> None:
        self.char = char
        self.fr = fr

    # if compared with same class, compare their frequencies. Otherwise compare hashes
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, self.__class__):
            return self.fr == __o.fr
        return hash(self) == hash(__o)

    def __gt__(self, __o: object) -> bool:
        if isinstance(__o, self.__class__):
            return self.fr > __o.fr
        return False

    def __hash__(self) -> int:
        return hash(self.char)

    def __str__(self) -> str:
        return f"{self.char}: {self.fr}"

    def __len__(self) -> int:
        return len(self.char)

    def __add__(self, __o: object) -> object:
        if isinstance(__o, self.__class__):
            return Frequency(self.char + __o.char, self.fr + __o.fr)
        raise TypeError("Can't use addition here")


# self-explanatory
def count_frequency(string: str) -> list[Frequency]:
    result = list()
    for char in string:
        if char in result:
            continue
        result.append(Frequency(char, string.count(char)))
    return result


def extract_min(fr_list: list) -> Frequency:
    key = fr_list.index(min(fr_list))
    return fr_list.pop(key)


def build_tree(fr_list: list) -> tuple[Frequency, list]:
    n = len(fr_list)
    tree = list()
    for _ in range(n - 1):
        first = extract_min(fr_list)
        second = extract_min(fr_list)
        tree.extend((first, second))
        fr_list.append(first + second)
    tree.sort(key=lambda x: x.fr, reverse=True)
    return fr_list[0], tree


def encode_char(char: str, root: Frequency, tree: list) -> str:
    # if there are no char pairs, like in case of 'aaaaaa' string, then code is just 'a': 0
    if not tree:
        return '0'
    code = ''
    current_leaf = root
    while len(current_leaf) > 1:
        for fr in tree:
            if (len(fr) < len(current_leaf) and 
                fr.char in current_leaf.char and
                char in fr.char):
                code += '0' if current_leaf.char.startswith(fr.char) else '1'
                current_leaf = fr
                break
    return code


def encode_all_chars(string: str, root: Frequency, tree: list) -> dict:
    code_dict = dict()
    for char in string:
        if char in code_dict:
            continue
        code_dict[char] = encode_char(char, root, tree)
    return code_dict


def encode_string(code_dict: dict, string: str) -> str:
    code = ''
    for char in string:
        code += code_dict[char]
    return code


# unlike code_dict, which contains chars as keys and codes as values, decode_dict should be reversed
# codes are keys, chars are values
def decode_string(decode_dict: dict, code: str) -> str:
    string = ''
    buffer = ''
    for char in code:
        buffer += char
        if buffer in decode_dict:
            string += decode_dict[buffer]
            buffer = ''
    return string


def main():
    string = input()
    frequency_list = count_frequency(string)
    root, tree = build_tree(frequency_list)
    frequency_list.clear()
    code_dict = encode_all_chars(string, root, tree)
    code = encode_string(code_dict, string)
    # what is shown by this print: amount of distinct chars in given string, length of encoded string...
    print(len(set(string)), len(code))
    # ...dictionary in form: ['char': 'code']...
    for key in sorted(code_dict.keys()):
        print(f"{key}: {code_dict[key]}")
    # ...aaand encoded string itself.
    print(code)


if __name__ == '__main__':
    main()