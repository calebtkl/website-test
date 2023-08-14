from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import mysql.connector
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
load_dotenv()

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json['text']
    
    # Process the user input and generate the chatbot response
    chatbot_response = handle_response(user_input, 'sample_username')
    
    # Render the HTML file with the chatbot response
    return render_template('chatbot.html')

my_db = mysql.connector.connect(
    host = "cloud.mindsdb.com",
    user = os.environ.get("USER"),
    password = os.environ.get("PASSWORD"),
    port="3306"
)



TOKEN: Final = '6160459115:AAH5MsBe0EA0bdDC7yUx2nMrRPepHbAMiK4'
BOT_USERNAME: Final = '@LegalCodebreakerBot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Im Here to answer any questions that you have!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('If you need more help, please turn to Google or seek other options.')


# Responses

def handle_response(text: str, username:str) -> str:
    user_message = str(text)

    
    cursor = my_db.cursor()
    cursor.execute(f'''SELECT response from mindsdb.testbot5 WHERE author_username = "{username}" AND text="{user_message}" ''')
    for x in cursor:
        formatted_text = str(x).replace("\\n", "\n").strip("(),")
        return formatted_text


async def handle_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text:str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: {text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text:str = text.replace(BOT_USERNAME, '').strip()
            response:str = handle_response(new_text, update.message.chat.username)
        else:
            return
    else:
        response: str = handle_response(text, update.message.chat.username)

    print('Bot:',response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



if __name__ == '__main__':
    print('starting bot...')
    app =Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #errors
    app.add_error_handler(error)

    print('polling started...')
    app.run_polling(poll_interval=1)
