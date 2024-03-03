
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import enums

API_URL = 'https://ifsc.razorpay.com/'
INFO_HEADER = "Detailed Info\n...................\n\n"


@Client.on_message(filters.text & filters.command(["ifsc"]))
async def ifsc_data(client: Client, message: Message):
    query = message.from_user.id

    try:
        response = req.get(API_URL + query)
        json_data = response.json()

        info = INFO_HEADER
        info += f"Bank: {json_data['BANK']}\n"
        info += f"Bank Code: {json_data['BANKCODE']}\n"
        info += f"IFSC: {json_data['IFSC']}\n"
        info += f"MICR: {json_data['MICR']}\n"
        info += f"State: {json_data['STATE']}\n"
        info += f"District: {json_data['DISTRICT']}\n"
        info += f"City: {json_data['CITY']}\n"
        info += f"Branch: {json_data['BRANCH']}\n"
        info += f"Address: {json_data['ADDRESS']}\n"
        info += f"Contact: {json_data['CONTACT']}\n"
        info += f"UPI: {json_data['UPI']}\n"
        info += f"ISO3166: {json_data['ISO3166']}\n"
        info += f"NEFT: {json_data['NEFT']}\n"
        info += f"IMPS: {json_data['IMPS']}\n"
        info += f"RTGS: {json_data['RTGS']}\n"
        info += f"Swift: {json_data['SWIFT']}\n"

        await message.reply(info)
    except Exception as e:
        await message.reply("Invalid IFSC Code 😕")
