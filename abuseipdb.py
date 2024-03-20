"""KYE: IPInfo.io Module"""

import logging
import requests

import conf


logger = logging.getLogger(__name__)

def request(endpoint, headers, query):
    """Performs requests to API endpoint"""
    logger.debug("Performing API call to AbuseIPDB")
    response = requests.request(
        method="GET", url=endpoint, headers=headers, params=query, timeout=30
    )
    if response.status_code == 200:
        logger.debug("Data successfully retrieved from AbuseIPDB")
        return response.json()
    else:
        logger.error(
            "Error occurred when attempting to request intelligence from AbuseIPDB"
            "Returned error code %s",
            response.status_code,
        )
        return None


def format_data(re):
    """Formats data in a human-readable format"""
    re = re["data"]
    if re is None:
        return ""

    logger.info("AbuseIPDB: %s", re)
    return f"""
    AbuseIPDB Data
        Allowlisted: {re["isWhitelisted"]}
        Tor Node: {re["isTor"]}
        Total Reports: {re["totalReports"]}
        Last Report: {re["lastReportedAt"]}
        Abuse Confidence: {re["abuseConfidenceScore"]}%
        """


def analyse(entity):
    """Retrieves configuration, and initiates analysis"""
    logger.info("AbuseIPDB module has been launched.")

    # Retrieve config and build request
    config = conf.read_config(__name__)
    endpoint = config["API"]["endpoint"]
    headers = {"Accept": "application/json", "Key": config["API"]["key"]}
    query = {"ipAddress": entity, "maxAgeInDays": "90"}

    return format_data(request(endpoint, headers, query))
