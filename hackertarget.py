"""KYE: Hacker Target Module"""

import logging

import conf
import req


logger = logging.getLogger(__name__)


def format_data(re):
    """Formats data in a human-readable format"""
    re = re.decode("utf-8").strip('"').split('","')
    if re is None or len(re) < 4:
        return ""

    data = f"""
    Hacker Target Data:
        Organisation: AS{re[1]} {re[3]}
        """
    return data


def analyse(entity):
    """Retrieves configuration, and initiates analysis"""
    logger.info("Hacker Target module has been launched.")

    # Retrieve config
    config = conf.read_config(__name__)
    module = config["Module"]["name"]
    endpoint = config["API"]["endpoint"]

    url = f"{endpoint}{entity}"
    return format_data(req.request(module, url).content)
