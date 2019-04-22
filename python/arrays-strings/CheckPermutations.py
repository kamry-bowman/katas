from collections import defaultdict


def check_permutations(str1, str2):
    if len(str1) != len(str2):
        return False

    quantity = defaultdict(int)

    for char in str1:
        quantity[char] += 1

    for char in str2:
        quantity[char] -= 1

        if quantity[char] < 0:
            return False

    for key in quantity:
        if quantity[char] > 0:
            return False

    return True


if __name__ == "__main__":
    print(check_permutations("cat", "tca"))
    print(check_permutations("tca", "cat"))
    print(check_permutations("cat", "taa"))
    print(check_permutations("taa", "cat"))
    print(check_permutations("garbage", "gbarage"))
    print(check_permutations("garbage", "gbaragg"))

# Space complexity: O(n)
# Time complexity: O(1)
