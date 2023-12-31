from discord import app_commands, Intents, Client, Interaction
from discord.ext import commands
import random
import discord
import json

with open('config.json','r') as config_file:
    config_data = json.load(config_file)

bot_token = config_data['token']


class Bot(Client):
    def __init__(self, *, intents: Intents) -> None:
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self) -> None:
        return self.tree.sync(guild=None)


bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot running correctly')

@bot.tree.command()
async def givemebadge(interaction: Interaction):
    await interaction.response.send_message("Listo!, espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer")

@bot.command()
async def towers(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        await ctx.send("Invalid round id")
    elif round_length == 36:
        tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16,tower17,tower18,tower19,tower20,tower21,tower22,tower23,tower24 = ":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:"
        a =  random.randint(1,3)
        b =  random.randint(1,3)
        c =  random.randint(1,3)
        d =  random.randint(1,3)
        e =  random.randint(1,3)
        f =  random.randint(1,3)
        g =  random.randint(1,3)
        h =  random.randint(1,3)

        if a == 1:
            tower1 = ":star:"
        elif a == 2:
            tower2 = ":star:"
        elif a == 3:
            tower3 = ":star:"
        if b == 1:
            tower4 = ":star:"
        elif b == 2:
            tower5 = ":star:"
        elif b == 3:
            tower6 = ":star:"
        if c == 1:
            tower7 = ":star:"
        elif c == 2:
            tower8 = ":star:"
        elif c == 3:
            tower9 = ":star:"
        if d == 1:
            tower10 = ":star:"
        elif d == 2:
            tower11 = ":star:"
        elif d == 3:
            tower12 = ":star:"
        if e == 1:
            tower13 = ":star:"
        elif e == 2:
            tower14 = ":star:"
        elif e == 3:
            tower15 = ":star:"
        if f == 1:
            tower16 = ":star:"
        elif f == 2:
            tower17 = ":star:"
        elif f == 3:
            tower18 = ":star:"
        if g == 1:
            tower19 = ":star:"
        elif g == 2:
            tower20 = ":star:"
        elif g == 3:
            tower21 = ":star:"
        if h == 1:
            tower22 = ":star:"
        elif h == 2:
            tower23 = ":star:"
        elif h == 3:
            tower24 = ":star:"

        row1 = tower1 + tower2 + tower3
        row2 = tower4 + tower5 + tower6
        row3 = tower7 + tower8 + tower9
        row4 = tower10 + tower11 + tower12
        row5 = tower13 + tower14 + tower15
        row6 = tower16 + tower17 + tower18
        row7 = tower19 + tower20 + tower21
        row8 = tower22 + tower23 + tower24
    
        info = str(random.randint(45,95))
        pfp = "https://i.imgflip.com/6hz980.png?a466824"
        list = [0xFF0000,0x00FF2E,0x000FFF,0xF700FF]
        color = random.choice(list)
        em = discord.Embed(color=color)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Hecho por Gui")
        em.add_field(name="Towers Predictor",value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7 + "\n" + row8 + "\n" + "**Acierto**" + "\n" + info + "%")
        await ctx.send(embed=em)
        
bot.run(bot_token)                 