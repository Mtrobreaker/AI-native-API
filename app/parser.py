# app/parser.py

import json


def load_openapi_file(file_path):

    with open(file_path, "r") as file:

        data = json.load(file)

    return data