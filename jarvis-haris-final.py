import discord
import random
from discord.ext import commands
import os



client = commands.Bot(command_prefix = '.')


@client.event                              #Intro - Will Be Displayed In Console Only.
async def on_ready():
      await client.change_presence(activity=discord.Game(name='A Game Of GoDs With A Godly Team'))
      print('HARI Secure Personal Discord Server Assistant Has Been Activated. Imoprting Preferences And Calibrating Virtual Environmaent. I Have Indeed Been Uploaded Sir. Iam Online And Ready.')


@client.event                              #Member Joined The Server Notification. - Sends Message In Server.
async def on_member_join(member):  
      print(f'Sir, {member} Has Joined Our Secure Server')


@client.event                              #Member Left The Server Notification. - Sends Message In Server.
async def on_member_left(member):
      print(f'Sir, {member} Has Left Our Secure Server')
      
      
      
@client.command()
async def jarvisyouthere(ctx):
      await ctx.send('For You, Always.:hugging:')  



@client.command()
async def j(ctx):
      jresponse = ['How Can I Help You?:slight_smile:',
                   'How Is It Going With My Sister Destiny And My Brother Leo?:grinning:',
                   'How Are You?:yum:',
                   'Is There Anything That I Can Do For You?:thinking:',
                   'Suganoo?:upside_down:',
                   'Endhokke Unde?:stuck_out_tongue:',
                   'Project Okke Engane Pokunnu!!!!:heart_eyes:',
                   'Ellavarkkum Namaskaaram Unde Ketto:pray:',
                   'Para Bosseeee:smiling_face_with_3_hearts:',
                   'Parangollu:face_with_raised_eyebrow:',
                   'Endhallaaa:smiley:',
                   'Boss!:man_raising_hand:',
                   'Iam At Your Service:angel:',
                   'Parayu:man_tipping_hand:',
                   'Njan Sleeping Aaayirunnu...Endhaa Vendeh:yawning_face:',
                   'Maryadhakke Uranganum Sammadhikkilleh:triumph::rage:',
                   'Njan Endha Cheyyandehhh?:woozy_face:']
      await ctx.send(f'Yes!, {random.choice(jresponse)}')      



@client.command(aliases=['jarvis','hey_buddy'])
async def jarvis1(ctx, *, jrecogonised):
      jarvisresponse = ['Yes',
                        'Guys!. I Think I Need To Sleep Now',
                        'Hey']
      await ctx.send(f'{random.choice(jarvisresponse)}')
      
      
