#Bruce Reyes 
#INST326
import re
import argparse
import sys

#Server Class
class Server:
    """
    Stores all for all data for emails

    Attributes: emails: a list of email objects where each object corresponds to one email
    
    """
    #Init Method
    def __init__(self, path):
        """
        opens the file specified by the path for reading.
        sets attributes to a list of email objects.
        takes objects of email: message id, date, subject,
        sender, receiver, and body
        appends the objects to email
        
        Takes in Args of path:
            path to the file that we are going to read.

        """
        self.emails = []
        with open(path, 'r') as file:
            data = file.read()
            emails = [email.strip() for email in data.split("End Email\"")
                      if email.strip()]

            for email in emails:
                message_id = re.search(r"Message-ID: <(.+?)>", email).group(1)
                date = re.search(r"Date: (.+)", email).group(1)
                subject = re.search(r"Subject: (.*)", email).group(1)
                sender = re.search(r"From: (.*)", email).group(1)
                receiver = re.search(r"To: (.*)", email).group(1)
                body = re.search(r"\n\n([\s\S]*)", email).group(1)
                
                email = Email(message_id, date, subject, sender,receiver, body)
                self.emails.append(email)
      
#Email Class
class Email():
    """
    stores and initializes all of the objects of the email in server.emails list

    has unique attributes of each email which are stored as strings:
        message_id: unique id for all message
        date: date of email
        subject: subject of email
        sender: sender of email
        receiver: recipient of email
        body: content of the email
    """
    def __init__(self, message_id, date, subject, sender, receiver, body):
        """
        initializes and stores all of the attributes of the email
        """
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body

#main Method
def main(path):
    """
    instance of server class is created and uses the path which

    takes in path of text file being parsed

    returns length as integer of email in instance
    """
    server = Server(path)
    return len(server.emails) 

#parser method
def parse_args(args_list):
    """
    Instance created from ArgumentParser module
    takes in args_list as argument 

    returns object created from Argument parser
     
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help = "Path to the text file", type = str)
    return parser.parse_args(args_list)

#if name = main which is needed later
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.path)