"""
Know Your Entity main script.
Handles arguments, logging and input validation
"""

import ast
import argparse
import importlib
import ipaddress
import logging
import sys

import conf
import ai_gen

logger = logging.getLogger(__name__)


def parse_args():
    """Parses the arguments provided via CLI."""

    # Define the argument parser
    parser = argparse.ArgumentParser(
        prog="knowyourentity.py",
        description="An OSINT federated information retrieval framework.",
        epilog="Developed by Enrico Renna. Licenced under GPLv3.0.",
    )

    # Provide the viable arguments
    parser.add_argument(
        "entity",
        type=str,
        help="The entity to be analysed. Currently only IP addresses are supported.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="The level of verbosity of the script. Default and recommended is INFO.",
    )

    # Parse and return arguments
    return parser.parse_args()


def log(args):
    """Configure logging for the framework"""

    # Setup logging variables
    log_file = "./logs/" + args.entity + ".log"

    # Configure logger
    logging.basicConfig(
        filename=log_file,
        encoding="utf-8",
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=args.verbose,
    )

    # Also log to stdout
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    # Begin logging
    logger.info("Know Your Entity has started.")
    logger.info("The entity to be investigated is %s.", args.entity)
    logger.info("The verbosity has been set to %s.", args.verbose)


def validate_input(entity):
    """Verify whether the input is a valid IP address"""

    try:
        address = ipaddress.ip_address(entity)
        if address.is_private:
            logger.warning(
                "The IPv%s address %s is a private address reserved for internal network "
                "use, not accessible from the internet, and typically used for "
                "communication within a local network.",
                str(address.version),
                entity,
            )
            done()
        return address.version
    except ValueError as e:
        logger.critical("The entity %s. The program will now exit.", str(e))
        done()


def done():
    """Nothing else to do, exit."""

    logger.info("\n\nAll operations have been completed. Exiting...")
    sys.exit(1)


def main():
    """Main function, calls other functions."""

    args = parse_args()  # Retrieve arguments
    log(args)
    version = validate_input(args.entity)
    config = conf.read_config("knowyourentity")
    tools = ast.literal_eval(config["Settings"]["tools"])
    if version != 4:
        ipv4_only = ast.literal_eval(config["Settings"]["ipv4_only"])
        tools = [tool for tool in tools if tool not in ipv4_only]

    intelligence = ""
    for tool in tools:
        pkg = importlib.import_module(tool)
        intelligence += pkg.analyse(args.entity)

    ai_gen.generate(args.entity, intelligence)

    f_name = "./intelligence/" + args.entity + ".txt"
    output = open(f_name, "w+", encoding="utf-8")
    output.write(intelligence)
    output.close()

    done()


if __name__ == "__main__":
    main()
