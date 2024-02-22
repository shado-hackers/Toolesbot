import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

# Create a Pyrogram client.
#client = Client("my_bot", api_id=123456, api_hash="0123456789abcdef")

# Define the command handler.
@client.on_message(filters.command("ifsc"))
async def ifsc_handler(client: Client, message: Message):
    # Get the IFSC code from the message.
    ifsc_code = message.text.split()[1]

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

# Start the bot.
