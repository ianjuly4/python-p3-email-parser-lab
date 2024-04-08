# your code goes here!
import re
class EmailAddressParser:
    def __init__(self, email):
        if isinstance(email, str):
            self.email = email
        else:
            raise Exception("Email is not a string")
        
    def parse(self):
        email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', self.email)
        unique_addresses = list(set(email_addresses))
        unique_addresses.sort()
        return unique_addresses