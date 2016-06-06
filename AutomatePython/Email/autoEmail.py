#! python3
#email.py - Defines a function to send an email from Silverpi936@gmail.com to a
# specified email address. It requires a 'to' address, the subject, and the body.

import smtplib

#Get passwd from file
passwdFile = open('Em_passwd.pwd')
passwd = passwdFile.read()
passwdFile.close()

# Preset values
myEmail = 'Silverpi936@gmail.com'

def autoEmail(target, subject, body):
    repeat = True
    while repeat == True:
        try:
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(myEmail,passwd)
            smtpObj.sendmail(myEmail,target,'Subject: %s \n%s'%(subject,body))
            smtpObj.quit()
            repeat = False
        except:
            print("I am trying to email %s with subject %s and body %s."%(target, subject, body))
            print("Something went wrong. Should I try again? (y/n)")
            answer = input()
            if answer =='n' or answer =='N' or answer =='no' or answer =='No' or answer =='NO':
                repeat = False
                
