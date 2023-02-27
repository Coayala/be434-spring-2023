#!/usr/bin/env python3
"""
Author : cayalaortiz <cayalaortiz@localhost>
Date   : 2023-02-26
Purpose: Translate DNA/RNA to proteins
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence', metavar='str', help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # Creating codon table
    codon_table = {line.split()[0]: line.split()[1] for line in args.codons}

    k = 3
    seq = args.sequence
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        translation = codon_table.get(codon.upper(), '-')
        args.outfile.write(translation)

    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
