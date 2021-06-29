import discord
import requests
from discord.ext import commands,tasks
from PIL import Image, ImageFont, ImageDraw

class Necsa(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("Bot is online")

	@commands.Cog.listener()
	async def on_message(self, message):
	    if message.channel.name == "bot-testing":
	      if message.author == self.user:
	        return

	      lower_msg = message.content.lower()

	      is_nsfw = warden.nsfwCheck(lower_msg)
	      if is_nsfw:
	          censored_message = warden.censorMessage(lower_msg)
	          await message.delete()
	          await message.channel.send(f"""Here's a censored version of {message.author.mention}'s message: {censored_message}""")

	def customizer(self, pngImage, font, fontSize, pfpURL, memberCount, memberUsername):
	    img = Image.open(pngImage)
	    W, H = (img.width, img.height)
	    
	    pfp = Image.open(requests.get(pfpURL, stream=True).raw)
	    basewidth = 190
	    wpercent = (basewidth/float(pfp.size[0]))
	    hsize = int((float(pfp.size[1])*float(wpercent)))
	    pfp = pfp.resize((basewidth,hsize), Image.ANTIALIAS)
	    w1, h1 = pfp.size
	    img.paste(pfp, (int((W-w1)/2), int((H-h1)/2 - 90)))
	    
	    font = ImageFont.truetype(font, fontSize)
	    text = "Welcome!, @"+memberUsername
	    draw = ImageDraw.Draw(img)
	    w, h = draw.textsize(text, font=font)
	    draw.text(((W-w)/2, 80+(H-h)/2), text, (255, 255, 255), font=font)
	    
	    font = ImageFont.truetype("Aileron-ThinItalic.otf", 50)
	    text = "Member #"+str(memberCount)
	    w, h = draw.textsize(text, font=font)
	    draw.text(((W-w)/2, 170+(H-h)/2), text, (255, 255, 255), font=font)
	    img.save("text.png")

	@commands.Cog.listener()
	async def on_member_join(self, member):
	    
	  #ASSIGNS COMMUNITY ROLE TO NEWCOMERS 
	  # role = discord.utils.get(self.guilds[0].roles, name = "Community")
	  # await member.add_roles(role)
	  # print(member.name)

	  #WELCOMES WITH A WELCOME CARD 
	  channel = member.guild.system_channel
	  self.customizer("background.png", "Aileron-Regular.otf", 60, member.avatar_url, member.guild.member_count, member.name)
	  await channel.send(f"""Welcome to Our Server!, {member.mention}""")
	  await channel.send(file=discord.File("text.png"))

def setup(client):
	client.add_cog(Necsa(client))
