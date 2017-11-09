# I M P O R T S
import discord
import time
import asyncio
import os
import random
import redis

TOKEN = 'MzY2OTg4Njc2ODYyODM2NzM3.DOAPNw.ytLoZYWUGQjzb0qxbXd-08t4qMM'

link = discord.Client()

# B O T
class l1nk():

    red = redis.Redis.from_url('redis://localhost')

    global user_info
    user_info = {}

    # S T A R T   U P
    @link.event
    async def on_ready():
        print('Online.')
        print('------')
        print(link.user.name)
        print('------')
        print(link.user.id)
        print('------')
        euab = await link.get_user_info('337333673781100545')
        euabdm = await link.start_private_message(euab)

    # C O M M A N D S

    @link.event
    async def on_message(message):

        # H I
        if message.content.startswith('/hi'):
            await link.send_message(message.channel, 'Hello there.')
            await link.send_message(message.channel, 'How are **you**?')
            await link.wait_for_message(author=message.author, content=None)
            await link.send_message(message.channel, "That's **nice**.")

        # Y T
        if message.content.startswith('/yt'):
            args = message.content[4:]
            url = ('https://www.youtube.com/results?search_{}').format(
                                                                urlencode({'query' : ' '.join(args)}
            ))
            await link.send_message(message.channel, 'Here are your search **results.** Enjoy. :thumbsup: :ok_hand:' + '-> ' + url + ' <-')

        # C L E A R
        if message.content.startswith('/clear'):
            chan = message.channel
            numb = message.content[:7]
            await link.send_message(message.channel, 'Are you **sure?**')
            aa = await link.wait_for_message(author=message.author, content=None)
            if (aa.content == 'yes'):
                cll = await link.purge_from(chan,
                                         limit = 1000,
                                         check = None)
                time.sleep(1)
                rr = await link.send_message(message.channel, '`Right. I deleted {} messages.` :ok_hand:'.format(len(cll)))
                time.sleep(1)
                await link.delete_message(rr)
            if (aa.content == 'no'):
                await link.send_message(message.channel, 'Ok. I will **not** clear.')

        # B U G
        if message.content.startswith('/bug'):
            with open('./bugs/reported-bugs.txt', 'a') as rb:
                bugg = message.content[5:]
                print ('Bug: ' + bugg)
                print ('Bug: ' + bugg, file=rb)
                await link.send_message(message.channel, '**Thank you** for reporting an __**error!**__ :thumbsup:')

        # L 1 N K   S T A T   C O M M A N D S

        # A C C O U N T
        if message.content.startswith('/account'):
            if os.path.exists('./accounts/{}.account'.format(message.author.discriminator)):
                with open('./accounts/{}.account'.format(message.author.discriminator), 'r') as accountr:
                    ar = accountr.read()
                    await link.send_message(message.channel, ar)
            if not os.path.exists('./accounts/{}.account'.format(message.author.discriminator)):
                await link.send_message(message.channel, "You do **not** have an account. Would you like to create one?")
                lswfm = await link.wait_for_message(author=message.author, content=None)
                lswfmc = lswfm.content
                if (lswfmc == 'yes'):
                    with open('./accounts/{}.account'.format(message.author.discriminator), 'w') as accountw:
                        print('L 1 N K   S T A T', file=accountw)
                        with open('./accounts/{}.account'.format(message.author.discriminator), 'a') as account1:
                            print('', file=account1)
                            print("{}'s Account:".format(message.author.name), file=account1)
                            print('', file=account1)
                            await link.send_message(message.channel, 'Your **account** has been made.')
                            member = await link.get_user_info(message.author.id)
                        user_info.append('{"{}".format(member.name): os.urandom(15)}')
                        with open('./userinfo/ids.txt', 'w') as ids:
                            print(user_info, file=ids)
                        await link.send_message(message.channel, 'Your **account** has been made.')
                if (lswfmc == 'no'):
                    await link.send_message(message.channel, 'Ok.')

        # S I G N   U P
        if message.content.startswith('/signup'):
            with open('./accounts/{}.account'.format(message.author.discriminator), 'a') as accountw:
                print('L 1 N K   S T A T', file=accountw)
                print('', file=accountw)
                print("{}'s Account:".format(message.author.name), file=accountw)
                print('', file=accountw)
                member = await link.get_user_info(message.author.id)
                user_info.append('{"{}".format(member.name): os.urandom(15)}')
                with open('./userinfo/ids.txt', 'w') as ids:
                    print(user_info, file=ids)
                await link.send_message(message.channel, 'Your **account** has been made.')

        # A D M I N

        # K I C K
        if message.content.startswith('/kick'):
            mauthor = message.author.server.get_member(message.author.id)
            if (mauthor == message.server.owner):
                kickmember = message.mentions[0]
                await link.kick(kickmember)
                await link.send_message(message.channel, '{} has been **kicked!** I hope it was **rational.**'.format(kickmember.name))
            if not (mauthor == message.server.owner):
                await link.send_message(message.channel, "You silly **prick.** You **don't** have **sufficient permissions.**")

        # G O O D B Y E
        if message.content.startswith('/goodbye'):
            allowed = ['292556142952054794']
            if (message.author.id in allowed):
                mess1 = await link.send_message(message.channel, ":wave: **Adios boss!** :wave:")
                mess2 = await link.send_message(message.channel, "**Connection closed.**")
                time.sleep(0.5)
                await link.delete_message(mess1)
                await link.delete_message(mess2)
                await link.logout()
            if not (message.author.id in allowed):
                await link.send_message(message.channel, ":middle_finger: You are the biggest **prick.** Don't **even** try. :middle_finger:")

        # U S E L E S S   C O M M A N D S
        if message.content.startswith('/mcount'):
            await link.send_message(message.channel, 'There is **currently** {} members on **{}**.'.format(message.server.member_count, message.server.name))

        # I N F O
        global gay
        gay = ['239674070885597185', '308727872561086476'];

        if message.content.lower().startswith('/info'):
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]

            userembed = discord.Embed(
                title = "Username:",
                description = user.name,
                color = 0x228b22,
            )

            userembed.set_author(
                name = "Stuff About {}:".format(user.name)
            )

            userembed.add_field(
                name = "Joined at:".format(message.server.name),
                value = userjoinedat
            )

            userembed.add_field(
                name = "{} was born at:".format(user.name),
                value = usercreatedat
            )

            userembed.add_field(
                name = "{}'s Discriminator".format(user.name),
                value = user.discriminator
            )

            userembed.add_field(
                name = "{}'s ID".format(user.name),
                value = user.id
            )

            userembed.add_field(
                name="Status:",
                value = user.status

            )

            if user.id in gay:
                userembed.add_field(
                    name="Is gay:",
                    value = '__**Very.**__'
                )
            else:
                userembed.add_field(
                    name="Is gay:",
                    value = 'No.'
                )

            await link.send_message(message.channel, embed = userembed)

        # S E X U A L I T Y
        if message.content.lower().startswith('/sexuality'):
            sexuality = message.content[11:]
            if sexuality.lower() == 'gay':
                pass

        # N E W S L E T T E R
        Admins = ['292556142952054794']
        subs = ['292556142952054794', '337333673781100545']
        if message.content.startswith('/newsl') and message.author.id in Admins:
            dm = await link.start_private_message(message.author)
            await link.send_message(dm, 'What will the **news** be?')
            news = await link.wait_for_message(author=message.author, channel=dm)
            await link.send_message(dm, 'The **news** has been **announced.**')
            for peepz in subs:
                peep = await link.get_user_info(peepz)
                peepdm = await link.start_private_message(peep)
                await link.send_message(peepdm, news.content)





link.run(TOKEN)
