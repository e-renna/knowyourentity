"""KYE: Requests library"""

import logging
import requests

logger = logging.getLogger(__name__)


def request(module, endpoint, headers=None, query=None, auth=None):
    """Performs requests to API endpoint"""
    logger.debug("Performing API call to %s", module)
    response = requests.request(
        method="GET",
        url=endpoint,
        headers=headers,
        params=query,
        auth=auth,
        timeout=30
    )
    if response.status_code == 200:
        logger.debug("Data successfully retrieved from %s", module)
        logger.info("%s: %s", module, response.content)
        return response
    else:
        logger.error(
            "Error occurred when attempting to request intelligence from %s"
            "Returned error code %s",
            module,
            response.status_code,
        )
        return None
