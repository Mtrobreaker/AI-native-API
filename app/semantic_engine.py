# app/semantic_engine.py

def generate_semantics(endpoint):

    summary = endpoint["summary"].lower()

    capability = {

        "capability_name": "",

        "purpose": "",

        "risk_level": "low",

        "side_effects": []
    }

    if "invoice" in summary:

        capability["capability_name"] = (
            "create_invoice"
        )

        capability["purpose"] = (
            "Generate customer invoice"
        )

        capability["side_effects"] = [
            "billing_record_created"
        ]

        capability["risk_level"] = "medium"

    else:

        capability["capability_name"] = (
            "unknown_capability"
        )

        capability["purpose"] = (
            "Unknown action"
        )

    return capability