#!/usr/bin/env python3
"""
Author : david <david@localhost>
Date   : 2020-08-07
Purpose: Picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--sorted',
        action='store_true',  # this means store True for s
        help='sorts items',
        default=False)

    parser.add_argument('picnic_items',
                        metavar='list',
                        nargs='+',
                        help='list of items for picnic')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.picnic_items
    if args.sorted:
        items.sort()
    sentence = 'You are bringing '
    if len(items) == 1:
        print(sentence + items[0] + '.')
    elif len(items) == 2:
        print(f'{sentence}{items[0]} and {items[1]}.')
    else:
        # join all except last:
        all_itmes_except_last = ', '.join(items[:-1])
        print(f'{sentence}{all_itmes_except_last}, and {items[-1]}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
