import smtplib
with open(r'D:\Jarvis\protocol.txt') as f:
    line=f.readlines()   

content = 'mail sent from python code'

server = smtplib.SMTP('smtp.gmail.com',587)

server.ehlo()
server.starttls()
server.login('bosssam29518@gmail.com',line[-1])
server.sendmail('bosssam29518@gmail.com', 'sameer.alam100@gmail.com', content)
server.close()

print('Mail sent')