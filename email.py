import smtplib

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import COMMASPACE, formatdate

from_addr = 'pybitesblog@gmail.com'
to_addr = ['bob@rocks.com', 'julis_is@awesome.com']
msg = MIMEMultipart()

msg['From'] = from_addr
msg['To'] = ", ".join(to_addr)
msg['Subject'] = "Test Automation Email"

from_addr = 'pybitesblog@gmail.com'
to_addr = 'pybitesblog@gmail.com'
recipients = ['bob@rocks.com', 'julian_is@awesome.com']
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Bcc'] = ", ".join(recipients)
msg['Subject'] = 'Test Automation Email'