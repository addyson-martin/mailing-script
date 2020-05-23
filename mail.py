import smtplib 
import zaroorisaman
#import sys
#import random
#from email.mime.text import MIMEText
def send(fp,server,sender_mail,send_to_email,message,sent_status):
    server.sendmail(sender_mail, send_to_email, message)
    fp.write('email sent to '+send_to_email+'\n')
    sent_status.append(send_to_email)
sent_status=[]
#### this code block is for cli
#recipent_name=[(str(sys.argv[1].strip()))]
#recipent_mail=[(str(sys.argv[2].strip()))]

#list contains the name of the recipents 
recipent_name=['test1','test2']
#list contains the emails of the recipents
recipent_mail=['mail1@iiit-bh.ac.in','mail2@gmail.com']

##### block ends
names=recipent_name
sender_mail=zaroorisaman.u_mail
sender_pass=zaroorisaman.passwd
send_to_email =recipent_mail
len_list=len(send_to_email)
fp=open('response.txt','a')
# print(names,send_to_email)
server = smtplib.SMTP('smtp.gmail.com', 587)


#enter the subject and body of your mail over here resp. 
subject = "subject of the mail"
body="Your body of mail "


server.starttls()

server.login(sender_mail, sender_pass)
for i in range(len_list):
    body_temp= 'Dear ' + names[i] +',\n' +body
    message = 'Subject: {}\n\n{}'.format(subject,body_temp)
    send(fp,server,sender_mail,send_to_email[i],message,sent_status)
server.quit()
print("Email Sent Successfully!..A log can be found in response.txt")
fp.close()
