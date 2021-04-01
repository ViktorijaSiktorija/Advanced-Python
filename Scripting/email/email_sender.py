# built in modul
import smtplib  # smtp server, protkol za slanje mejlova
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Template, da postane template objekat
html = Template(Path('index.html').read_text())
# zeza gugl u kursu pise sta treba da se promeni
email = EmailMessage()
email['from'] = 'Viktorija Siktorija'
email['to'] = 'viktorija@gmail.com'
email['subject'] = 'Dobila si na lutriji!'

# sadrzaj emaila set_content
# substitute jer je template, da zamenimo name u html
email.set_content(html.substitute({'name': 'muahah'}), 'html')

# smtp server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # 587 standard protokola SMTP
    # ehlo metoda, da oznaci da je server tu
    smtp.ehlo()
    # tls - enkripsn mehanizam
    smtp.starttls()
    smtp.login('vika@gmail.com', 'pasword')
    smtp.send_message(email)
