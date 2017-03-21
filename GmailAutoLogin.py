import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Gmail Auto Login
#Coded by | WarLord
#https://github.com/saanwer
def getID(url):
	pUrl = urlparse.urlparse(url)
	return urlparse.parse_qs(pUrl.query)['id'][0]

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("email", help="Gmail email")
	parser.add_argument("password", help="Gmail password")
	args = parser.parse_args()

	browser = webdriver.Firefox()
	browser.get("https://accounts.google.com")

	emailElement = browser.find_element_by_id("Email")
	emailElement.send_keys(args.email)
	emailElement.submit()
	time.sleep(4)
	passElement = browser.find_element_by_id("Passwd")
	passElement.send_keys(args.password)
	passElement.submit()
	time.sleep(5)
	browser.get("https://mail.google.com/mail/u/0/")

	os.system('cls')#os.system('clear') if Linux
	print "[+] Auto login success!"
	browser.close()

if __name__ == "__main__":
	Main()
