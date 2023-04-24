#!/usr/bin/env python3
"""
Author : cayalaortiz <cayalaortiz@arizona.edu>
Date   : 2023-04-23
Purpose: Python grep
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        help='Search pattern',
                        metavar='PATTERN',
                        type=str,
                        default=None)

    parser.add_argument('input',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.input:
        for line in fh:
            if args.insensitive:
                search_res = re.search(args.pattern, line, flags=re.I)
            else:
                search_res = re.search(args.pattern, line)

            line_start = f'{fh.name}:' if len(args.input) > 1 else ''

            if search_res:
                args.outfile.write(f'{line_start}{line}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
