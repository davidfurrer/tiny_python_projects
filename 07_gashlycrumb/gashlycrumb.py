#!/usr/bin/env python3
"""
Author : david <david@localhost>
Date   : 2020-08-10
Purpose: Gashlycrumb
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='str',
                        help='One or more letter(s).',
                        nargs='+')

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt',
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    gash_dict = {}
    for line in args.file:
        gash_dict[line[0].upper()] = line.rstrip()

    for letter in args.letter:
        if letter.upper() in gash_dict:
            print(gash_dict[letter.upper()])
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
