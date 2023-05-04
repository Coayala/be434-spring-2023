#!/usr/bin/env python3
"""
Author : cayalaortiz <cayalaortiz@arizona.edu>
Date   : 2023-05-02
Purpose: Substitution Cipher
"""

import argparse
import sys
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Substitution Cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-s',
                        '--seed',
                        help='A random seed',
                        metavar='SEED',
                        type=int,
                        default=3)

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
def get_key(my_dict, val):
    """Return the key from a value in a dictionary"""

    return [k for k, v in my_dict.items() if v == val][0]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    coded_alpha = random.sample(alpha, 26)

    cipher_key = {alpha[i]: coded_alpha[i] for i in range(len(alpha))}

    if not args.decode:
        for line in args.input:
            enc_line = [
                cipher_key[letter.upper()]
                if letter.upper() in alpha else letter
                for letter in line.rstrip()
            ]
            args.outfile.write(f"{''.join(enc_line)}\n")
    else:
        for line in args.input:
            dec_line = [
                get_key(cipher_key, letter.upper())
                if letter.upper() in alpha else letter
                for letter in line.rstrip()
            ]
            args.outfile.write(f"{''.join(dec_line)}\n")


# --------------------------------------------------
if __name__ == '__main__':
    main()
