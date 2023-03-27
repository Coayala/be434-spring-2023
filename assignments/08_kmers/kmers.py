#!/usr/bin/env python3
"""
Author : cayalaortiz <cayalaortiz@arizona.edu>
Date   : 2023-03-26
Purpose: Find common kmers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
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

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    if args.kmer <= 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def get_kmers(string, kmer_len):
    """Function to get the kmers from a string"""

    kmers = []
    for i in range(0, len(string) + 1):
        ss = string[i:i + kmer_len]
        if len(ss) == kmer_len:
            kmers.append(ss)
    return kmers


# --------------------------------------------------
def count_kmers(file, kmer_len):
    """Function to count the kmers in a file"""

    kmer_dict = {}
    for line in file:
        kmers = []
        for word in line.split():
            kmers.extend(get_kmers(word, kmer_len))
        for mer in kmers:
            if mer not in kmer_dict:
                kmer_dict[mer] = 0
            kmer_dict[mer] += 1

    return kmer_dict


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # Initializing dictionary for counting kmers

    kmer_file1 = count_kmers(args.f1, args.kmer)
    kmer_file2 = count_kmers(args.f2, args.kmer)

    set_file1 = set(kmer_file1)
    set_file2 = set(kmer_file2)

    for mer in set_file1.intersection(set_file2):
        print(f'{mer:<10}{kmer_file1[mer]:>6}{kmer_file2[mer]:>6}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
