class Contact:
    all_contacts = []
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        all_contacts.append(self)
        
class MailSender:
    def send_mail(self, message):
        print("send mail to", self.email)
        # e-mail logic
        
class EmailableContact(Contact, MailSender):    # Multiple inheritance
    pass

