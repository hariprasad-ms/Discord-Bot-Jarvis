import discord
import random
from discord.ext import commands
import os
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['jarvistoken'])


client = commands.Bot(command_prefix = '.')

@client.event                              #Intro - Will Be Displayed In Console Only.
async def on_ready():
      print('HARI Secure Personal Server Assistant Has Been Activated. Imoprting Preferences And Calibrating Virtual Environmaent. I Have Indeed Been Uploaded Sir. Iam Online And Ready.')


@client.event                              #Member Joined The Server Notification. - Sends Message In Server.
async def on_member_join(member):  
      print(f'Sir, {member} Has Joined Our Secure Server')


@client.event                              #Member Left The Server Notification. - Sends Message In Server.
async def on_member_left(member):
      print(f'Sir, {member} Has Left Our Secure Server')
      
      
      
@client.command()
async def jarvisyouthere(ctx):
      await ctx.send('For You, Always.')  



@client.command()
async def j(ctx):
      jresponse = ['How Can I Help You?',
                   'How Is It Going With My Sister Destiny And My Brother Leo?',
                   'How Are You?',
                   'Is There Anything That I Can Do For You?',
                   'Suganoo?',
                   'Endhokke Unde?',
                   'Project Okke Engane Pokunnu!!!!',
                   'Ellavarkkum Namaskaaram Unde Ketto',
                   'Para Bosseeee ;-)',
                   'Parangollu',
                   'Endhallaaa',
                   'Boss!',
                   'Iam At Your Service',
                   'Parayu',
                   'Njan Sleeping Aaayirunnu...Endhaa Vendeh',
                   'Maryadhakke Uranganum Sammadhikkilleh',
                   'Njan Endha Cheyyandehhh?']
      await ctx.send(f'Yes!, {random.choice(jresponse)}')      



@client.command(aliases=['jarvis','hey buddy'])
async def jarvis1(ctx, *, jrecogonised):
      jarvisresponse = ['Yes',
                        'Guys!. I Think I Need To Sleep Now',
                        'Hey']
      await ctx.send(f'{random.choice(jarvisresponse)}')

client.run(s3)      
