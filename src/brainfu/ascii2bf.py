#!/usr/bin/env python3

# Copyright (C) 2020, Vi Grey
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY AUTHOR AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

import sys

help_flag = False
filepath = ""

def get_args():
    global help_flag, filepath
    if len(sys.argv) >= 2:
        i = 0
        for a in sys.argv[1:]:
            if a.upper() == "--HELP" or a.upper() == "-H":
                help_flag = True
            elif i == len(sys.argv[1:]) - 1:
                filepath = a
            i += 1

def print_help():
    help_string = ("Usage: python3 ascii2bf.py [ OPTIONS ] [ " +
        "input_file ]\r\n\r\n" +
        "Prints a brainfu-- program that prints out the contents of " +
        "input_file\r\n\r\n" +
        "Options:\r\n"
        "  -h, --help  Print Help (this message) and exit\r\n\r\n"
        "Example:\r\n" +
        "  python3 ascii2bf.py --help\r\n" +
        "  python3 ascii2bf.py -h\r\n" +
        "  python3 ascii2bf.py test.txt")
    print(help_string)

def print_bf():
    global filepath
    if filepath == "":
        print("\x1b[91mInput File Required. Use --help argument to learn more.\x1b[0m")
        exit(1)
    ascii_file = open(filepath, "rb")
    filecontent = ascii_file.read()
    ascii_file.close()
    uniquecount = {}
    unique = []
    for letter in filecontent:
        if letter not in unique:
            uniquecount[letter] = 1
        uniquecount[letter] += 1
        unique = sorted(uniquecount, key = uniquecount.get, reverse = True)
    setup = ">++[-<+>>++<]>[-<+>>++<]>[-<+>>++<]>[-<+>>++<]>[-<+>>++<]>[-<+>>++<]>[-<+>>++<]>[-]<"
    leftarrow = 1
    for i in range(8):
        if i != 7:
            setup += "<[-"
            setup += ">" * i
        else:
            setup += ">" * (i - 1)
        leftarrow = 0
        for item in unique:
            binaryitem = format(item, '#010b')[2:]
            setup += ">"
            if binaryitem[i] == "1":
                setup += "+"
            leftarrow += 1
        setup += "<" * leftarrow
        if i != 7:
            setup += "<" * i
            setup += "]"
            setup + ">" * i
        else:
           setup += ">"
    oldindex = 0
    for letter in filecontent:
        letterindex = unique.index(letter)
        right = letterindex - oldindex
        oldindex = letterindex
        if right > 0:
            setup += ">" * right
        else:
            setup += "<" * -right
        setup += "."
    while "<>" in setup:
        setup = setup.replace("<>", "")
    while "><" in setup:
        setup = setup.replace("><", "")
    print(setup)


get_args()
if help_flag:
    print_help()
else:
    print_bf()
