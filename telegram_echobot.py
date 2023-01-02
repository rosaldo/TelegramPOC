#!/usr/bin/env python3
# coding: utf-8

import telegram as tg
from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater

from config import EchoBot


class TEchoBot:
    version = "1.0.0"
    token = EchoBot.token

    def __init__(self):
        up = Updater(self.token, use_context=True)
        dp = up.dispatcher
        dp.add_handler(MessageHandler(Filters.all, self.echo), 0)
        up.start_polling()

    def typing(self, update: Update, context: CallbackContext):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=tg.ChatAction.TYPING)

    def echo(self, update: Update, context: CallbackContext):
        self.typing(update, context)
        update.message.reply_text(
            update.message.text,
            parse_mode=tg.ParseMode.HTML,
        )


echo_bot = TEchoBot()
