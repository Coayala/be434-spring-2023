#!/usr/bin/env python3
"""
Author : cayalaortiz <cayalaortiz@arizona.edu>
Date   : 2023-02-05
Purpose: Add numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        metavar='INT',
                        type=int,
                        nargs='+',
                        help='Numbers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    numbers_list = args.numbers

    if len(numbers_list) == 1:
        print(f'{numbers_list[0]} = {numbers_list[0]}')
    else:
        numbers_sum = sum(numbers_list)
        str_list = [str(num) for num in numbers_list]
        numbers_str = ' + '.join(str_list)

        print(f'{numbers_str} = {numbers_sum}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
