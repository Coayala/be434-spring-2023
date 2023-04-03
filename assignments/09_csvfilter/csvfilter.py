#!/usr/bin/env python3
"""
Author : cayalaortiz <cayalaortiz@arizona.edu>
Date   : 2023-04-02
Purpose: Filter delimited records
"""

import argparse
import pandas as pd


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        required=True)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        default=None,
                        required=True)

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Input file',
                        metavar='OUTFILE',
                        type=str,
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    args = parser.parse_args()

    if args.delimiter == '$\t':
        args.file = pd.read_csv(args.file.name, sep='\t', dtype=object)
    else:
        args.file = pd.read_csv(args.file.name, dtype=object)

    if args.col != '':
        if args.col not in args.file.columns:
            cols = ", ".join(args.file.columns)
            parser.error(
                f'--col "{args.col}" not a valid column!\nChoose from {cols}.')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if args.col != '':
        data_filt = args.file[args.file[args.col].str.contains(args.val,
                                                               case=False,
                                                               na=False)]
    else:
        data_filt = pd.DataFrame(columns=args.file.columns)
        for col in args.file.columns:
            temp_df = args.file[args.file[col].str.contains(args.val,
                                                            case=False,
                                                            na=False)]
            data_filt = data_filt.merge(temp_df, how='outer')

    nrows = data_filt.shape[0]

    data_filt.to_csv(args.outfile)

    print(f'Done, wrote {nrows} to "{args.outfile}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
