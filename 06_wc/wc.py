#!/usr/bin/env python3
"""
Author : david <david@localhost>
Date   : 2020-08-07
Purpose: wc
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='wc',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    num_lines_total, num_words_total, num_bytes_total = 0, 0, 0

    for fh in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
            num_lines_total += 1
            num_words_total += len(line.split())
            num_bytes_total += len(line)

        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')

    if len(args.file) > 1:
        print(
            f'{num_lines_total:8}{num_words_total:8}{num_bytes_total:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
