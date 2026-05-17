# app/schema_generator.py

import json


def save_capabilities(capabilities):

    with open(
        "output/capabilities.json",
        "w"
    ) as file:

        json.dump(
            capabilities,
            file,
            indent=4
        )