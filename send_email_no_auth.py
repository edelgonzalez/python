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

sender="icinga@teradatacloud.com"
recipient="edgar.gonzalez@teradata.com"


msg = "\r\n".join([
  "From: " + sender,
  "To: " + recipient,
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])


server = smtplib.SMTP('10.25.41.150',25)
#server.ehlo()
#server.starttls()
server.ehlo()
# server.mail(sender)
# server.rcpt(recipient)
# server.data(msg)
# server.quit()

server.sendmail(sender,recipient, msg)
