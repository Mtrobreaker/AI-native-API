# app/extractor.py

def extract_endpoints(openapi_data):

    paths = openapi_data.get("paths", {})

    extracted = []

    for path, methods in paths.items():

        for method, details in methods.items():

            endpoint_info = {

                "path": path,

                "method": method.upper(),

                "summary": details.get(
                    "summary",
                    "No summary"
                )
            }

            extracted.append(endpoint_info)

    return extracted