# I M P O R T S
import discord
import asyncio

# G L O B A L   V A R I A B L E S
link = discord.Client()

# P L U G I N
class hi():
    async def hi(self, message):
        await self.link.send_message(message.channel, 'Hello. How are **you**?')
        await self.link.wait_for_message(author=message.author, content=None)
        await self.link.send_message(message.channel, "That's" +  '**nice.**')
