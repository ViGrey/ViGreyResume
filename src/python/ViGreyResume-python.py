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

bf_flag = False
help_flag = False
filepath = ""

# Get name of the python script (this script)
script_name = sys.argv[0]
script_name.replace("\\", "/")
script_name = script_name.split("/")[-1]

def get_args():
    global bf_flag, help_flag, filepath
    if len(sys.argv) >= 2:
        i = 0
        for a in sys.argv[1:]:
            if a.upper() == "--HELP" or a.upper() == "-H":
                help_flag = True
            elif a.upper() == "--BF" or a.upper() == "-B":
                # Only set bf_flag if not the last argument
                if i < len(sys.argv[1:]) - 1:
                    bf_flag = True
                    # Set bf file path to argument after bf flag
                    filepath = sys.argv[1:][i + 1]
            i += 1

def print_help():
    help_string = ("Usage: python3 " + script_name + " [ OPTIONS ] \r\n\r\n" +
        "Prints an ASCII version of the resume if no options are provided\r\n\r\n"
        "Options:\r\n" +
        "  -b, --bf BF_FILE_PATH   Interpret BF_FILE_PATH as a Brainfu-- " +
        "Program\r\n" +
        "  -h, --help              Print Help (this message) and exit\r\n\r\n" +
        "Examples:\r\n" +
        "  python3 " + script_name + "\r\n" +
        "  python3 " + script_name + " --bf " + script_name + "\r\n" +
        "  python3 " + script_name + " -b " + script_name + "\r\n" +
        "  python3 " + script_name + " --help\r\n" +
        "  python3 " + script_name + " -h")
    print(help_string)

def interpret_bf():
    global filepath
    print("\x1b[92m\x1b[1mInterpreting Brainfu-- File\x1b[0m")

    bf_file = open(filepath, "rb")
    instructions = bf_file.read().decode("latin1")
    bf_file.close()

    memory = [0] * 30000  # Set Brainfu-- Memory Tape Size to 30000
    memptr = 0    # Set Brainfu-- Memory Pointer to Offset 0
    instptr = 0   # Set Brainfu-- Instruction Pointer to Offset 0

    # Loop until brainfu-- file finished being interpreted
    while True:
        inst = instructions[instptr]
        if inst == "+":
            # Increment memory cell by 1 (8-bit uint wrap)
            memory[memptr] += 1
            if memory[memptr] == 256:
                memory[memptr] = 0
        elif inst == "-":
            # Decrement memory cell by 1 (8-bit uint wrap)
            memory[memptr] -= 1
            if memory[memptr] == -1:
                memory[memptr] = 255
        elif inst == "<":
            # Move memory tape pointer offset to left by 1 if not 0
            if memptr > 0:
                memptr -= 1
            else:
                print("\x1b[91mMemory Pointer out of bounds (-1)\x1b[0m")
                exit(1)
        elif inst == ">":
            # Move memory tape pointer offset to left by 1 if not 29999
            if memptr < 29999:
                memptr += 1
            else:
                print("\x1b[91mMemory Pointer out of bounds (30000)\x1b[0m")
                exit(1)
        elif inst == ".":
            # Print single byte in current memory cell as ASCII value
            sys.stdout.write(chr(memory[memptr]))
        elif inst == ",":
            # Take first byte of user input and store it in current memory cell
            if (sys.version_info > (3, 0)):
                memory[memptr] = input().encode("utf8")[0]
            else:
                memory[memptr] = ord(raw_input()[0])
        elif inst == "]":
            squares = 0   # Set Square Bracket Balance to 0
            # Move instruction pointer to the left until the matching
            # [ instruction is found
            while True:
                # Move instruction pointer to the left by 1
                instptr -= 1
                if instptr < 0:
                    # Produce error if out of instruction pointer range
                    print("\x1b[91mNo Matching [ for ] instruction\x1b[0m")
                    exit(1)
                inst = instructions[instptr]
                if inst == "]":
                    # Add 1 to `squares` if instruction is a ]
                    # This is used to find matching square brackets
                    squares += 1
                elif inst == "[":
                    if squares != 0:
                        # Subtract 1 to `squares` if instruction is a [
                        # This is used to find matching square brackets
                        squares -= 1
                    else:
                        # If `squares` is 0, the matching [ has been found  
                        # Move instruction pointer left 1 so the [ instruction
                        # can be interpreted
                        instptr -= 1
                        break
        elif inst == "[":
            # Check if current memory cell value is 0
            # If memory cell value is 0, ignore the [ instruction
            if memory[memptr] == 0:
                squares = 0   # Set Square Bracket Balance to 0
                # Move instruction pointer to the right until the matching
                # ] instruction is found
                while True:
                    # Move instruction pointer to the right by 1
                    instptr += 1
                    if instptr == len(instructions):
                        # Produce error if out of instruction pointer range
                        print("\x1b[91mNo Matching ] for [ instruction\x1b[0m")
                        exit(1)
                    inst = instructions[instptr]
                    if inst == "[":
                        # Add 1 to `squares` if instruction is a [
                        # This is used to find matching square brackets
                        squares += 1
                    elif inst == "]":
                        if squares != 0:
                            # Subtract 1 to `squares` if instruction is a ]
                            # This is used to find matching square brackets
                            squares -= 1
                        else:
                            # If `squares` is 0, the matching ] has been found  
                            break
        # Move instruction pointer to the right by 1
        instptr += 1
        if instptr == len(instructions):
            # End interpreting when at the end of instructions
            break
    print("")
    print("\x1b[92m\x1b[1mFinished Interpreting Brainfu-- File\x1b[0m")

