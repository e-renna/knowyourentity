"""KYE: Config library"""
import configparser

def read_config(name):
    """Dynamically reads config file of the module requesting it."""
    file = "config/" + name + ".ini"
    config = configparser.ConfigParser()
    config.read(file)
    return config
