"""KYE: LLM Integration"""

import logging

import conf
import req

logger = logging.getLogger(__name__)

def generate(entity, intelligence):
    """Generate summary based on input and prompt"""
    config = conf.read_config(__name__)
    module = config["Module"]["name"]
    endpoint = config["API"]["endpoint"]
    key = f"""Bearer {config["API"]["key"]}"""
    model = config["API"]["model"]
    prompt = (
        config["API"]["prompt"].replace("(IP)", entity) + "\n" + intelligence
    )

    headers = {
        "Authorization": key,
        "Content-Type": "application/json",
    }

    data = {
        "model": model,
        "prompt": prompt,
        "temperature": 0.2,
        "max_tokens": 200,
    }

    response = req.request(
        module, endpoint, method="POST", headers=headers, json=data
    ).json()
    logger.warning("The below summary is AI generated. LLMs can make mistakes. Please verify the information with the output file.")
    print(
        response["choices"][0]["text"]
    )  # or do whatever you need with the response
