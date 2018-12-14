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
pu = "\033[1;35m" #>Purple# 
###########################
import socket,sys,optparse,re
from os import system as sy
sy("")
try:
  import requests
  from pytube import YouTube as YT
except ImportError as e:
        e = e[0][16:]
	print(rd+"\n[!]"+yl+" Error: "+wi+" ["+gr+e+wi+"] Library Is Not Exist "+rd+"!!!")
	print(gr+"[+]"+wi+" Please Download It Use This Command: "+gr+"pip install "+e)
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
## Get Video Title
def get_title(video_url):
  response = requests.get(video_url).text
  title = re.findall(r'"title":"[^>]*",',response)[0].split(',')[0][9:-1]
  return title


## [For Download Single Video]
def YTD_1v(link):
	if cnet != True:
          	   print(rd+"\n["+yl+"!"+rd+"]"+yl+" Please Check Your Internet Connection "+rd+"!!!")
          	   exit(1)
        
        print(gr+"\n["+wi+"~"+gr+"]"+wi+" Download Vedio In Progress "+gr+"....")
	try:
           title = get_title(link)
        except IndexError:
                title = "Unknown Video Title !!!"
        print(gr+"  ["+wi+"+"+gr+"]"+wi+" Video Title: "+yl+title)
        try:
          YT(link).streams.first().download("output/")
          print(gr+"  ["+wi+"+"+gr+"]"+wi+" Download "+gr+"Complete :)")
	  print(gr+"  ["+wi+"~"+gr+"]"+wi+" Saved In: "+gr+"output/"+yl)
	except KeyboardInterrupt:
                print(" ")
                exit(1)
        except EOFError:
                print(" ")
                exit(1)

# [For Download Youtube Videos In Playlist]

def plyre(url):
    if cnet != True:
      print(rd+"\n["+yl+"!"+rd+"]"+yl+" Please Check Your Internet Connection "+rd+"!!!")
      exit(1)
    
    if "list=" not in str(url):
        print(rd+"\n["+yl+"!"+rd+"]"+yl+" Error: Incorrect Playlist URL "+rd+"!!!\n["+yl+"!"+rd+"]"+yl+" Please Check Your Playlist URL"+rd+"!")
        exit(1)
    req = url.rfind('=') + 1
    ply = url[req:]
    try:
        response = requests.get(url).text
    except Exception:
        print(rd+"["+yl+"!"+rd+"]"+yl+" Error: Please Check Your YouTube PlayList URL "+rd+"!!!")
        exit(1)
    repl = re.compile(r'watch\?v=\S+?list=' + ply)
    found = re.findall(repl, response)
    urls = []
    if found:
        for ur in found:
            if '&' in ur:
              vurl= ur.index('&')
            urls.append('http://www.youtube.com/' + ur[:vurl])
        checked = []
        videos_URLS = []
        for i in urls:
            if i in checked: continue
            videos_URLS.append(i)
            checked.append(i)
        loop = 1
        print(gr+"\n["+wi+"~"+gr+"]"+wi+" Download PlayList In Progress"+gr+"....")
        hmany = len(videos_URLS)
	print(wi+"  ["+gr+"*"+wi+"]"+gr+" Total Videos In PlayList <"+yl+str(hmany)+gr+">")
	print(wi+"-------------------------------------")
        for link in videos_URLS:
          if not link.strip(): continue
          link = link.strip()
          try:
            print(wi+"  ["+gr+str(loop)+wi+"]"+gr+" Downloading Video_Url[ "+wi+str(link)+gr+" ]")
            try:
              title = get_title(link)
            except IndexError:
              title = "Unknown Video Title !!!"
            print(gr+"  ["+wi+"+"+gr+"]"+wi+" Video Title: "+yl+title)
	    fname = "{}({})".format(title,str(loop))
	    YT(link).streams.first().download("output/", filename=str(fname))
	    print(gr+"    ["+wi+str(loop)+gr+"]"+wi+" Video Download "+gr+"Complete ")
	    print(gr+"    ["+wi+"~"+gr+"]"+wi+" Saved In: "+gr+"output/"+fname)
	    print(pu+"========")
	  except KeyboardInterrupt:
		 print(" ")
		 exit(1)
	  except EOFError:
		 print(" ")
		 exit(1)
          except Exception as e:
                print(rd+"  ["+yl+"!"+rd+"]"+yl+" Error: In Video Number["+rd+str(loop)+yl+"] In PlayList "+rd+"!!!\n")
	  loop +=1
    else:
        print(rd+"["+yl+"!"+rd+"]"+yl+" No videos Was Found In This PlayList "+rd+"!!!")
        exit(1)
                    
