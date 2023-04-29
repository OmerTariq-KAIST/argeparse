#tutorial on argparse
import argparse
import pprint
from typing import Optional
from typing import Sequence

#custom type function
def pos_int(s: str) -> int:
    try:
        v = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f'expected integer, got {s!r}')
    
    if v<=0:
        raise argparse.ArgumentTypeError(f'expected pos integer, got {v}')
    return v

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    #state arguments below
    #positional
    #parser.add_argument('filename')
    #optional
    # - shot vs long opts
    # - aliases
    # - defaults

    parser.add_argument('-c', '--config', '--jsonfile', 
                        default='config.json',
                        #required=True, 
                        help='specify the config file. (default: %(default)s)') 
    
    #custom types
    parser.add_argument(
        '--days',
        type=pos_int,
    )

    #count
    parser.add_argument(
        '-v', '--verbose', action='count', default=0
    )
    #boolean options
    parser.add_argument(
        '--force', action='store_true'
    )
    #append
    parser.add_argument(
        '--log', action='append', default=[]
    )

    #choices
    parser.add_argument(
        '--color', choices=('auto', 'always', 'never')
    )

    #sub-commands
    subparser = parser.add_subparsers(dest='command')
    subparser.required = True

    status_parser = subparser.add_parser('status', help='show status')
    status_parser.add_argument('--force', action='store_true')

    args = parser.parse_args(argv)
    pprint.pprint(vars(args))
    return 0



if __name__== '__main__':
    exit(main())
