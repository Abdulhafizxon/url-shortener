import pytest

from main import decode, encode


@pytest.mark.parametrize("number", [0, 1, 61, 62, 63, 3843, 3844, 10**9, 2**40])
def test_round_trip(number):
    assert decode(encode(number)) == number


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, "0"),
        (1, "1"),
        (61, "Z"),
        (62, "10"),
        (63, "11"),
        (478, "7I"),
        (3844, "100"),
    ],
)
def test_encode_known_values(number, expected):
    assert encode(number) == expected


@pytest.mark.parametrize(
    "code, expected",
    [
        ("0", 0),
        ("Z", 61),
        ("10", 62),
        ("11", 63),
        ("7I", 478),
        ("100", 3844),
    ],
)
def test_decode_known_values(code, expected):
    assert decode(code) == expected


def test_encode_gives_unique_codes():
    codes = {encode(n) for n in range(10_000)}
    assert len(codes) == 10_000


def test_encode_negative_raises():
    with pytest.raises(ValueError):
        encode(-1)


def test_decode_empty_string_raises():
    with pytest.raises(ValueError):
        decode("")


@pytest.mark.parametrize("bad_code", ["ab$", " ", "a b", "7I!"])
def test_decode_invalid_character_raises(bad_code):
    with pytest.raises(ValueError):
        decode(bad_code)
