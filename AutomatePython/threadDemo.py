#! /usr/bin/python3

import threading, time

print('Start of program.')

def takeaNap():
	time.sleep(5)
	print('Wake up!')

threadObj = threading.Thread(target=takeaNap)
threadObj.start()

print('End of program')
