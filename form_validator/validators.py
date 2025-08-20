import re

email_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def validate_form(data):
    errors = {}

    required_fields = ["name","email","message"]

    for field in required_fields:
        value = data.get(field)
        if value is None or value.strip() == "":
            errors[field] = "This field cannot be empty"
        else:
            data[field] = str(value).strip()
        
    
    email = data.get("email","")

    if email and not email_pattern.match(email):
        errors["email"] = "The email format is not valid"
    
    if len(errors) == 0:
        is_valid = True
    else:
        is_valid = False

    return is_valid , errors

form1 = {"name": "Ali", "email": "ali@example.com", "message": "salam"}
form2 = {"name": "", "email": "wrong@", "message": "  "}


print(validate_form(form1))
print(validate_form(form2))