# Dominik Molenda
# zadania 1-3
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--lines',
                    default=[10],
                    type=int,
                    nargs=1,
                    help='Number of lines to show.')

parser.add_argument('file',
                    type=str,
                    help='File which should be displayed.')
parser.add_argument('-v', '--verbose',
                    action='store_true',
                    default=False,
                    help='Explain what is done.')

args = parser.parse_args()

if args.verbose:
    print(f'Program is running with name {sys.argv[0]}')
    print(
        f'It will print {args.lines[0]} lines from {args.file} and terminate.')
    print('='*50)

if sys.argv[0] == "head.py":
    try:
        with open(args.file) as f:
            for i in range(args.lines[0]):
                print(f.readline().strip())
    except:
        print("File not found")
elif sys.argv[0] == "tail.py":
    try:
        with open(args.file) as f:
            lines = f.readlines()[-args.lines[0]:]
            for line in lines:
                print(line.strip())
    except:
        print("File not found")
if args.verbose:
    print('='*50)
