import json
import os
import requests
from telegram import Bot
from bs4 import BeautifulSoup
import asyncio

# Telegram bot token
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_IDS_FILE = "/PATH/TO/chat_ids.json"
RESIDENCE_DATA_FILE = "/PATH/TO/residence_data.json"
CROUS_URL = "https://trouverunlogement.lescrous.fr/tools/41/search?bounds=7.6881371_48.6461896_7.8360646_48.491861"
# Function to scrape CROUS listings
def scrape_residences():
    response = requests.get(CROUS_URL)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return {}

    soup = BeautifulSoup(response.text, 'html.parser')
    listings = soup.find_all('li', class_='fr-col-12')

    residence_counts = {}

    for listing in listings:
        title_element = listing.find('h3', class_='fr-card__title')
        if title_element:
            title = title_element.text.strip()
            residence_counts[title] = residence_counts.get(title, 0) + 1

    with open(RESIDENCE_DATA_FILE, "w") as file:
        json.dump(residence_counts, file)

    return residence_counts

# Function to build the update message
def build_update_message():
    if os.path.exists(RESIDENCE_DATA_FILE):
        with open(RESIDENCE_DATA_FILE, "r") as file:
            residence_data = json.load(file)
    else:
        residence_data = {}

    total_houses = sum(residence_data.values())
    message = "🏠 *Mises à jour des résidences CROUS Nancy :*\n"
    message += f"🔢 *Nombre total de logements disponibles : {total_houses}*\n\n"

    for residence, count in residence_data.items():
        message += f"🔹 {residence}: {count} logement(s) disponible(s)\n"

    message += f"\n🔗 [Consultez les logements ici]({CROUS_URL})"
    return message

# Asynchronous function to send updates
async def send_updates():
    scrape_residences()  # Scrape data
    message = build_update_message()  # Build message

    if os.path.exists(CHAT_IDS_FILE):
        with open(CHAT_IDS_FILE, "r") as file:
            chat_ids = json.load(file)
    else:
        chat_ids = []

    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    for chat_id in chat_ids:
        try:
            await bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
        except Exception as e:
            if "Forbidden" in str(e):
                print(f"User {chat_id} blocked the bot. Removing from list.")
                chat_ids.remove(chat_id)

    # Save updated chat IDs
    with open(CHAT_IDS_FILE, "w") as file:
        json.dump(chat_ids, file)

# Entry point for the script
if __name__ == '__main__':
    asyncio.run(send_updates())