all:
	python3 main.py
server:
	pm2 start main.py --interpreter=/usr/bin/python3
list:
	pm2 list
stop:
	pm2 stop main.py
