from collections import Counter


def checkPalindromePerm(string):
    counter = Counter(string.lower().replace(" ", ""))

    odds = 0
    print(counter)
    for char, count in counter.items():
        if count % 2 == 1:
            odds += 1

    return odds < 2


if __name__ == "__main__":
    print(checkPalindromePerm("Tact Coa"))
    print(checkPalindromePerm("Tact Coaa"))

# time: O(n)
# space: O(n)
