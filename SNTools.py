from tkinter import *
from tkinter.scrolledtext import ScrolledText
from argparse import ArgumentParser

from SNToolsGUI import SNToolsGUI

parser = ArgumentParser("SNTools is a tool which support Serial and Network")

def help():
    print("""
        please input:
        Serial Tool:
        python3 SNTools.py -s -b 9600 -c com3 "020100"
        Network Tool:
        python3 SNTools.py -n -h '127.0.0.1' -p 6001 "020100"
        
        GUI Tool:
        python3 SNTools.py -g
        
    """)

def SNToolsTerminal():
    parser.add_argument('-g', action='store_true', help='SNTools GUI Model')
    parser.add_argument('-s', action='store_true', help='SNTools Serial Model')
    parser.add_argument('-n', action='store_true', help='SNTools Network Model')

    parser.add_argument('-p', type=int,metavar='port',default=6001, help='Network Model`s port')
    parser.add_argument('-b', type=int, metavar='bond', default=9600, help='Serial Model`s bond rate')
    parser.add_argument('-h', type=str, metavar='port', default='127.0.0.1', help='Network Model`s host ip')
    parser.add_argument('-c', type=str, metavar='com serial', default='com1', help='Serial Model`s com')

    args = parser.parse_args()
    if args.g:


    print(args.)


if __name__ == '__main__':
    SNToolsTerminal()