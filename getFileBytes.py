#!/usr/bin/python3

from argparse import ArgumentParser

# Reads bytes from file
def parseBytes(filePath):
    for each_line in open(filePath,'rb'):
        for each_byte in each_line:
            yield each_byte

# Parse args
parser = ArgumentParser(description="Reads a binary file and outputs each byte in either hex or int form with any chosen prepending and appending string",epilog="Written by CaptainWoof")
parser.add_argument("-f","--file",required=True,type=str,action='store',help="File to read bytes from")
parser.add_argument("-p","--prepend",required=False,type=str,action='store',default="\\x",help="String to prepend to each byte in output; default: '\\x'")
parser.add_argument("-a","--append",required=False,type=str,action='store',default="",help="String to append to each byte in output; default: None")
parser.add_argument('-t',"--format",required=False,type=str,action='store',choices=['int','hex'],default='hex',help="Output representation of each byte; default: 'hex'")
parser.add_argument("-o","--output",required=False,type=str,action='store',help="File to output results to")
args = parser.parse_args()

# Initial setup
byteStream = parseBytes(args.file)
template = "{0}{1}{2}".format(args.prepend,r"{}" if args.format == 'int' else r"{:02x}",args.append)
outputFile = None if args.output is None else open(args.output,'w+')

# Read and output bytes
try:    
    while True:
        nextByte = template.format(next(byteStream))
        print(nextByte,end="")
        if outputFile is not None:
            outputFile.write(nextByte)
except StopIteration:
    pass
finally:
    if outputFile is not None:
        outputFile.close()
    print("")
