#!/usr/bin/env python3
"""
Author : cayalaortiz <cayalaortiz@arizona.edu>
Date   : 2023-04-09
Purpose: Find common words
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('f1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('f2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    words1 = []

    for line in args.f1:
        for word in line.split():
            if word not in words1:
                words1.append(word)

    words2 = []

    for line in args.f2:
        for word in line.split():
            if word not in words2:
                words2.append(word)

    set_file1 = set(words1)
    set_file2 = set(words2)

    for mer in set_file1.intersection(set_file2):
        args.outfile.write(f'{mer}\n')


# --------------------------------------------------
if __name__ == '__main__':
    main()
