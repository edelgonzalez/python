# import smtplib
# server = smtplib.SMTP('smtp.gmail.com:587')
# server.ehlo()
# server.starttls()
#
# server.login("eegonzalezv@gmail.com", "verenjena")
#
# msg = "\r\n".join([
#   "From: eegonzalezv@gmail.com",
#   "To: edgar.gonzalez@teradata.com",
#   "Subject: Just a message",
#   "",
#   "Why, oh why"
#   ])
# server.sendmail("eegonzalezv@teradata.com","edgar.gonzalez@teradata.com", msg)


import smtplib
server = smtplib.SMTP('email-smtp.us-west-2.amazonaws.com',25)
#server.ehlo()
server.starttls()
sender="edgar.gonzalez@teradata.com"
recipient="edgar.gonzalez@teradata.com"

server.login("AKIAIIRLY3AZAH56323A", "AtVnIOv7lKrte1qIZFBPLyMcXZBasa9w+H9IodDXC+fC")

msg = "\r\n".join([
  "From: " + sender,
  "To: " + recipient,
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])

server.sendmail(sender,recipient, msg)
