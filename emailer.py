import smtplib, ssl

sender_email = "testreuben90@gmail.com"
receiver_email = "reubena.kavalov@gmail.com"
message = """\
Subject: Test SUBJECT

This message is sent from Python."""

# Send email here

port = 465  # For SSL
password = 'Reubentest123!'

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("testreuben90@gmail.com", password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message)
