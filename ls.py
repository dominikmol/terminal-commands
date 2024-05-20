import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('path',
                    default=".",
                    type=str,
                    nargs='?',
                    help='File which should be displayed.')

parser.add_argument('-d', '--directory',
                    action='store_true',
                    default=False)

args = parser.parse_args()

dir = os.scandir(args.path)
for entry in dir:
    if args.directory:
        if not entry.is_file():
            print(f'{entry.name}/')
    else:
        if entry.is_file():
            print(entry.name)
        else:
            print(f'{entry.name}/')
