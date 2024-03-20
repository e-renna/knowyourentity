"""KYE: Config library"""
import configparser
import logging

logger = logging.getLogger(__name__)

def read_config(name):
    """Dynamically reads config file of the module requesting it."""
    file = "config/" + name + ".ini"
    logger.debug("Attempting to load %s configuration file.", file)
    config = configparser.ConfigParser()
    config.read(file)
    logger.debug("The configuration file for %s has been "\
                 "successfully loaded.", config["Module"]["name"])
    return config