# [For Download Youtube Videos from File Link]
def YTD_flst(flst):
	try:
	  flstop = open(flst, "r").readlines()
	except IOError:
	    print(rd+"\n["+yl+"!"+rd+"]"+yl+"Error: No such File: ["+rd+flst+yl+"]"+rd+" !!!")
	    exit(1)
	if cnet == True: # Connected :)
	    print(gr+"\n["+wi+"~"+gr+"]"+wi+" Download All Videos From File List"+gr+"[~]")
	    loop = 1
	    for link in flstop:
	      link = str(link).strip()
	      try:
		 print(wi+"["+gr+str(loop)+wi+"]"+gr+" Downloading Video_Url[ "+wi+str(link)+gr+" ]")
	         try:
                   title = get_title(link)
                 except IndexError:
                    title = "Unknown Video Title !!!"
                 print(gr+"  ["+wi+"+"+gr+"]"+wi+" Video Title: "+yl+title)
		 fname = "{}({})".format(title,str(loop))
		 YT(link).streams.first().download("output/", filename=str(fname))
	         print(gr+"  ["+wi+str(loop)+gr+"]"+wi+" Video Download "+gr+"Complete ")
		 print(gr+"  ["+wi+"~"+gr+"]"+wi+" Saved In: "+gr+"output/"+fname)
		 print(" ")
	      except KeyboardInterrupt:
		 print(" ")
		 exit(1)
	      except EOFError:
		 print(" ")
		 exit(1)
              except Exception as e:
                print(rd+"  ["+yl+"!"+rd+"]"+yl+" Check Video Link In Line["+rd+str(loop)+yl+"] In File List "+rd+"!!!\n")
	      loop +=1
	else:
	   print(rd+"\n["+yl+"!"+rd+"]"+yl+" Please Check Your Internet Connection "+rd+"!!!")
	   exit(1)
 
## Usage ##

parse = optparse.OptionParser("""
Usage: python YTD.py [OPTIONS]
 ________________________________________________________________________________
|          .:: OPTIONS ::.            	       .:: Description ::.               |
+===================================+============================================+
+				    +						 +
|  -u --video-url <Video Url>       |  Download Single Video From YouTube	 |
+                                   +                                            +
|  -p --playList  <PlayList Url>    |  Download All Videos In YouTube PlayList   |
+                                   +                                            +
|  -f --fileList  <Video File Links>|  Download All Video From Links File	 |
+				    +						 +
|===================================+============================================|
|                            .:: EXAMPLES ::.                                    |
==================================================================================
|[1]~[Download Single YouTube Video]
|---->>>>>>>>>>>>>>> python YTD.py -u https://youtu.be/60ItHLz5WEA
|
|[2]~[Download Some YouTube PlayList]
|---->>>>>>>>>>>>>>> python YTD.py -p https://www.youtube.com/watch?v=_UonBSAzITE&list=PLYT4vq6pQVSv3zECGufMrCDXKX0Ouxzde
|
|[3]~[Download All Videos From File Videos Links]
|---->>>>>>>>>>>>>>> python YTD.py links.txt

""")
def main():
  parse.add_option("-u","-U","--video-url","--VIDEO-URL",dest="ovd",type="string")
  parse.add_option("-f","-F","--filelist", "--FILELIST",dest="flst",type="string")
  parse.add_option("-p","-P","--playlist","--PLAYLIST",dest="plyls",type="string")

  (options,args) = parse.parse_args()
  if options.ovd !=None:
	link = options.ovd
        YTD_1v(link)
  elif options.plyls:
        playlistURL = options.plyls
        plyre(playlistURL)
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
