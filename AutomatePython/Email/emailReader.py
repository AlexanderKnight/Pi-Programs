#! /usr/bin/python3

import imapclient
import pyzmail
#from OpenSSL import SSL
#from OpenSSL import crypto

passwdFile = open('Em_passwd.pwd')
passwd = passwdFile.read()
passwdFile.close()
print("Password retrieved and stored")
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
print('IMAP connected')
try:
	imapObj.login('Silverpi936@gmail.com',passwd)
	print('Logged In!')
except Exception as exc:
	print("I could not log on. /n "+exc)


repeat = True
while repeat ==True:
	imapObj.select_folder('INBOX',readonly=False)
	UIDs = imapObj.search(['ALL'])
	
	print(UIDs)
	print('What message would you like to see?')
	index = int(input())
	for i in range(len(UIDs)):
		if index == UIDs[i]:
			pickedUID = UIDs[i]
	rawMessages = imapObj.fetch([pickedUID], ['BODY[]','FLAGS'])
	message = pyzmail.PyzMessage.factory(rawMessages[pickedUID][b'BODY[]'])
	print('Subject: '+message.get_subject())
	fromMessage = 'From: '
	for i in range(len(message.get_addresses('from'))):
		for j in range(len(message.get_addresses('from')[i])):
			fromMessage += ', '+message.get_addresses('from')[i][j]
	print(fromMessage)
	if message.text_part != None:
		print('Message: \n'+message.text_part.get_payload().decode(message.text_part.charset))
	print('Would you like to delete this email?(y/n)')
	delete = input()
	if delete == 'y' or delete =='Y' or delete == 'yes' or delete == 'YES' or delete == 'Yes':
		imapObj.delete_messages(pickedUID)
	print('Would you like to read another email?(y/n)')
	answer = input()
	if answer == 'no' or answer =='NO' or answer =='n' or answer =='N' or answer =='No':
		repeat = False

imapObj.logout()
print('Logged out')

