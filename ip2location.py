"""KYE: IP2Location Module"""

import logging

import pycountry

import conf
import req


logger = logging.getLogger(__name__)

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
    config = conf.read_config(__name__)
    module = config["Module"]["name"]
    endpoint = config["API"]["endpoint"]
    key = config["API"]["key"]

    param1 = "?key="
    param2 = "&ip="
    url = f"{endpoint}{param1}{key}{param2}{entity}"
    return format_data(req.request(module, url).json())
