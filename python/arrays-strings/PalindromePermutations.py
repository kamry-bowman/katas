from collections import Counter


def checkPalindromePerm(string):

    vector = 0
    for char in string:
        if char == " ":
            continue
        index = ord(char.lower()) - ord("a")

        vector ^= 1 << index

    if vector == 0:
        return True

    odds = 0
    while vector > 0:
        if vector & 1:
            odds += 1
        vector = vector >> 1

    return odds < 2


if __name__ == "__main__":
    print(checkPalindromePerm("Tact Coa"))
    print(checkPalindromePerm("Tact Coaa"))
    print(checkPalindromePerm("aa bb"))
    print(checkPalindromePerm("aa bbb"))
    print(checkPalindromePerm("aaa bbb"))

# time: O(n)
# space: O(1)
