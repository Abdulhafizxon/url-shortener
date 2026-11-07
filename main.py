import string
# import sys
base = 62
alphabet = string.digits + string.ascii_letters
alpha_dic = {symbol: i for i, symbol in enumerate(alphabet)}


def encode(num: int) -> str:
    if num == 0:
        return '0'
    result = []

    if num < 0:
        raise ValueError("Number should be non-negative number")

    # i = 0
    # print(alphabet)
    while num > 0:
        # print(i, num)
        # i += 1
        remainder = int(num % base)
        num //= base
        result.append(alphabet[remainder])

    # result.append(str(num))
    result = result[::-1]
    str_result = "".join(result)
    # str_result = str_result[::-1]
    return str_result


def decode(encoded_str: str) -> int:
    if len(encoded_str) == 0:
        raise ValueError("Input shouldn't empty")
    # i = 0
    result = 0
    # print(alphabet)
    # print(alpha_dic)
    for char in encoded_str:
        if char not in alpha_dic:
            raise ValueError(f"Invalid character {char!r} in your code")
        result = result * base + alpha_dic[char]

    return result


def main():
    print(encode(-10))


if __name__ == "__main__":
    main()
