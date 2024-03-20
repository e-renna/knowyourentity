"""KYE: IPInfo.io Module"""

import logging
import requests

import conf


logger = logging.getLogger(__name__)

def request(endpoint):
    """Performs requests to API endpoint"""
    logger.debug("Performing API call to FeodoTracker")
    response = requests.request(
        method="GET", url=endpoint, timeout=30
    )
    if response.status_code == 200:
        logger.debug("Data successfully retrieved from FeodoTracker")
        return response
    else:
        logger.error(
            "Error occurred when attempting to request intelligence from FeodoTracker"
            "Returned error code %s",
            response.status_code,
        )
        return None


def format_data(re, entity):
    """Formats data in a human-readable format"""
    re = str(re.content)
    if entity in re:
        return """
    Feodo Tracker Data:
        C&C or Botnet: true
    """

    return """
    Feodo Tracker Data:
        C&C or Botnet: false
    """


def analyse(entity):
    """Retrieves configuration, and initiates analysis"""
    logger.info("FeodoTracker module has been launched.")

    # Retrieve config and build request
    config = conf.read_config(__name__)
    endpoint = config["API"]["endpoint"]

    return format_data(request(endpoint), entity)
