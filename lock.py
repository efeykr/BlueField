import subprocess
import threading
import time
import os
starttime = time.time()
begin = 'xscreensaver -no-splash &'
while True:
	s = subprocess.Popen("bluetoothctl info", shell=True, stdout=subprocess.PIPE)
	subprocess_return = s.stdout.read()
	subprocess_return = subprocess_return.split()
	s.stdout.close()
	if (subprocess_return[0].decode("utf-8")) == "Missing":
		a = subprocess.Popen("xscreensaver-command -activate", shell=True, stdout=subprocess.PIPE)
		subprocess_return = a.stdout.read()
		subprocess_return = subprocess_return.split()
		a.stdout.close()
	else: 
		
		b = subprocess.Popen("xscreensaver-command -deactivate ", shell=True, stdout=subprocess.PIPE)
		b.stdout.close()
	time.sleep(5)
