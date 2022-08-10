"""Spreadsheet Column Printer

Purpose - The script allows the user to print to the console all the columns in
the spreadsheet. It is assumed the first row of the spreadsheet is the location of the columns.

Args - This script accepts comma separated value files (.csv) as well as excel(.xls) files

Third Party Imports - This script requires that 'pandas' be installed within the python
environment you are running the script in.

Functions - This file can be also be imported as a module and contains the following functions:

    * get_spreadsheet_columns - returns the list of column headers in the spreadsheet
    * main - the main function of the script
"""

import argparse

import pandas as pd


def get_spreadsheet_cols(file_loc, print_cols=False):
    """Gets and prints the spreadsheet's header columns

    Parameters
    -----------
    file_loc: str
        The file location of the spreadsheet
    print_cols: bool, optional
        A flag used to print the columns to the console (default is False)

    Returns
    -------
    list
        a list of strings used that are the column headers
    """

    file_data = pd.read_excel(file_loc)
    col_headers = list(file_data.columns.values)

    if print_cols:
        print('\n'.join(col_headers))

    return col_headers


def main():
    # create a parser with a description
    parser = argparse.ArgumentParser(description=__doc__)
    # add arguments to the parser
    parser.add_argument(
        'input_file',
        type=str,
        help='The location of the spreadsheet file to print the columns of'
    )
    # parse the arguments added
    args = parser.parse_args()
    column_list = get_spreadsheet_cols(args.input_file, print_cols=False)
    print(column_list)


if __name__ == "__main__":
    main()
