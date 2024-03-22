"""KYE: AbuseIPDB Module"""

import logging

import conf
import req


logger = logging.getLogger(__name__)


def format_data(re):
    """Formats data in a human-readable format"""
    re = re["data"]
    if re is None:
        return ""

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
    module = config["Module"]["name"]
    endpoint = config["API"]["endpoint"]
    headers = {"Accept": "application/json", "Key": config["API"]["key"]}
    query = {"ipAddress": entity, "maxAgeInDays": "90"}

    return format_data(req.request(module, endpoint, headers, query).json())
