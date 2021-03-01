import logging
logging.basicConfig(filename='output.log', format='%(asctime)s - %(levelname)s - %(message)s')

import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

def send_email(*args):
    """Sends an email with one or multiple attachments

    Parameters
    ----------
    *args : list
        A list of arguments, which will be the filenames

    Returns
    ----------
    None
    """

    message = Mail(
        from_email='me@tyshaikh.com',
        to_emails='tyshaikh29@gmail.com',
        subject='NYL Data Processing Results',
        html_content='See attached log file, CSV outputs and data visualization.')

    for arg in args:
        with open(arg, 'rb') as f:
            data = f.read()
            f.close()
        encoded_file = base64.b64encode(data).decode()

        attachedFile = Attachment(
            FileContent(encoded_file),
            FileName(arg)
        )
        message.attachment = attachedFile

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as e:
        logging.error(e.message)
