import asyncio
import requests
import json
 
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("ifsc"))
async def ifsc_handler(client: Client, message: Message):
    # Check if the message contains an IFSC code.
    if len(message.text) > 1:
        # Get the IFSC code from the message.
        ifsc_code = message.text.split(" ")[1]

        # Make a request to the IFSC API.
        response = await asyncio.get(f"https://ifsc.razorpay.com/{ifsc_code}")

        # Parse the response.
        data = response.json()

        # Format the response.
        response_text = f"""
Bank: {data['BANK']}
Address: {data['ADDRESS']}
City: {data['CITY']}
State: {data['STATE']}
Branch: {data['BRANCH']}
MICR Code: {data['MICR']}
UPI: {data['UPI']}
RTGS: {data['RTGS']}
NEFT: {data['NEFT']}
IMPS: {data['IMPS']}
"""

        # Send the response to the user.
        await message.reply_text(response_text)
    else:
        # If the message does not contain an IFSC code, send an error message.
        await message.reply_text("Please provide an IFSC code.")
 
 
