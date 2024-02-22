import asyncio
import json
import logging

from pyrogram import Client, filters
from pyrogram.errors import BadRequest

logging.basicConfig(level=logging.INFO)

# Initialize the Pyrogram client
client = Client("currency-exchange-bot")

# Exchange rates API URL
API_URL = "https://api.exchangerate-api.com/v4/latest"

# Supported currencies
SUPPORTED_CURRENCIES = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"]

# Start the bot
#@client.on_message(filters.command("start"))
#async def start_command(client, message):
   # await message.reply_text("Hi! I'm a currency exchange bot. You can use me to convert currencies.")

# Handle currency exchange requests
@Client.on_message(filters.text & filters.regex(r"^/exchange (.+) to (.+)$"))
async def exchange_command(client, message):
    # Extract the currencies from the message text
    currencies = message.text.split("to")
    from_currency, to_currency = currencies[0].strip(), currencies[1].strip()

    # Check if the currencies are supported
    if from_currency not in SUPPORTED_CURRENCIES or to_currency not in SUPPORTED_CURRENCIES:
        await message.reply_text("Sorry, I don't support those currencies.")
        return

    # Fetch the exchange rate from the API
    try:
        async with client.get(API_URL, params={"base": from_currency}) as response:
            data = json.loads(await response.text())
    except BadRequest:
        await message.reply_text("Sorry, there was a problem fetching the exchange rate.")
        return

    # Calculate the exchange amount
    exchange_rate = data["rates"][to_currency]
    amount = float(message.text.split(" ")[1])
    converted_amount = amount * exchange_rate

    # Send the exchange result to the user
    await message.reply_text(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

# Run the bot
#if __name__ == "__main__":
   # client.run()
