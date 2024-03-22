"""KYE: ThreatFox Module"""

import logging

import conf
import req


logger = logging.getLogger(__name__)


def format_data(re):
    """Formats data in a human-readable format"""
    if re is None:
        return ""
    print(re)
    data = """
    ThreatFox Data"
        IoC: """

    if re["query_status"] == "ok":
        re = re["data"][0]
        data += f"""{re["threat_type"]}
        Malware: {re["malware_printable"]}
        First seen: {re["first_seen"]}
        """
    else:
        data += "No indicators of compromise"

    return data


def analyse(entity):
    """Retrieves configuration, and initiates analysis"""
    logger.info("ThreatFox module has been launched.")

    # Retrieve config
    config = conf.read_config(__name__)
    module = config["Module"]["name"]
    endpoint = config["API"]["endpoint"]

    data = {"query": "search_ioc", "search_term": entity}

    url = f"{endpoint}"
    return format_data(
        req.request(module, url, method="POST", json=data).json()
    )
