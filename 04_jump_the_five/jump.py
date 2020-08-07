#!/usr/bin/env python3
"""
Author : david <david@localhost>
Date   : 2020-08-07
Purpose: Encrpyt phone number
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='jump',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sentence',
                        metavar='str',
                        help='sentence with phone number to encrypt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    encoding = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5',
    }

    sentence = ''.join(
        [encoding[x] if x.isdigit() else x for x in args.sentence])

    print(sentence)


# --------------------------------------------------
if __name__ == '__main__':
    main()
