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
input_filepath = ""
output_filepath = ""

def get_args():
    global help_flag, input_filepath, output_filepath
    if len(sys.argv) >= 2:
        i = 0
        for a in sys.argv[1:]:
            if a.upper() == "--HELP" or a.upper() == "-H":
                help_flag = True
            elif i == len(sys.argv[1:]) - 2:
                input_filepath = a
            elif i == len(sys.argv[1:]) - 1:
                output_filepath = a
            i += 1

def print_help():
    help_string = ("Usage: python3 bfcomment.py [ OPTIONS ] [ " +
        "input_file ] [ output_file ]\r\n\r\n" +
        "Saves input_file with matched square brackets to " +
        "output_file\r\n\r\n" +
        "Options:\r\n"
        "  -h, --help  Print Help (this message) and exit\r\n\r\n"
        "Example:\r\n" +
        "  python3 bfcomment.py --help\r\n" +
        "  python3 bfcomment.py -h\r\n" +
        "  python3 bfcomment.py input.txt output.txt")
    print(help_string)

def comment_file():
    global input_filepath, output_filepath
    if input_filepath == "":
        print("\x1b[91mInput File Required. Use --help argument to learn more.\x1b[0m")
        exit(1)
    if output_filepath == "":
        print("\x1b[91mOutput File Required. Use --help argument to learn more.\x1b[0m")
        exit(1)
    unmatched_right = 0
    unmatched_left = 0
    text_file = open(input_filepath, "rb")
    characters = text_file.read().decode("latin1")
    text_file.close()
    for c in characters:
        if c == "[":
            unmatched_right += 1
        elif c == "]":
            if unmatched_right == 0:
                unmatched_left += 1
            else:
                unmatched_right -= 1
    characters_bin = characters.encode("latin1")
    characters_bin = (b"[" * unmatched_left) + characters_bin
    characters_bin += b"]" * (unmatched_right + 1)
    characters_bin = b"[-][" + characters_bin
    output_text_file = open(output_filepath, "wb")
    output_text_file.write(characters_bin)
    output_text_file.close()


get_args()
if help_flag:
    print_help()
else:
    comment_file()
