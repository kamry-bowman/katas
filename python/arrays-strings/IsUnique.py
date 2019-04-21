# check for uniqueness

# loop over characters
# check in hash table if already there
# if not add to hash table
# time-complexity N
# space-complexity N


# use a bit vector

# initialize bit vector
import array


def make_bit_array(size):
    intSize = size >> 5  # number of 32-bit integers
    if size & 31:
        intSize += 1    # increment intSize if size does not fit evenly into 32, so we can have the partial byte
    vector = array.array('I')
    vector.extend((0,) * intSize)
    return vector


def test_bit(vector, pos):
    record = pos >> 5
    offset = pos & 31

    mask = 1 << offset
    return vector[record] & mask


def set_bit(vector, pos):
    record = pos >> 5
    offset = pos & 31

    mask = 1 << offset
    vector[record] |= mask

    return vector


def char_is_duplicate(vector, char):
    return test_bit(vector, ord(char))


def save_char(vector, char):
    set_bit(vector, ord(char))


def is_unique(target):
    vector = make_bit_array(122)
    for char in target:
        if char_is_duplicate(vector, char):
            return False
        else:
            save_char(vector, char)
    return True


if __name__ == "__main__":
    print("run")
    print(is_unique("cat"))
    print(is_unique("hello"))
    print(is_unique("cat5"))
    print(is_unique("5cat5"))
