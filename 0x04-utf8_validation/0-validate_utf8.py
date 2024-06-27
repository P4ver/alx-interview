#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding."""
    number_bytes = 0

    msk_x = 1 << 7
    msk_y = 1 << 6

    for m in data:

        msk_byte = 1 << 7

        if number_bytes == 0:

            while msk_byte & m:
                number_bytes += 1
                msk_byte = msk_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (m & msk_x and not (m & msk_y)):
                    return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
