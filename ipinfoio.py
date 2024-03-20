"""KYE: IPInfo.io Module"""

import logging
import requests

import pycountry

import conf


logger = logging.getLogger(__name__)


def request(url):
    """Performs requests to API endpoint"""
    logger.debug("Performing API call to IPInfo.io")
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        logger.debug("Data successfully retrieved from IPInfo.io")
        return response.json()
    else:
        logger.error(
            "Error occurred when attempting to request intelligence from IPInfo.io."\
            "Returned error code %s", response.status_code
            )
        return None


def format_data(re):
    """Formats data in a human-readable format"""
    if re is None:
        return ""

    logger.info("IPInfo.io: %s", re)
    return f"""
    IPInfo.io Data
        Hostname: {re["hostname"]}
        City: {re["city"]}
        Region: {re["region"]}
        Country: {pycountry.countries.get(alpha_2=re["country"]).name}
        Organisation: {re["org"]}
        """

def analyse(entity):
    """Retrieves configuration, and initiates analysis"""
    logger.info("IPInfo.io module has been launched.")

    # Retrieve config
    config = conf.read_config(__name__)
    endpoint = config["API"]["endpoint"]
    key = config["API"]["key"]

    uri = "/json?token="
    url = f"{endpoint}{entity}{uri}{key}"
    return format_data(request(url))
