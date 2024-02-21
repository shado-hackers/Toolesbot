import requests as req
from pyrogram import *
from Config import MAPI_KEY,credsurl

base_url='https://api.macaddress.io/v1?apiKey='
search_query='&output=json&search='






@bot.on_message(filters.text)
async def mac_query(client,message):
    credit=credsurl+MAPI_KEY
    cred_res=req.get(credit)
    cred_js=cred_res.json()
        
    
    mac_id=message.text
    url=base_url+MAPI_KEY+search_query+mac_id
    mac=req.get(url)

    mac_js=mac.json()


    oui=str(mac_js['vendorDetails']['oui'])
    ispriv=str(mac_js['vendorDetails']['isPrivate'])
    company=str(mac_js['vendorDetails']['companyName'])
    companyaddr=str(mac_js['vendorDetails']['companyAddress'])
    countrycode=str(mac_js['vendorDetails']['countryCode'])

    blockfound=str(mac_js['blockDetails']['blockFound'])
    borderlft=str(mac_js['blockDetails']['borderLeft'])
    borderrght=str(mac_js['blockDetails']['borderRight'])
    blocksize=str(mac_js['blockDetails']['blockSize'])
    assignment=str(mac_js['blockDetails']['assignmentBlockSize'])
    datecrtd=str(mac_js['blockDetails']['dateCreated'])
    dateupdated=str(mac_js['blockDetails']['dateUpdated'])

    searchtrm=str(mac_js['macAddressDetails']['searchTerm'])
    isvalid=str(mac_js['macAddressDetails']['isValid'])
    virtualmcn=str(mac_js['macAddressDetails']['virtualMachine'])
    app=str(mac_js['macAddressDetails']['applications'])
    transtype=str(mac_js['macAddressDetails']['transmissionType'])
    admtype=str(mac_js['macAddressDetails']['administrationType'])
    wireshrknts=str(mac_js['macAddressDetails']['wiresharkNotes'])
    comment=str(mac_js['macAddressDetails']['comment'])

    mac_vendor="\n\n**Vendor Data's**\n\n\n```OUI : "+oui+"\nIsPrivate : "+ispriv+"\nCompany Name : "+company+"\nCompanyAddress : "+companyaddr+"\nCountry Code : "+countrycode
    mac_blockdt="```\n\n**Block Details**\n\n\n```BlockFound : "+blockfound+"\nBorderLeft : "+borderlft+"\nBorderRight : "+borderrght+"\nBlockSize : "+blocksize+"\nAssignment BlockSize : "+assignment+"\nDate Created : "+datecrtd+"\nDate Updated : "+dateupdated
    mac_data="```\n\n**MAC Address Details**\n\n\n```SearchTerm : "+searchtrm+"\nIsValid : "+isvalid+"\nVirtual Machine : "+virtualmcn+"\Application's : "+app+"\nTransmission Type : "+transtype+"\nAdministration Type : "+admtype+"\nWireshark Notes : "+wireshrknts+"\nComment : "+comment+'```'
    credit_result="**Free Plan**\n\n`Total Credits : 100/month`\n`Available Credits : "+str(cred_js)+'`'
    await message.reply(credit_result)
    await message.reply(mac_vendor+mac_blockdt+mac_data)
    await message.reply('[Developer](https://t.me/riz4d)')

