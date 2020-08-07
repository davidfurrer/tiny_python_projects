#!/usr/bin/env python3
"""
Author : david <david@localhost>
Date   : 2020-08-07
Purpose: Howler
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='text input or path to text file')

    parser.add_argument('-o',
                        '--outfile',
                        help='save output to this file',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    if os.path.isfile(text):
        with open(text, 'r') as f:
            text = f.read()

    if args.outfile:
        with open(args.outfile, 'wt') as f:
            f.write(text.upper())
    else:
        print(text.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
