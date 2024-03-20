"""KYE: IPInfo.io Module"""

import logging

import pycountry

import conf
import req


logger = logging.getLogger(__name__)

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
    module = config["Module"]["name"]
    endpoint = config["API"]["endpoint"]
    key = config["API"]["key"]

    uri = "/json?token="
    url = f"{endpoint}{entity}{uri}{key}"
    return format_data(req.request(module, url).json())
