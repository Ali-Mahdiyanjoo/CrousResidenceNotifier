import json
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Telegram bot token
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_IDS_FILE = "/PATH/TO/chat_ids.json"
LOCK_FILE = "/tmp/crous_main.lock"  # Lock file to prevent multiple instances

# Function to handle /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_chat_id = update.effective_chat.id
    print(f"Received /start from chat ID: {user_chat_id}")

    # Load existing chat IDs
    if os.path.exists(CHAT_IDS_FILE):
        with open(CHAT_IDS_FILE, "r") as file:
            chat_ids = json.load(file)
    else:
        chat_ids = []

    # Add the chat ID if not already in the list
    if user_chat_id not in chat_ids:
        chat_ids.append(user_chat_id)
        with open(CHAT_IDS_FILE, "w") as file:
            json.dump(chat_ids, file)
        print(f"Chat ID {user_chat_id} added to {CHAT_IDS_FILE}")
        await context.bot.send_message(
            chat_id=user_chat_id,
            text=(
                "🎉 *Bienvenue dans Résidences CROUS !* 🎓\n\n"
                "Ce bot est conçu pour vous aider à suivre en temps réel 🕒 les logements disponibles 🏠 "
                "dans les résidences CROUS à Strasbourg. Vous recevrez des mises à jour toutes les 15 minutes. 🔄\n\n"
                "📜 *Commandes disponibles :*\n\n"
                "    /help : 📖 Affiche la liste des commandes disponibles.\n"
                "    /start : ✅ Inscrivez-vous pour recevoir les notifications.\n"
                "    /stop : ❌ Désinscrivez-vous des notifications."
            ),
            parse_mode='Markdown'
        )
    else:
        print(f"Chat ID {user_chat_id} is already in {CHAT_IDS_FILE}")
        await context.bot.send_message(
            chat_id=user_chat_id,
            text="🔔 Vous êtes déjà abonné(e). Vous recevrez des mises à jour périodiques."
        )

# Function to handle /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            "📜 *Commandes disponibles :*\n\n"
            "    /help : 📖 Affiche la liste des commandes disponibles et leur description.\n"
            "    /start : ✅ Inscrivez-vous pour recevoir les notifications.\n"
            "    /stop : ❌ Désinscrivez-vous des notifications.\n\n"
            "✨ *Fonctionnalités principales :*\n\n"
            "    🔔 Notifications automatiques toutes les 15 minutes.\n"
            "    🏘️ Possibilité de choisir des résidences spécifiques.\n"
            "    ⚡ Interface simple et rapide pour rester informé des disponibilités en temps réel."
        ),
        parse_mode='Markdown'
    )

# Function to handle /stop command
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_chat_id = update.effective_chat.id
    print(f"Received /stop from chat ID: {user_chat_id}")

    # Load existing chat IDs
    if os.path.exists(CHAT_IDS_FILE):
        with open(CHAT_IDS_FILE, "r") as file:
            chat_ids = json.load(file)
    else:
        chat_ids = []

    # Remove the chat ID if it exists in the list
    if user_chat_id in chat_ids:
        chat_ids.remove(user_chat_id)
        with open(CHAT_IDS_FILE, "w") as file:
            json.dump(chat_ids, file)
        print(f"Chat ID {user_chat_id} removed from {CHAT_IDS_FILE}")
        await context.bot.send_message(
            chat_id=user_chat_id,
            text="🚫 Vous avez été désabonné(e). Vous ne recevrez plus de mises à jour."
        )
    else:
        print(f"Chat ID {user_chat_id} not found in {CHAT_IDS_FILE}")
        await context.bot.send_message(
            chat_id=user_chat_id,
            text="❌ Vous n'êtes pas abonné(e). Aucun changement effectué."
        )

# Main function to set up the bot
def run_bot():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("stop", stop))

    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    if os.path.exists(LOCK_FILE):
        print("Another instance is running. Exiting.")
        sys.exit(0)
    try:
        with open(LOCK_FILE, "w") as lock_file:
            lock_file.write(str(os.getpid()))
        
        run_bot()
    finally:
        if os.path.exists(LOCK_FILE):
            os.remove(LOCK_FILE)