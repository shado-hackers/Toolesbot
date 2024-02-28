from pyrogram import Client
import requests as req
from plugins.info import head, ibase_url
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums

API='https://ifsc.razorpay.com/' 
head="**Detailed InFo**\n...................\n\n"
 

@Client.on_message(filters.command("ifsc"))
async def ifsc_data(client: Client, message):
    
    query = message.text.upper()
    try:
        url_request = req.get(API + query)
        url_json = url_request.json()

        # datas
        swift = 'Swift :   ' + str(url_json['SWIFT']) + '\n'
        city = 'City :   ' + str(url_json['CITY']) + '\n'
        upi = 'UPI :   ' + str(url_json['UPI']) + '\n'
        iso = 'ISO3166 :   ' + str(url_json['ISO3166']) + '\n'
        neft = 'NEFT :   ' + str(url_json['NEFT']) + '\n'
        imps = 'IMPS :   ' + str(url_json['IMPS']) + '\n'
        rtgs = 'RTGS :   ' + str(url_json['RTGS']) + '\n'
        centre = 'Centre :   ' + str(url_json['CENTRE']) + '\n'
        address = 'Address :   ' + str(url_json['ADDRESS']) + '\n\n'
        branch = 'Branch :   ' + str(url_json['BRANCH']) + '\n'
        micr = 'MICR :   ' + str(url_json['MICR']) + '\n'
        contact = 'Contact :   ' + str(url_json['CONTACT']) + '\n'
        dist = 'District :   ' + str(url_json['DISTRICT']) + '\n'
        state = 'State :   ' + str(url_json['STATE']) + '\n'
        bank = 'Bank :   ' + str(url_json['BANK']) + '\n'
        bankcd = 'Bank Code :   ' + str(url_json['BANKCODE']) + '\n'
        ifsc = 'IFSC :   ' + str(url_json['IFSC']) + '\n'

         result = head + '' + bank + bankcd + ifsc + micr + state + dist + city + branch + address + contact + upi + iso + neft + imps + rtgs + swift + ''

        await m.edit_text(result, parse_mode=enums.ParseMode.HTML)
    except Exception as e:
        await message.reply("Sorry ,'"+query+"' is Invalid IFSC Code 😕")
        await message.reply("if you're facing a error or else ping @shado_hackers 🤝")
