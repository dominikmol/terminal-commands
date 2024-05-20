import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--delimiter',
                    default=" ",
                    type=str,
                    nargs=1,
                    help='column splitter')

parser.add_argument('-f', '--fields',
                    action='store',
                    default=False,
                    help='fields to print')

parser.add_argument('file',
                    type=str,
                    help='File which should be displayed.')

parser.add_argument('--output-delimiter',
                    type=str,
                    default=" ",
                    help='operate columns with specific string on print')

args = parser.parse_args()
for line in open(args.file):
    if isinstance(args.delimiter, list):
        args.delimiter = args.delimiter[0]
    line = line.strip().split(args.delimiter)
    if args.fields == False:
        for i in range(len(line)):
            if i == len(line) - 1:
                print(line[i])
            else:
                print(line[i], end=args.output_delimiter)
    else:
        fields = args.fields.split(',')
        if len(fields) == 1:
            print(line[int(fields[0])-1])
        else:
            for i in range(len(fields)):
                f = int(fields[i])
                if int(f)-1 >= len(line):
                    if i == len(fields)-1:
                        print()
                    else:
                        continue
                if i == len(fields)-1:
                    print(line[f-1])
                else:
                    print(line[f-1], end=args.output_delimiter)
