#!/usr/bin/python3

import sys


def display_info(status_counts, cumulative_file_size):
    """
    Method to print
    Args:
        status_counts: dict of status codes
        cumulative_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(cumulative_file_size))
    for key, val in sorted(status_counts.items()):
        if val != 0:
            print("{}: {}".format(key, val))


cumulative_file_size = 0
status_code = 0
line_counter = 0
status_counts = {"200": 0,
                 "301": 0,
                 "400": 0,
                 "401": 0,
                 "403": 0,
                 "404": 0,
                 "405": 0,
                 "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            line_counter += 1

            if line_counter <= 10:
                cumulative_file_size += int(parsed_line[0])  # file size
                status_code = parsed_line[1]  # status code

                if (status_code in status_counts.keys()):
                    status_counts[status_code] += 1

            if (line_counter == 10):
                display_info(status_counts, cumulative_file_size)
                line_counter = 0

finally:
    display_info(status_counts, cumulative_file_size)
