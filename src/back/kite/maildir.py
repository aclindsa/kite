import mailbox
import email.utils
import re

def read_mail(path):
    mdir = mailbox.Maildir(path)
    return mdir

def extract_email_headers(msg):
    """Extract headers from email"""

    msg_obj = {}
    msg_obj["from"] = {}
    from_field = msg.getheaders('From')[0]
    msg_obj["from"]["name"], msg_obj["from"]["address"] = email.utils.parseaddr(from_field)
    msg_obj["to"] = email.utils.getaddresses(msg.getheaders('To'))
    

    msg_obj["subject"] = msg.getheaders('Subject')[0]
    msg_obj["date"] = msg.getheaders('Date')[0]

    return msg_obj

def extract_email(msg):
    """Extract all the interesting fields from an email"""
    msg_obj = extract_email_headers(msg)
    msg_obj["contents"] = msg.fp.read()
    return msg_obj

def get_emails(mdir):
    l = []
    for id, msg in mdir.iteritems():
        msg_obj = extract_email(msg)
        msg_obj["id"] = id
        l.append(msg_obj)
    return l

def get_email(mdir, id):
    msg = mdir.get(id)
    return extract_email(msg)
