from pyrogram import Client
import requests as req
from plugins.info import head, ibase_url
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums

API='https://ifsc.razorpay.com/' 
head="Detailed InFo\n...................\n\n"
 

@Client.on_message(filters.command("ifsc"))
async def ifsc_data(_, message: Message):
    ifsc_data = message.text.split(" ", 1)
    if len(ifsc_data) == 1:
        await message.reply_text("Usage:\n/ifsc [ifsc]")
        return
    else:
        ifsc_data = ifsc_data[1]
        m = await message.reply_text("Searching...")
    try:
        url = requests.get(f"https://ifsc.rizad.me/?ifsc={IFSC-CODE}")
        response = json.loads(url.text)
        text = f"""
swift: {response['swift']}
Status: {response['city']}
upi: {response['upi']}
neft: {response['neft']}
iso : {response['iso']}
rtgs: {response['rtgs']}
imps : {response['imps']}
centre: {response['centre']}
address: {response['address']}
branch: {response['branch']}
dist: {response['District']}
State: {response['state']}
Bank: {response['Bank']}"""
           await m.edit_text(text, parse_mode=enums.ParseMode.HTML)
    except Exception as e:
        await m.edit_text("Sorry ,'"+ifsc_data+"' is Invalid IFSC Code 😕")
        await m.edit_text("if you're facing a error or else ping @shado_hackers 🤝")
