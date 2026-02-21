import smtplib
from email.mime.text import MIMEText

class Mailer:

    def __init__(self, sender, password, smtp_port=587, mail_service='gmail'):
        self.sender = sender
        self.password = password
        self.smtp_port = smtp_port
        self.smtp_service = self.get_smtp_service(mail_service)
    def send_mail(self, recepients, raw_message):
        msg =  self.prep_msg(recepients, raw_message)
        try:
            print("sending mail")
            with smtplib.SMTP(self.smtp_service, self.smtp_port) as smtp_server:
                smtp_server.ehlo()
                smtp_server.starttls()
                smtp_server.ehlo()
                smtp_server.login(self.sender, self.password)
                smtp_server.sendmail(self.sender, recepients, msg.as_string())
                return "Email sent successfully"
        except Exception as e:
            return e
        
    def prep_msg(self, recepients,raw_message):
        msg = MIMEText(raw_message['body'])
        msg['Subject'] = raw_message['subject']
        msg['From'] = self.sender
        msg['To'] = ', '.join(recepients)
        return msg

    def get_smtp_service(self, mail_service):
        if 'gmail' in mail_service.lower():
            return 'smtp.gmail.com'
        else:
            # implement others here TODO
            return None




# password: kktu hyol adbb qfjo # password: kktu hyol adbb qfjo

# lajk ducj puuw mamb 
