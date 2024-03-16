import argparse

def parse_args():
    # Define the argument parser
    parser = argparse.ArgumentParser(
        prog='knowyourentity.py',
        description='An OSINT federated information retrieval framework.',
        epilog='Developed by Enrico Renna. Licenced under GPLv3.0.'
    )

    # Provide the viable arguments
    parser.add_argument('entity', 
                        type=str, 
                        help='The entity to be analysed.')
    parser.add_argument('-v', '--verbose', 
                        type=int, 
                        choices=range(1, 5),
                        default=1, 
                        help="The level of verbosity of the script. Default is 1.")

    # Parse and return arguments
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args() # Retrieve arguments