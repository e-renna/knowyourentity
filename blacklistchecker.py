"""KYE: Blacklist Checker Module"""

import logging

import conf
import req


logger = logging.getLogger(__name__)


def format_data(re):
    """Formats data in a human-readable format"""
    if re is None:
        return ""

    return f"""
    Blacklist Checker Data:
        Listed by: {re["detections"]} blocklist(s)
        """


def analyse(entity):
    """Retrieves configuration, and initiates analysis"""
    logger.info("Blacklist Checker module has been launched.")

    # Retrieve config
    config = conf.read_config(__name__)
    module = config["Module"]["name"]
    endpoint = config["API"]["endpoint"]
    key = config["API"]["key"]

    url = f"{endpoint}{entity}"
    auth = (key, "")
    return format_data(req.request(module, url, auth=auth).json())