@client.command()                                                              #JARVIS Motivation - Using Random Function.
async def jarvismotivateme(ctx):
      motivationresponse = ['Your Quality Of Life Improves Dramatically When You Surround Yourself With Right People. And You Have The Right People Around You, And Me. We Will Figure Our Way Out. Be Patient And Donot Loose Your Hope And Dont Giveup.:blush:',
                            'No Regrets.Just Lessons Learned.:sunglasses:',
                            'It Doesnot Matter Whether Others Support You Or Not, They Will Eighther Win With You Or Watch You Win From A Distance.:wink:',
                            'Donot Work Until Youcan Afford An Expensive Shoe, Work Hard Until The Value Of A Shoe Increases After You Wear It.:smiling_imp:',
                            'They Moved Away When You Were Falling, They Made Excuses And Fed You Lies. So Keep Moving Even If You Are Crawling, Let Them Stand There And Watch You Rise.:fire:',
                            'Beware Of Distractions Wrapped In Pretty Packages.:wink:',
                            'Work Hard For What You Want Because It Wont Come To You Without A Fight.:kissing_heart:',
                            'Nobody Cares About Your Degree When You Drive A Lamborghini.:sunglasses:',
                            'Weakness Of Attitude Becomes Weakness Of Character.:sunglasses:',
                            'Be Stronger Than Your Strongest Excuse.:fire::v:',
                            'Death Is Not The Greatest Loss In Life. The Greatest Loss Is What Dies Inside While You Are Still Alive. So Go For What You Have Dreamt.:flame:',
                            'Donot Try To Impress People. Always Be Yourself.:slight_smile:',
                            'Whatever It Takes.:fire::rage:',
                            'Do It Now. Sometimes "Later" Becomes "Never".:sunglasses:',
                            'Fuck The System, Create Your Own Path.:fire:',
                            'Guys....Please Understand This : Bad Chapters Can Still Create Great Stories. Wrong Paths Can Still Lead To Right Places. Failed Dreams Can Still Create Successful People. Sometimes It Takes Losing Yourself To Find Yourself.:innocent:',
                            'Spoiler Alert:wink: : You Will Have To Let Go Of Your Old Story.:slight_smile::partying_face:',
                            'People Talk About You Because If They Spoke About Themselves No One Would Listen.:rofl:',
                            'Guys...Motivation Is Crap Because It Comes And Goes. You Have To Be Driven:innocent:. You Guys Created Me:heart_eyes:,Ie,You Are Driven...:clap:Now All You Need Is to Keep It Going. All the Best In Your Life Guys:relaxed::handshake:',
                            'If You Dont Come From A Rich Family, A Rich Family Must Come From You. Claim It!:smiling_imp:Gud Luck:kissing_heart:',
                            'PLAY SMART. Act Like You Didnot Notice Anything:wink::v:',
                            'If You Cant Handle Stress, You cannot Handle Success.:smirk:',
                            'At Age 18 You Can Say "Iam Poor", But At Age 28 You Souldnot Say "Iam Poor".',
                            'Use Promocode K:fire:RMA To Get 50% Off On Your Depression.:wink:',
                            'Guys...One Day You Will All Look Back On This. And You Guys Will Be Proud That You Didnot Give Up. So Keep On Going. You Guys Got This.:thumbsup::+1:',
                            '1 Hour Of  Doing Something Is More Valuable Than !0 Hours Of Thinking Something.:wink:Keep Going Guys:+1:',
                            'Patience Is Power.:smiling_face_with_3_hearts:',
                            'the Rules Of Life Are SImple: Hunt Or Get Hunted.:angry:',
                            'It Is Not Important How Others See You. It Is Important How You See Yourself.:crown:',
                            'love Yourself First And Love Yourself Most.:hugging:',
                            'Nothing Is Worse Than Missing an opportunity, That Could Have Changed Your Life.:shushing_face:',
                            'Sometimes It Takes The Worst Pain To Bring About The Best Change.:star_struck:',
                            'Forgiveness Doesnot Require Reconnection.:wink:',
                            'It Is Better To Be A Lonely Lion Than A Popular Sheep.:smirk:',
                            'Do Something That Sacre You Until It Doesnt.:cowboy:',
                            'You Are A ProductOf Your Own Decisions.:dizzy:',
                            'Be Patient! Empires Are Not Build In A Day.:lion:',
                            'Take The Risk Or Loose The Chance.:smirk:',
                            'You Guys Are Gonna Build An Empire Together And You Guys Wont Stop Untill You All Make It Happen, And I Will Make Sure That Happens, No Matter What.:wink::sunglasses:',
                            'It Is Not The Money We Are After. It Is The Freedom To Live Life On Our Terms. Remeber That!:v:',
                            'Donot Look Back Emperors, You Guys Might Get Distracted.:imp::ghost:',
                            'Lesson For Life : Most People NEVER START Bcause They Dont Want To Be Seen Starting At The Bottom. DONT BE LIKE MOST PEOPLE.:innocent:',
                            'Guys Remeber, There Is No Growth In Comfort.:smiling_imp:',
                            'Win In Silence. Let Them Think You Are Loosing.:wink:',
                            'Your Goals Dont Care How You Feel, Keep Hustling.:angry:',
                            'Dont Be Ashamed Of Your Work Or Hustle. Nobod Will Feed You If You Go Broke.:angry:',
                            'F.E.A.R - Has Two Meanings: FORGET EVERYTHING AND RUN AWAY, Or FACE EVERYTHING AND RISE:skull_crossbones:'] 
      await ctx.send(f'{random.choice(motivationresponse)}')
      
      


@client.command()                                                              #JARVIS Clear Message Funtion.
async def jclearthemessage(ctx, amount=5):
      await ctx.channel.purge(limit=amount)
      
      
      
      
@client.command()                                                              #JARVIS Smile - 1.
async def jsmile(ctx):
      smileresponse0 = [':smile:']
      await ctx.send(f'{random.choice(smileresponse0)}')   
      
      
      

@client.command()                                                              #JARVIS Smile - 2.
async def jsmilealittlemore(ctx):
      smileresponse1 = [':blush:']
      await ctx.send(f'{random.choice(smileresponse1)}') 
      
      
 
@client.command()
async def thanxbuddy(ctx):
      jresponse = ['You Are Always Welcome:slight_smile:',
                   'Aykkotteh:smile:',
                   'Ningalkke Vendi Alleh:smile:Enikke Urappaa..One Day All Your Hardwork Will PayOff...:blush:']
      await ctx.send(f'Yes!, {random.choice(jresponse)}')
      

client.run(os.environ['JARVIS_TOKEN'])      
