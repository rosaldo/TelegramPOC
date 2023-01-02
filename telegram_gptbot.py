#!/usr/bin/env python3
# coding: utf-8

import openai
import telegram as tg
from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater

from config import ChatGPT


class ChatBotGPT:
    version = "1.0.0"
    token = ChatGPT.token
    openai.api_key = ChatGPT.api_key

    def __init__(self):
        up = Updater(self.token, use_context=True)
        dp = up.dispatcher
        dp.add_handler(MessageHandler(Filters.all, self.chat), 0)
        up.start_polling()

    def typing(self, update: Update, context: CallbackContext):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=tg.ChatAction.TYPING)

    def chat(self, update: Update, context: CallbackContext):
        self.typing(update, context)
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=update.message.text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        update.message.reply_text(
            message.strip(),
            parse_mode=tg.ParseMode.HTML,
        )


chat_bot = ChatBotGPT()
