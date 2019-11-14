#coded by Angga Surya 
import urllib.request
import re
import time
import os


def angga():
	print("\033[96m=" * 100)
	print("\033[96m$$\                               $$\ ")                       
	print("\033[96m\__|                              \__| ")                       
	print("\033[96m$$\  $$$$$$\   $$$$$$\   $$$$$$\  $$\     $$$$$$$\  $$$$$$\ ")
	print("\033[96m$$ |$$  __$$\  \____$$\ $$  __$$\ $$ |   $$  _____|$$  __$$\ ")
	print("\033[96m$$ |$$ /  $$ | $$$$$$$ |$$ /  $$ |$$ |   $$ /      $$ /  $$ | ")
	print("\033[96m$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |   $$ |      $$ |  $$ | ")
	print("\033[96m$$ |$$$$$$$  |\$$$$$$$ |$$$$$$$  |$$ |$$\\$$$$$$$\ \$$$$$$  | ")
	print("\033[96m\__|$$  ____/  \_______|$$  ____/ \__|\__|\_______| \______/ ")
	print("\033[96m    $$ |                $$ |                              ")
	print("\033[96m    $$ |                $$ |                              ")
	print("\033[96m    \__|                \__|                              ")
	print("\033[33m\nCoded by : Angga Surya Pardana (github.com/EvCf1703)\n")
	print("\033[96m=" * 100)
	hi = input("\n\033[97m\nEnter your IP : \033[31m")
time.sleep(2)

os.system("clear")
hi = urllib.request.Request('https://ipapi.co/xml')
c = urllib.request.urlopen(hi)
y = c.read()
Success = c.getcode()


os.system("clear")

angga()
time.sleep(3)
print("\n")
regex = re.findall(r'<ip>(.*?)</ip>',str(y))
for regex in regex:
    print("\033[97mYour Ip : \033[31m" + regex)
regex = re.findall(r'<city>(.*?)</city>',str(y))
print('\033[97mSuccess : \033[92m{}'.format(c.getcode()))
print("\n")
#coded by angga surya
time.sleep(3)

for regex in regex:
    print("\033[97mCity : " + regex)
regex = re.findall(r'<region>(.*?)</region>',str(y))
for regex in regex:
    print("\033[97mRegion : " + regex)
regex = re.findall(r'<region_code>(.*?)</region_code>',str(y))
for regex in regex:
    print("\033[97mRegion Code : " + regex)
regex = re.findall(r'<country>(.*?)</country>',str(y))
for regex in regex:
    print("\033[97mCountry : " + regex)
regex = re.findall(r'<country_name>(.*?)</country_name>',str(y))
for regex in regex:
    print("\033[97mCountry Name : " + regex)
regex = re.findall(r'<continent_code>(.*?)</continent_code>',str(y))
for regex in regex:
    print("\033[97mContinent Code : " + regex)
regex = re.findall(r'<in_eu>(.*?)</in_eu>',str(y))
for regex in regex:
    print("\033[97mIn Eu : " + regex)
regex = re.findall(r'<latitude>(.*?)</latitude>',str(y))
for regex in regex:
    print("\033[97mLatitude : " + regex)
regex = re.findall(r'<longitude>(.*?)</longitude>',str(y))
for regex in regex:
    print("\033[97mLongitude : " + regex)
regex = re.findall(r'<timezone>(.*?)</timezone>',str(y))
for regex in regex:
    print("\033[97mTimezone : " + regex)
regex = re.findall(r'<utc_offset>(.*?)</utc_offset>',str(y))
for regex in regex:
    print("\033[97mUtc Offset : " + regex)
regex = re.findall(r'<country_calling_code>(.*?)</country_calling_code>',str(y))
for regex in regex:
    print("\033[97mCountry Calling Code : " + regex)
regex = re.findall(r'<currency>(.*?)</currency>',str(y))
for regex in regex:
    print("\033[97mCurrency : " + regex)
regex = re.findall(r'<languages>(.*?)</languages>',str(y))
for regex in regex:
    print("\033[97mLanguages : " + regex)
regex = re.findall(r'<asn>(.*?)</asn>',str(y))
for regex in regex:
    print("\033[97mAns : " + regex)
regex = re.findall(r'<org>(.*?)</org>',str(y))
for regex in regex:
    print("\033[97mOrg : " + regex)
time.sleep(1.5)

print("don't forget to visit again")
