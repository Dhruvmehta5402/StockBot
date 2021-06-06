from discord.ext import commands
import random
from bsedata.bse import BSE

b = BSE()
print(b)

b = BSE(update_codes = True)

bot = commands.Bot(command_prefix='!')

@bot.command(name="test")
async def test(ctx):
    await ctx.send("Test successful")
    bluechip = ['TCS', 'Infosys', 'Reliance, M&M, Wipro, Bajaj Companies, MRF']
    recommend = f'Try investing in {random.choice(bluechip)}'
    await ctx.send(recommend)
    await ctx.send("Also check out the some of the Sensex Companies")

@bot.command(name="growth")
async def growth(ctx):
    risky = ['Adani Ent', 'Adani Ports', 'Adani Power', 'Alkyl Amine', 'Navin Fluorine', 'Balaji Amines', 'Apollo Hospital', 'Britannia', 'Titan Company', 'HAL']
    recommend = f'Try investing in {random.choice(risky)}'
    await ctx.send(recommend)
    await ctx.send("Also check out the rest of the Sensex Companies")

@bot.command(name="returns", help="Enter the bought price then the CMP to get Profit%")
async def returns(ctx, x, y):
    x = float(x)
    y = float(y)
    profit = y - x
    percent = (profit / x) * 100
    await ctx.send("Your return on this investment is: " + str(percent) + "%")

@bot.command(name="price", help="Enter the BSE stock code to get the price, change%")
async def returns(ctx, code):
    quote = b.getQuote(code)
    current = quote["currentValue"]
    share = quote["companyName"]
    change_percent = quote["pChange"]
    await ctx.send(share +" : " + str(current))
    await ctx.send("Change % today: " + str(change_percent) + "%")
    await ctx.send("Price updated on: " + quote["updatedOn"])

with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)