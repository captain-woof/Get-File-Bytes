# Get-File-Bytes

### Introduction
Reads a binary file and outputs each byte in either hex or int form with any chosen prepending and appending string.

### Usage and Arguments
```
usage: getFileBytes.py [-h] -f FILE [-p PREPEND] [-a APPEND] [-t {int,hex}]
                       [-o OUTPUT]
optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File to read bytes from
  -p PREPEND, --prepend PREPEND
                        String to prepend to each byte in output; default:
                        '\x'
  -a APPEND, --append APPEND
                        String to append to each byte in output; default: None
  -t {int,hex}, --format {int,hex}
                        Output representation of each byte; default: 'hex'
  -o OUTPUT, --output OUTPUT
                        File to output results to
```

### Author

[CaptainWoof](https://twitter.com/realCaptainWoof)