# Resume ASCII Data
resume_data = """\x1b[1mVi Grey\x1b[0m
vigrey.com | vi@vigrey.com | github.com/ViGrey

\x1b[1mLANGUAGES AND TECHNOLOGIES\x1b[0m
  * Go, Python, PHP, 6502 ASM, Z80 ASM, Bash, Javascript, HTML, CSS, JSON, XML, Brainfu--
  * Linux, Unix, Windows, CentOS, RHEL, AWS, Unix Permissions, Cron, AngularJS, Node.js, TCP/IP, HTTP, TLS, SSL, SQL, MongoDB, MySQL, LaTeX 

\x1b[1mWORK EXPERIENCE
  2014 - Present - \x1b[1mSoftware Engineer, Technology Researcher, & Speaker\x1b[0m
  VG Interactive (Independent) - Rochester, MN/New York, NY
  *Created a research lab to actively develop skills and knowledge in modern and historical technology
  *Writes and speaks about technology, security, and information theory 

  2018 - 2019 (Contract) - \x1b[1mConference Name Badge Developer\x1b[0m
  Midwest Gaming Classic - Milwaukee, WI
  * Created first name badge for a gaming conference that is a playable game cartridge
  * Developed new NES game "Bovinium Quest - Batteries Not Included" from scratch in 6502 Assembly
  * Programmed, assembled, and soldered over 600 cartridges by hand
  * Created score code system that lets players submit their high scores to an online leaderboard 

  2015 - \x1b[1mSoftware Engineer & Information Security Engineer\x1b[0m
  Excel Manufacturing - St. Charles, MN
  *Developed sales and support ticket management application to improve sales and support team productivity
  * Encrypted database information and hashed passwords with bcrypt to protect data in case of a data breach
  * Set up AWS virtual servers to test application deployment before running those applications in production environment 

  2015 (Contract) - \x1b[1mWeb Developer\x1b[0m
  Toymaker Television (Tymkrs) - Rochester, MN
  * Created a website design for desktop with the security requirements of needing to be static and easily maintainable
  * Optimized original website design to reduce loading times by more than 75% and allow for dynamic content size 

  2011 - 2013 - \x1b[1mSystem Administrator & Web Developer\x1b[0m
  Jon Hassler Theater - Plainview, MN
  * Created a web-based box office ticket reservation system to improve work productivity
  * Developed and maintained website, increasing page trafic by over 800%
  * Managed computer systems and networks to keep business operations functioning 

\x1b[1mRESENTATIONS\x1b[0m
  * 2019 - \x1b[1mBet You Never Played an NES Game like This: Innovating Under Limitations\x1b[0m - Cyphercon 4.0 - Milwaukee, WI 
  * 2018 - \x1b[1mI Dream of Game Genies and ZIP Files - Hacking the NES\x1b[0m - HOPE Conference - Manhattan, NY
  * 2017 - \x1b[1mPhishing for Root - DEFCON 201 Technical Meeting\x1b[0m - Hoboken, NJ
  * 2017 - \x1b[1mFair Results From an Unfair Coin\x1b[0m - NYC Python Lightning Talks - Manhattan, NY
  * 2017 - \x1b[1mAttacking Your Two-Factor Authentication\x1b[0m - K-LUG Technical Meeting - Rochester, MN

\x1b[1mPROJECTS\x1b[0m
  2020 - \x1b[1mThis Resume\x1b[0m
  * See Footnotes [1] [2] [3] [4]

  2019 - \x1b[1mGB/NES/PDF/HTML/ZIP Polyglot File\x1b[0m
  * Gameboy ROM that is also a functioning NES ROM, HTML file, PDF file, and ZIP file that contains the file's full source code 

  2018 - \x1b[1mBrainfu-- Programming Language Interpreter on NES Cartridge\x1b[0m
  * Interpreter for the Brainfu-- programming language that can be played on an NES using a standard NES controller

  2018 - \x1b[1mNESZIP\x1b[0m
  * Proof of concept tool that makes an NES ROM that is also a ZIP file that contains a copy of its own source code 

  2017 - \x1b[1m3F.py\x1b[0m
  * Python script that takes 2 different types of files and creates a file that is simultaneously a functioning version of both files 

  2017 - \x1b[1mModem-Tap\x1b[0m
  * Middleware audio engine written in Go that emulates a network connection though a Bell103 dial-up modem 

  2017 - \x1b[1mPersonal BBS\x1b[0m
  * Online Bulletin Board Service written in Go - telnet vigrey.com 

  2017 - \x1b[1mRoot Phisher\x1b[0m
  * Proof of concept Bash script that pretends to be the sudo password prompt and deletes traces of itself 

  2015 - \x1b[1mignis\x1b[0m
  * Scripting and templating engine written in Python for generating static websites 

  2014 - \x1b[1mLatchbox\x1b[0m
  * Password manager written in Go that uses a console based user interface 

  2013 - \x1b[1mrcube\x1b[0m
  * Python module that solves scrambled Rubik's Cubes 

  2012 - \x1b[1mdatecalc\x1b[0m
  * Python module that can calculate the day of the week for any date (Ported to Go, Ruby, and Javascript) 

\x1b[1mCOMMUNITY WORKSHOP MEMBERSHIPS\x1b[0m
  * 2018 - Present - \x1b[1mDEFCON 212\x1b[0m - Makerspace - New York, NY
  * 2017 - Present - \x1b[1mDEFCON 201\x1b[0m - Makerspace - Hoboken, NJ/Jersey City, NJ
  * 2013 - Present - \x1b[1mThe Rabbit Hole\x1b[0m (Operated by the Tymkrs) - Makerspace - Rochester, MN
  * 2016 - 2017 - \x1b[1mK-LUG\x1b[0m - Linux User Group - Rochester, MN

\x1b[1mPUBLICATIONS\x1b[0m
  * 2018 - \x1b[1mConcealing ZIP Files in NES Cartridges\x1b[0m - Proof of Concept or GTFO Issue 0x18, 4, pp 17-21

----------------
[1] This Python file is also a valid Brainfu-- file that prints this resume in ASCII
[2] This Python file is also a Brainfu-- interpreter - \x1b[1mpython3 """ + script_name + " --bf " + script_name + """\x1b[0m
[3] This Python file is also a valid PDF file version of this resume
[4] This Python file is also a valid static HTML file version of this resume - Rename \x1b[1m""" + script_name + """\x1b[0m to \x1b[1mViGreyResume.pdf\x1b[0m and open it in a PDF viewer
[5] The source code for this resume can be found at https://github.com/ViGrey/ViGreyResume or by unzipping this file, which is also a valid ZIP file"""


get_args()
if help_flag:
    print_help()
elif bf_flag:
    interpret_bf()
else:
    print(resume_data.replace("\n", "\r\n"))
