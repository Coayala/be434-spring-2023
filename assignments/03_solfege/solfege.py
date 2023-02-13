#!/usr/bin/env python3
"""
Author : cayalaortiz <cayalaortiz@localhost>
Date   : 2023-02-12
Purpose: Solfege
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Solfege',
                        nargs='+')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    som_dict = {
        'Do': 'A deer, a female deer',
        'Re': 'A drop of golden sun',
        'Mi': 'A name I call myself',
        'Fa': 'A long long way to run',
        'Sol': 'A needle pulling thread',
        'La': 'A note to follow sol',
        'Ti': 'A drink with jam and bread'
    }

    verse_list = [', '.join([note,
                            som_dict.get(note, "replace")])
                  if note in som_dict
                  else f'I don\'t know "{note}"'
                  for note in args.str]

    print('\n'.join(verse_list))


# --------------------------------------------------
if __name__ == '__main__':
    main()
