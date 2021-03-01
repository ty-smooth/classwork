import logging
import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)


def add_attachment(message, file):
    """Sends an email with one or multiple attachments

    Parameters
    ----------
    message : obj
        A Mail object
    file : str
        The filename of the attachment

    Returns
    ----------
    True : bool
        A confirmation that the file was attached
    """

    try:
        with open(file, 'rb') as f:
            data = f.read()
            f.close()
        encoded_file = base64.b64encode(data).decode()

        attachedFile = Attachment(
            FileContent(encoded_file),
            FileName(file)
        )
        message.attachment = attachedFile
        return True
    except:
        logging.error("We were unable to attach the file")
        return False


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

    attached = [add_attachment(message, arg) for arg in args]

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as e:
        logging.error(e.message)
