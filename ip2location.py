"""KYE: IPInfo.io Module"""

import logging
import requests

import pycountry

import conf


logger = logging.getLogger(__name__)


def settings():
    """Import IP2Location settings from config file."""
    logger.debug("Reading IP2Location configuration file.")
    config = conf.read_config(__name__)
    logger.debug("IP2Location module configuration has been imported.")
    return config


def request(url):
    """Performs requests to API endpoint"""
    logger.debug("Performing API call to IP2Location.io")
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        logger.debug("Data successfully retrieved from IP2Location.io")
        return response.json()
    else:
        logger.error(
            "Error occurred when attempting to request intelligence from IP2Location.io."\
            "Returned error code %s", response.status_code
            )
        return None


def format_data(re):
    """Formats data in a human-readable format"""
    if re is None:
        return ""

    logger.info("IP2Location.io: %s", re)
    return f"""
    IP2Location.io Data
        City: {re["city_name"]}
        Region: {re["region_name"]}
        Country: {pycountry.countries.get(alpha_2=re["country_code"]).name}
        Organisation: AS{re["asn"]} {re["as"]}
        """

def analyse(entity):
    """Retrieves configuration, and initiates analysis"""
    logger.info("IP2Location.io module has been launched.")

    # Retrieve config
    config = settings()
    endpoint = config["API"]["endpoint"]
    key = config["API"]["key"]

    param1 = "?key="
    param2 = "&ip="
    url = f"{endpoint}{param1}{key}{param2}{entity}"
    return format_data(request(url))
