"""KYE: LLM Integration"""

import conf
import req


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
    #print(prompt)

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
    #print(response)
    print(
        response["choices"][0]["text"]
    )  # or do whatever you need with the response
