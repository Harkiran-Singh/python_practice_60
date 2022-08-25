import argparse

"""
The script finds sum of command-line arguments using argparse module
"""
# Initialize the Parser
parser = argparse.ArgumentParser(description='Process some integers.')

# Adding Arguments
parser.add_argument('integers', metavar='N',
                    type=int,
                    nargs='+',
                    help='an integer for the accumulator'
                    )

parser.add_argument(dest='accumulate',
                    action='store_const',
                    const=sum,
                    help='sum of integers'
                    )

parser.add_argument('sum',
                    action='store_const',
                    const=sum
                    )

parser.add_argument('len',
                    action='store_const',
                    const=len
                    )
args = parser.parse_args()
add = args.sum(args.integers)
length = args.len(args.integers)
average = add / length
print(args.accumulate(args.integers))
print(average)


