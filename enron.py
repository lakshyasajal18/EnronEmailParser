import re
import argparse
import sys

class Server:
    """
    A class representing that stores emails
    """
    def __init__(self, path):
        """
       the server with emails from the given file path
        
        Args:
            path(str): path to the file containing the emails"""
        self.emails = [] 
        
        with open(path, 'r') as file:
            email_list = file.read().split('End Email\"')
            email_list.pop() #Remove the last empty element
            
            for email in email_list:
                #Extract email components using regular expressions
                message_id = re.search(r'Message-ID:(.+)' , email)
                date = re.search (r'Date: (.+?)\n', email)
                subject = re.search(r'Subject: (.+?)\n', email)
                sender = re.search(r'From: (.+?)\n', email)
                receiver = re.search(r'To: (.+?)\n', email)
                body = re.search(r'X-FileName:[\d\D]+', email)
                
                #Set component values to None if not found
                message_id = message_id.group() if message_id else None
                date = date.group() if date else None
                subject = subject.group() if subject else None
                sender = sender.group() if sender else None
                receiver = receiver.group() if receiver else None
                body = body.group() if body else None
                
                #Create an Email object and add it to the server's email list
                e=Email(message_id, date, subject, sender, receiver, body)
                self.emails.append(e)
                         
class Email:
    """
    A class representing email
    """
    def __init__(self, message_id, date, subject, sender, receiver, body):
        """an email with the given components
        
        Args:
            message_id (str): ID of the email 
            date (str): date of the email
            subject (str): subject of the email
            sender (str): sender of the email
            receiver (str): receiver of the email
            body (str): body of the email
        """
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body
        
def main(Path):
    """
    The main function
    
    Args:
        Path(str): the path to the file containing the emails
    
    Returns:
        int: the number of emails in the server"""
    server_class = Server(Path)
    return len(server_class.emails)

def parse_args(args_list):
    instance_parser = argparse.ArgumentParser()
    instance_parser.add_argument('path', type=str, help="Path of the file")
    return instance_parser.parse_args(args_list)
        
if __name__== "__main__":
    arguments = parse_args(sys.argv[1:])
    result = main(arguments.path)