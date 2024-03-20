"""KYE: IPInfo.io Module"""

import logging

import conf
import req


logger = logging.getLogger(__name__)

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
    module = config["Module"]["name"]
    endpoint = config["API"]["endpoint"]

    return format_data(req.request(module, endpoint), entity)
