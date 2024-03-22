"""KYE: Pulsedive Module"""

import logging

import conf
import req


logger = logging.getLogger(__name__)

def format_data(re):
    """Formats data in a human-readable format"""
    if "risk" not in re["results"]:
        return """
    Pulsedive Data
        IoC: No data available.
        """
    data = f"""
    Pulsedive Data
        Risk: {re["results"][0]["risk"]}
        IoC added on: {re["results"][0]["stamp_added"]}
        IoC last seen on: {re["results"][0]["stamp_seen"]}
        """
    return data

def analyse(entity):
    """Retrieves configuration, and initiates analysis"""
    logger.info("Pulsedive module has been launched.")

    # Retrieve config
    config = conf.read_config(__name__)
    module = config["Module"]["name"]
    endpoint = config["API"]["endpoint"]
    key = config["API"]["key"]

    uri = "explore.php?q=ioc%3D"
    params = "&limit=10&pretty=1&key="
    url = f"{endpoint}{uri}{entity}{params}{key}"
    return format_data(req.request(module, url).json())
