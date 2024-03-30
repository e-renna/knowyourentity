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

    data = f"""
    IPInfo.io Data
        City: {re["city"]}
        Region: {re["region"]}
        Country: {pycountry.countries.get(alpha_2=re["country"]).name}
        """
    if 'org' in re:
        data += f"""Organisation: {re["org"]}
        """
    if 'hostname' in re:
        data += f"""Hostname: {re["hostname"]}
        """
    return data

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
