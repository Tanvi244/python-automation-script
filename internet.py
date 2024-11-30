# AUTOMATION SCRIPT - MESSAGE AUTOMATICALLY SEND AT SPECIFIC EMAIL AT SPECIFIC TIME

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email(sender_email, sender_password, recipient_email, subject, message):
   
    msg = MIMEMultipart()                                    # Create message container
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

                                             
    msg.attach(MIMEText(message, 'plain'))                     # Add message body

    try:
       
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)                # Connect to SMTP server (e.g., Gmail's SMTP server)
        smtp_server.starttls()                                            # Start TLS encryption
        smtp_server.login(sender_email, sender_password)

        
        smtp_server.sendmail(sender_email, recipient_email, msg.as_string())   # Send email
        smtp_server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

def schedule_email(sender_email, sender_password, recipient_email, subject, message, scheduled_time):
   
    schedule.every().day.at(scheduled_time).do(send_email, sender_email, sender_password, recipient_email, subject, message)   # Schedule the email sending task

  
    while True:
        schedule.run_pending()           # Run the scheduler continuously
        time.sleep(1)

if __name__ == "__main__":
    sender_email = "tanvi.ghodke244@gmail.com"
    sender_password = "unbv bqdv glcz vdxr"         # Your email account password or app password
    recipient_email = "davikaghodke@gmail.com"
    subject = "Birthday wishes"
    message = "Wish you many many happy returs of the day your all dreams comes true god bless you!!!!"
    scheduled_time = "12:35"                        # Change this to the desired time in HH:MM format

    schedule_email(sender_email, sender_password, recipient_email, subject, message, scheduled_time)


    ###########################################################################################################


    
    # INPUT :   python internet.py
    # An error occurred while sending the email:(Username and Password not accepted) jevha password accept nahi honar tevha ha error yeil

    #INPUT : python internet.py
    # Email sent successfully (success jhala bcoz app password generate kela)