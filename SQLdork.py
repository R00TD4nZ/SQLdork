###############################
#
#author:r00t#d4nZ with bhai45bull
#desain:r00t#d4nZ with bhai45bu11
#usage:
#python SQLdork.py
#enter your dork
#Install google search first before using
#
###############################

from googlesearch import search
import urllib2
import os
import socket
import sys
from bs4 import BeautifulSoup

red	= 	"\033[01;31m"
green = 	"\033[01;32m"
yel =		"\033[01;33m"
end 	=	"\033[0m"

os.system("clear")

def credit():
    print '''\033[0m
    
      ________  ______     __         ______                   __   __
     ' ______' / ____ \   / /        / ____ \  ______         |  / / /
    / /_____  / /   / /  / /        / /   / / / ____ \   ____ | | / /
   '______  '/ /   / /  / /        / /   / / / /   / / /' __ '| '' /
  ______/ / / /__\ \/  / /_____   / /__ / / / /___/ / / /'  ' | | \ \ 
 '_______'  \_____\_\ /_______/  /_____'_/  \______/ /_/      |_/  \_\.


\033[1;91m }---------------[!] Scanner Google [!]---------------{
 |-------} Scanner SQL vulnerability with Dork {------|
  
 \033[1;91m[!]\033[0m SQL DORK SCANNER WEBSITE VULNERABILITY GOOGLE
 \033[1;91m[!]\033[0m Author : r00t#d4nZ
 \033[1;91m[!]\033[0m Github : https://github.com/R00TD4nZ/SQLdork
 \033[1;91m[!]\033[0m Team   : CR45H FIGHTER TEAM_C
 Use > Enter Dork SQL : example inurl:index.php?id=
 '''

def word_err(soup):
    i=-1
    words=['Warning', 'Fatal Error','Mysql','mysql','SQL','MySQL']
    for word in words:
	if word in str(soup):
		i+=1
    return i


def vuln_test(url):
    try:
	response =urllib2.urlopen(url)
	soup = BeautifulSoup( response.read(), 'html.parser' )
	url2=url+"'"
	response2=urllib2.urlopen(url2)
	soup2 = BeautifulSoup(response2.read(),'html.parser')
	if soup!=soup2 :
	    if word_err(soup2) > -1 :
		print "\n[%s*%s]Website SQL vulnerability =>  %s "% (green,end,url2)
    except urllib2.HTTPError :
	pass    
    except urllib2.URLError:
	pass
    
    
credit()
dork =raw_input("Dork Sql~# ")
try:
    url_list=search(dork)
    for url in url_list:
	vuln_test(url)    
except urllib2.HTTPError:
    print "%sNot Found Website Vuln%s (restart connection)  " %(green,red) 
 
