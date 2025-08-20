import re

email_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9]\.[A-Za-z]{2,}$")

def validate_form(data):
    errors = {}

    required_fields = ["name","email","message"]

    for field in required_fields:
        value = data.get(field)
        if value is None or value.strip() == "":
            errors[field] = "This field cannot be empty"
        else:
            data[field] = str(value).strip()
        