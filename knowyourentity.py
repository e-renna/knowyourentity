import argparse
import ipaddress
import logging
import sys

logger = logging.getLogger(__name__)

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
                        help='The entity to be analysed. Currently only IP addresses are supported.')
    parser.add_argument('-v', '--verbose', 
                        type=str, 
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        default='INFO', 
                        help='The level of verbosity of the script. Default and recommended is INFO.')

    # Parse and return arguments
    return parser.parse_args()

def log(args):
    # Setup logging variables
    log_file = './logs/' + args.entity + '.log'

    # Configure logger
    logging.basicConfig(filename=log_file,
                        encoding='utf-8',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=args.verbose)
    
    # Also log to stdout
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    
    # Begin logging
    logger.info('Know Your Entity has started.')
    logger.info('The entity to be investigated is ' + args.entity + '.')
    logger.info('The verbosity has been set to ' + args.verbose + '.')

def validate_input(entity):
    try:
        address = ipaddress.ip_address(entity)
    except (ValueError) as e:
        logger.critical('The entity ' + str(e) + '. The program will now exit.')


def main():
    args = parse_args() # Retrieve arguments
    log(args)
    validate_input(args.entity)
    logger.info('All operations have been completed. Exiting...')

if __name__ == '__main__':
    main()