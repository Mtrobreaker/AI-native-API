# app/main.py

from parser import load_openapi_file

from extractor import extract_endpoints

from semantic_engine import generate_semantics

from schema_generator import save_capabilities


print(
    "Agent Capability Generator Started!"
)

openapi_data = load_openapi_file(
    "samples/swagger.json"
)

endpoints = extract_endpoints(
    openapi_data
)

all_capabilities = []

for endpoint in endpoints:

    capability = generate_semantics(
        endpoint
    )

    all_capabilities.append(capability)

save_capabilities(all_capabilities)

print(
    "Capability schema generated!"
)