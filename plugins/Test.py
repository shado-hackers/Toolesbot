import pyrogram
from pyrogram import Client, filters
import requests

# Initialize the Pyrogram client
#app = Client("drug_info_bot")

# Define the command handler for "/drug_info" command
@Client.on_message(filters.command("druginfo"))
def drug_info_handler(client, message):
    # Extract the drug name from the message
    drug_name = message.text.split(" ")[1]

    # Send a request to the DrugBank API to get information about the drug
    response = requests.get(f"https://www.drugbank.ca/api/v2/drugs/{drug_name}")

    # Check if the request was successful
    if response.status_code != 200:
        message.reply_text("Sorry, I couldn't find any information about that drug.")
        return

    # Parse the JSON response
    data = response.json()

    # Extract the relevant information from the JSON response
    drug_info = f"{data['name']}\n\n"
    drug_info += f"CAS Number: {data['cas_number']}\n"
    drug_info += f"Description: {data['description']}\n"
    drug_info += f"Drug Interactions: {data['drug_interactions']}\n"
    drug_info += f"Side Effects: {data['side_effects']}\n"
    drug_info += f"Dosage: {data['dosage']}\n"

    # Send the drug information to the user
    message.reply_text(drug_info)

# Run the bot
