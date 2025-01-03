import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, message_body):
    try:
        # Set up the SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(message_body, 'plain'))

        # Start the server connection and login
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")

    finally:
        # Terminate the SMTP session
        server.quit()

# Example usage:
sender_email = "14annarose@gmail.com"
sender_password = "your-password"  # For Gmail, you may need an app password.
receiver_email = "recipient-email@example.com"
subject = "Test Email"
message_body = "This is a test email sent from Python."

send_email(sender_email, sender_password, receiver_email, subject, message_body)
