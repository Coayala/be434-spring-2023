#!/usr/bin/env python3
"""
Author : cayalaortiz <cayalaortiz@arizona.edu>
Date   : 2023-02-19
Purpose: Python cat
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true',
                        default=False)

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    num_lines = 0

    for fh in args.file:
        for line in fh:
            num_lines += 1
            if not args.number:
                text = line.rstrip()
            else:
                text = f'     {str(num_lines)}\t{line.rstrip()}'
            print(text)
        num_lines = 0


# --------------------------------------------------
if __name__ == '__main__':
    main()
