import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("2k20it29@kiot.ac.in", "SJ000$sj000")

# message to be sent
message = "Hi this is a testing mail function.\nThank you."

# sending the mail
s.sendmail("2k20it29@kiot.ac.in", "sanjainandhagopal@gmail.com", message)

# terminating the session
s.quit()
