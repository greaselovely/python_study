"""
A study in email validation capability.  
Will be useful for someone somewhere.  
"""

def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."
    for l in string:
        if l not in valid:
            return True
    return False

def is_valid(email):
    if email.count('@') == 1:
        prefix, domain = email.split('@')
        if has_invalid_characters(prefix):
            return email + " is invalid"
        if has_invalid_characters(domain):
            return email + " is invalid"
        if len(prefix) >= 1 and domain.count('.') == 1:
            domain_name, extension = domain.split('.')
            if len(domain_name) >= 1:
                if len(extension) >= 1:
                    return email + " is valid"
    return email + " is invalid"

def check(email):
    import re
    #pattern = r"(^\w.*)@{1}(\w.*)(\.\w.*){1,3}"
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.findall(pattern, email):
        if has_invalid_characters(email):
            return email + " is valid"
    else:
        return email + " is invalid"

emails = [
    "test@example.com",
    "valid@gmail.com",
    "invalid@gmail",
    "invalid",
    "not an email",
    "invalid@email",
    "!@/",
    "test@@example.com",
    "test@.com",
    "test@site.",
    "@example.com",
    "an.example@test",
    "te#st@example.com",
    "test@exam!ple.com",
    "poop@brit.mail.com"
]

for e in emails:
    print(check(e))
