from string import ascii_lowercase as letters

def to_encrypt(text, n):
    # to decrypt: same function with negative n
    return text.translate(str.maketrans(letters, letters[n:]+letters[:n]))


if __name__ == '__main__':
    
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("all good")
