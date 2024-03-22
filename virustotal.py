"""KYE: VirusTotal Module"""

import logging

import pycountry

import conf
import req


logger = logging.getLogger(__name__)


def format_data(re):
    """Formats data in a human-readable format"""
    re = re["data"]
    if re is None:
        return ""

    return f"""
    VirusTotal Data:
        Country: {pycountry.countries.get(alpha_2=re["attributes"]["country"]).name}
        Organisation: {"AS" + str(re["attributes"]["asn"])} {re["attributes"]["as_owner"]}
        Malicious: {re["attributes"]["last_analysis_stats"]["malicious"]} security vendor(s)
        Suspicious: {re["attributes"]["last_analysis_stats"]["suspicious"]} security vendor(s)
    """

def analyse(entity):
    """Retrieves configuration, and initiates analysis"""
    logger.info("VirusTotal module has been launched.")

    # Retrieve config and build request
    config = conf.read_config(__name__)
    module = config["Module"]["name"]
    endpoint = config["API"]["endpoint"] + entity
    headers = {"accept": "application/json", "x-apikey": config["API"]["key"]}

    return format_data(req.request(module, endpoint, headers).json())
