#!/usr/bin/env python3
"""
Author : cayalaortiz <cayalaortiz@localhost>
Date   : 2023-04-16
Purpose: Run-length encoding/data compression
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type=str,
                        help='DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, encoding='utf-8') as fh:
            args.text = fh.read()
    else:
        args.text = args.text

    return args


# --------------------------------------------------
def rle(seq):
    """Make a jazz noise here"""

    encoded = []
    i = 0

    while i <= len(seq) - 1:
        count = 1
        encoded.append(seq[i])
        j = i
        while j < len(seq) - 1:
            if seq[j] == seq[j + 1]:
                count += 1
                j += 1
            else:
                break
        encoded.append(str(count))
        i = j + 1

    encoded = [e for e in encoded if e != '1']

    encoded = ''.join(encoded)

    return encoded


# --------------------------------------------------
def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for seq in args.text.splitlines():
        print(rle(seq))


# --------------------------------------------------
if __name__ == '__main__':
    main()
