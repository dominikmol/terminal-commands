# Dominik Molenda
import os
import argparse

parser = argparse.ArgumentParser()
file_count = 0
dir_count = 0

def tree(path, iter=0):
    global file_count
    global dir_count
    dir = os.scandir(path)
    if iter == args.level:
        return
    if iter == 0:
        if args.path == '':
            print('.')
        else:
            print(args.path)
            
    for entry in dir:
        if args.directory:
            if not entry.is_file():
                dir_count += 1
                if iter == 0:
                    print(f'\--{entry.name}/')
                else:
                    for _ in range(iter):
                        print('   ', end='')
                    print(f'\--{entry.name}/')
                tree(entry.path, iter+1)
        else:
            if entry.is_file():
                file_count += 1
                if iter == 0:
                    print(f'|--{entry.name}')
                else:
                    for _ in range(iter):
                        print('  ', end='')
                    print(f'|--{entry.name}')
            else:
                dir_count += 1
                if iter == 0:
                    print(f'\--{entry.name}/')
                else:
                    for _ in range(iter):
                        print('   ', end='')
                    print(f'\--{entry.name}/')
                tree(entry.path, iter+1)

parser.add_argument('path',
                    default=".",
                    type=str,
                    nargs='?',
                    help='File which should be displayed.')

parser.add_argument('-d', '--directory',
                    action='store_true',
                    default=False)

parser.add_argument('-L', '--level',
                    default=-1,
                    type=int)

args = parser.parse_args()
tree(args.path)
print(f'\n{dir_count} directories, {file_count} files')