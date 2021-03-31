import os
from dotenv import load_dotenv, find_dotenv
import discord
from discord.ext import commands as cmds
from WebScraper import WebScraper
from JokeScraper import JokeScraper
import random

# Finds and loads the enviroment variables from the env file
load_dotenv(find_dotenv())


class Bot:

    global bot, token  # bot and token variables
    bot = cmds.Bot(command_prefix='$')
    bot.remove_command('help')
    token = os.getenv('TOKEN')  # Returns the key value of TOKEN

    def __init__(self):
        self.startBot()

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} is connected')

    @bot.command()
    async def yes(ctx):
        await ctx.channel.send("no")

    @bot.command()
    async def professor(ctx, *args):
        name = str(args[0])
        webscraper = WebScraper(name)
        embed = discord.Embed(
            color=discord.Colour.orange()
        )
        if webscraper.tid() == "404-Not Found":
            embed.add_field(name="Error", value="Professor Not Found\n \
                            Please input their correct first and last name")
            await ctx.channel.send(embed=embed)
            return

        embed.set_author(name=webscraper.professorName())
        embed.add_field(name="Professor Description:",
                        value=webscraper.professorDescription(),
                        inline=False)
        embed.add_field(name="Number of Ratings:",
                        value=webscraper.num_of_ratings())
        embed.add_field(name="Overall Rating:",
                        value=webscraper.overall_rating())
        embed.add_field(name="Would Take Again?",
                        value=webscraper.would_take_again())
        embed.add_field(name="Level of Difficulty:",
                        value=webscraper.lvl_of_diff())
        embed.add_field(name="Top Tags:",
                        value='\n'.join(webscraper.top_tags()))
        embed.add_field(name="Top Comment:",
                        value=webscraper.top_comment(),
                        inline=False)
        embed.add_field(name="Link:", value=webscraper.get_link(),
                        inline=False)
        await ctx.channel.send(embed=embed)

    @bot.command()
    async def laugh(ctx):
        JP = JokeScraper()
        jokes = JP.get_jokes()
        joke = str(random.choice(jokes))
        joke_number = jokes.index(joke)
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(name="Here is one...")
        embed.add_field(name="Joke #"+str(joke_number), value=joke)
        await ctx.channel.send(embed=embed)

    @bot.command()
    async def help(ctx):
        embed = discord.Embed(
            color=discord.Colour.green()
        )
        embed.set_author(name='Below are the different commands:')
        embed.add_field(
            name='$laugh', value='Outputs a randomly generated joke', inline=False)
        embed.add_field(name='$professor "Full name"',
                        value='Input: (in quotes) the full name of the professor\n \
                        Output: information on the professor from RateMyProfessor', inline=False)
        await ctx.channel.send(embed=embed)

    def startBot(self):
        bot.run(token)


if __name__ == "__main__":
    bot = Bot()
