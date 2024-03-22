"""KYE: IPQualityScore Module"""

import logging

import pycountry

import conf
import req


logger = logging.getLogger(__name__)

def format_data(re):
    """Formats data in a human-readable format"""
    if re is None:
        return ""

    return f"""
    IPQualityScore Data
        City: {re["city"]}
        Region: {re["region"]}
        Country: {pycountry.countries.get(alpha_2=re["country_code"]).name}
        Organisation: AS{re["ASN"]} {re["ISP"]}
        Fraud Score: {re["fraud_score"]}
        Mobile: {re["mobile"]}
        Crawler: {re["is_crawler"]}
        Proxy: {re["proxy"]}
        VPN: {re["vpn"]}
        TOR Node: {re["tor"]}
        Bot: {re["bot_status"]}
        Recent abuse: {re["recent_abuse"]}
        Hostname: {re["host"]}
        """

def analyse(entity):
    """Retrieves configuration, and initiates analysis"""
    logger.info("IPQualityScore module has been launched.")

    # Retrieve config
    config = conf.read_config(__name__)
    module = config["Module"]["name"]
    endpoint = config["API"]["endpoint"]
    key = config["API"]["key"]
    options = config["API"]["options"]

    url = f"{endpoint}{key}/{entity}{options}"
    return format_data(req.request(module, url).json())
