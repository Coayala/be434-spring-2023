#!/usr/bin/env python3
"""
Author : cayalaortiz <cayalaortiz@localhost>
Date   : 2023-05-02
Purpose: Vigenere Cipher
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Vigenere Cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-k',
                        '--keyword',
                        help='A keyword',
                        metavar='KEYWORD',
                        type=str,
                        default='CIPHER')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_XL = alpha * 2

    alpha_values = {alpha[i]: i for i in range(len(alpha))}

    if not args.decode:
        for line in args.input:
            line = line.upper().rstrip()
            kidx = 0
            enc_line = []

            for i, letter in enumerate(line):
                if letter in alpha:
                    value_line = alpha_values[letter]
                    value_keyword = alpha_values[args.keyword[kidx]]
                    new_letter = alpha_XL[value_line + value_keyword]
                    enc_line.append(new_letter)
                    kidx = 0 if kidx + 1 == len(args.keyword) else kidx + 1
                else:
                    enc_line.append(letter)

            args.outfile.write(f"{''.join(enc_line)}\n")
    else:
        for line in args.input:
            kidx = 0
            dec_line = []

            for i, letter in enumerate(line):
                if letter in alpha:
                    value_line = alpha_values[letter]
                    value_keyword = alpha_values[args.keyword[kidx]]
                    new_letter = alpha_XL[value_line - value_keyword]
                    dec_line.append(new_letter)
                    kidx = 0 if kidx + 1 == len(args.keyword) else kidx + 1
                else:
                    dec_line.append(line[i])

            args.outfile.write(f"{''.join(dec_line)}")


# --------------------------------------------------
if __name__ == '__main__':
    main()
