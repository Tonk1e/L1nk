# I M P O R T S
import discord
import asyncio
import os

# G L O B A L   V A R I A B L E S
link = discord.Client()

# P L U G I N
class l1nkstat():
    async def account(message):
        if os.path.exists('./Accounts/{}.account'.format(message.author.discriminator)):
            with open('./Accounts/{}.account'.format(message.author.discrimator), 'r') as accountr:
                ar = accountr.read()
                await link.send_message(message.channel, ar)
        if not os.path.exists('./Accounts/{}.account'.format(message.author.discriminator)):
            await link.send_message(message.channel, "You do **not** have an account. Please **create** one with `/signup`")
