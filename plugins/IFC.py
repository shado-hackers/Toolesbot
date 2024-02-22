from pyrogram import *
import requests as req
#from plugins.info import head,ibase_url
from pyrogram import Client as app
from pyrogram import filters
import urllib3

urllib3.disable_warnings()


API = "https://ifsc.rizad.me/?ifsc="
head="**Detailed InFo**\n...................\n\n"

@app.on_message(filters.command("ifsc"))
async def ifsc_data(client,message):
    
   query=message.text.upper()
   try:
    http = urllib3.PoolManager()
    url_request=requests.get( API+query)
    url_json=url_request.data.decode('utf-8')
    url_json=json.loads(url_json)
    
    #datas
    swift='Swift :   '+str(url_json['SWIFT'])+'\n'
    city='City :   '+str(url_json['CITY'])+'\n'
    upi='UPI :   '+str(url_json['UPI'])+'\n'
    iso='ISO3166 :   '+str(url_json['ISO3166'])+'\n'
    neft='NEFT :   '+str(url_json['NEFT'])+'\n'
    imps='IMPS :   '+str(url_json['IMPS'])+'\n'
    rtgs='RTGS :   '+str(url_json['RTGS'])+'\n'
    centre='Centre :   '+str(url_json['CENTRE'])+'\n'
    address='Address :   '+str(url_json['ADDRESS'])+'\n\n'
    branch='Branch :   '+str(url_json['BRANCH'])+'\n'
    micr='MICR :   '+str(url_json['MICR'])+'\n'
    contact='Contact :   '+str(url_json['CONTACT'])+'\n'
    dist='District :   '+str(url_json['DISTRICT'])+'\n'
    state='State :   '+str(url_json['STATE'])+'\n'
    bank='Bank :   '+str(url_json['BANK'])+'\n'
    bankcd='Bank Code :   '+str(url_json['BANKCODE'])+'\n'
    ifsc='IFSC :   '+str(url_json['IFSC'])+'\n'
    
    result=head+''+bank+bankcd+ifsc+micr+state+dist+city+branch+address+contact+upi+iso+neft+imps+rtgs+swift+''
        
    await message.reply(result)
   except:
       await message.reply("Sorry ,'"+query+"' is Invalid IFSC Code 😕")
       await message.reply("if you're facing a error or else ping @shado_hackers 🤝")
