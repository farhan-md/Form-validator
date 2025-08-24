import re

email_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def validate_name(name):
    if name is None:
        return False
    
    # Delete space form beginning and end
    if name.strip() == "":
        return False
    
    return True

def validate_email(email):
    if email is None:
        return False
    
    if not email_pattern.match(email):
        return False
    
    return True

def validate_message(message):
    if not message:
        return False
    
    if message.strip() == "":
        return False
    
    return True


def validate_form(data):
    if not validate_name(data.get("name","")):
        return False,"Name cannot be empty"
    
    if not validate_email(data.get("email","")):
        return False,"Invalid email format"
    
    if not validate_message(data.get("message","")):
        return False,"Message cannot be empty"
    
    return True,"Form is valid"
form1 = {"name": "Ali", "email": "ali@example.com", "message": "salam"}
form2 = {"name": "", "email": "wrong@", "message": "  "}


print(validate_form(form1))
print(validate_form(form2))