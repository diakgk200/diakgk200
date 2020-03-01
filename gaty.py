import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import asyncio
import requests
import random

TOKEN = 'Njc3NDQyMjMxMDAyNzI2NDQw.XldXdA.a3hCaX49kDb9anMdPjC82H_j3Sw'
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("========== Server Start ==========")
    print("Client Name: " + client.user.name)
    print("Client ID: " + str(client.user.id))
    print("==================================")
    print("\n")


async def prescence():
    await client.wait_until_ready()
    lists = ["Type to '.help'"]

    while not client.is_closed():
        status = random.choice(lists)

        await client.change_presence(activity=discord.Game(status))
        await asyncio.sleep(3)

@client.command()
async def search(ctx):
    baseUrl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=post&query='
    plusUrl = input("검색어를 입력하세요: ")
    url = baseUrl + urllib.parse.quote_plus(plusUrl)

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find_all(class_='sh_blog_title')

    for i in title:
        await ctx.send(i.attrs['title'])
        await ctx.send(i.attrs['href'])

client.loop.create_task(prescence())
client.run(TOKEN)