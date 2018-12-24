#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import argparse
import sys
from typing import Dict, Any


def cli_arg_parser() -> Dict[str, Any]:
    """
    Parses the arguments from CLI and returns to the dictionary
    where keys are the options/flags

    ex: when -f triggered, there'll be 'file' key in the dictionary.
    and values are accessible with list syntax `[]`

    Test when filename passed as positional argument
    >>> sys.argv = [sys.argv[0], "file name"]
    >>> cli_arg_parser()
    {'file': 'file name', 'pack': None, 'silent': False, 'out': None, 'no_log': False, 'str_gen': None}

    Test no file passed
    >>> sys.argv = [sys.argv[0], ]
    >>> cli_arg_parser()
    Traceback (most recent call last):
      ...
    SystemExit: 2
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file",
                        help="File to be obfuscated. Optional")
    parser.add_argument("-p",
                        "--pack",
                        help="Available packers: bz2, gz, lzma")
    parser.add_argument("-s",
                        "--silent",
                        action="store_true",
                        help="Just quietness")
    parser.add_argument("-o", "--out",
                        help="Destination for the output file")
    parser.add_argument("--no-log",
                        action="store_true",
                        help="Not save log file(s)")
    parser.add_argument("--str-gen",
                        help="Available string generators: jp, ch, in")
    # Return to dictionary
    args = vars(parser.parse_args())
    return args


if __name__ == "__main__":
    import doctest

    doctest.testmod()
