#!/usr/bin/python

# I LOVE Python :)
# Simple Script For Download Viedos From Youtube :)
# This Script Coded By: Oseid Aldary
# Let's Started :)

# COLORS ##################
wi = "\033[1;37m" #>>White#
rd = "\033[1;31m" #>Red   #
gr = "\033[1;32m" #>Green #
yl = "\033[1;33m" #>Yallow#
###########################
import socket,sys,optparse,urllib
from lxml import etree
from os import system as sy
sy("")
try:
  from pytube import YouTube as YT
  from pytube.exceptions import RegexMatchError as YTERROR1, VideoUnavailable as YTERROR2
except:
	print(rd+"\n[!]"+yl+" Error: "+wi+" ["+gr+" Pytube "+wi+"] Library Is Not Exist "+rd+"!!!")
	print(gr+"[+]"+wi+" Please Download It Use This Command: "+gr+"pip install pytube")
	exit(1)

## Check Your Internet Connection ##
server = "www.google.com"
def check():
  try:
    ip = socket.gethostbyname(server)
    con = socket.create_connection((ip, 80), 2)
    return True
  except socket.error:
	pass
  return False
cnet = check()

#[ For Download One Video]
def YTD_1v(link):
	if cnet == True: # Connected :)
	    print(gr+"\n["+wi+"~"+gr+"]"+wi+" Download Vedio In Progress "+gr+"....")
	    try:
	      title = etree.HTML(urllib.urlopen(link).read())
	      title = title.xpath("//span[@id='eow-title']/@title")
	      if len(title) > 0:
	       title = ''.join(title)
	       print(gr+"  ["+wi+"+"+gr+"]"+wi+" Video Title: "+yl+title)
	      YT(link).streams.first().download("output/")
	      print(gr+"  ["+wi+"+"+gr+"]"+wi+" Download "+gr+"Complete :)")
	      print(gr+"  ["+wi+"~"+gr+"]"+wi+" Saved In: "+gr+"output/"+yl+title)
	    except YTERROR1:
		print(rd+"\n  ["+yl+"!"+rd+"]"+yl+" Please Check Video Link "+rd+"!!!")
		exit(1)
	    except YTERROR2:
                print(rd+"\n  ["+yl+"!"+rd+"]"+yl+" Please Check Video Link "+rd+"!!!")
                exit(1)
	    except KeyboardInterrupt:
		 print(" ")
		 exit(1)
	else:
	   print(rd+"\n[!]"+yl+" Please Check Your Internet Connection "+rd+"!!!")
	   exit(1)
# [For Download Youtube PlayList]
def YTD_flst(flst):
	try:
	  flstop = open(flst, "r").readlines()
	except:
	    print(rd+"\n[!]"+wi+"bash: cd: {}: No such file or directory".format(flst))
	    exit(1)
	if cnet == True: # Connected :)
	    print(gr+"\n["+wi+"~"+gr+"]"+wi+" Download All Videos From File List"+gr+"[~]")
	    loop = 1
	    for link in flstop:
	      link = str(link).strip()
	      try:
		 print(wi+"["+gr+str(loop)+wi+"]"+gr+" Downloading Video_Url[ "+wi+str(link)+gr+" ]")
                 title = etree.HTML(urllib.urlopen(link).read())
                 title = title.xpath("//span[@id='eow-title']/@title")
                 if len(title) > 0:
                   title = ''.join(title)
                   print(gr+"  ["+wi+"+"+gr+"]"+wi+" Video Title: "+yl+title)
		 fname = "{}({})".format(title,str(loop))
		 YT(link).streams.first().download("output/", filename=str(fname))
	         print(gr+"  ["+wi+str(loop)+gr+"]"+wi+" Video Download "+gr+"Complete ")
		 print(gr+"  ["+wi+"~"+gr+"]"+wi+" Saved In: "+gr+"output/"+fname)
		 print(" ")
	      except YTERROR1:
		print(rd+"  ["+yl+"!"+rd+"]"+yl+" Check Video Link In Line["+rd+str(loop)+yl+"] In File List "+rd+"!!!\n")
	      except YTERROR2:
                print(rd+"  ["+yl+"!"+rd+"]"+yl+" Check Video Link In Line["+rd+str(loop)+yl+"] In File List "+rd+"!!!\n")
	      except KeyboardInterrupt:
		 print(" ")
		 exit(1)
	      except EOFError:
		 print(" ")
		 exit(1)
	      loop +=1
	else:
	   print(rd+"\n[!]"+yl+" Please Check Your Internet Connection "+rd+"!!!")
	   exit(1)
 
## Usage ##

parse = optparse.OptionParser("""
Usage: python YTD.py [OPTIONS]
 _______________________________________________________________________________
|          .:: OPTIONS ::.            	       .:: Description ::.              |
+==================================+============================================+
+				   +						+
|  -u --video-url <Video Url>      |  Download Single Video From YouTube	|
+  -f --file-list <video Url File> +  Download All Video From Links File	+
|				   |						|
+==================================+============================================+
""")
def main():
  parse.add_option("-u","--video-url",dest="ovd",type="string")
  parse.add_option("-f","--file-list",dest="flst",type="string")
  (options,args) = parse.parse_args()
  if options.ovd !=None:
	link = options.ovd
        YTD_1v(link)

  elif options.flst !=None:
	flst = options.flst
	YTD_flst(flst)
  else:
     print(parse.usage)
     exit(1)

if __name__ == "__main__":
    main()

##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
