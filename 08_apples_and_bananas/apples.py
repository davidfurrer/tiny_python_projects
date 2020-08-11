#!/usr/bin/env python3
"""
Author : david <david@localhost>
Date   : 2020-08-10
Purpose: Apples
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='A vowel',
                        metavar='str',
                        default='a',
                        type=str,
                        choices=list('aeiou'))

    return parser.parse_args()


def replace_vowels(text: str, x: str):
    new_text = []
    for char in text:
        if char in 'aeiou':
            new_text.append(x)
        elif char in 'AEIOU':
            new_text.append(x.upper())
        else:
            new_text.append(char)
    return ''.join(new_text)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    print(replace_vowels(args.text, args.vowel))


# --------------------------------------------------
if __name__ == '__main__':
    main()
