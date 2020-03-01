from bs4 import BeautifulSoup
import os
import re
import time
import random
import asyncio
import discord
from discord.ext import commands
import requests
import urllib
import urllib.request
import random
import datetime

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
    lists = ["Type to '.help'", "𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒊𝒏𝒈 𝑯𝒆𝒏𝒕𝒂𝒊♥♥"]

    while not client.is_closed():
        status = random.choice(lists)

        await client.change_presence(activity=discord.Game(status))
        await asyncio.sleep(3)


@client.command()
async def neko(ctx):
    timer = [60, 40, 100]

    while True:
        embed = discord.Embed(
            title="Neko.Life", color=0xFF69B4,
        )
        embed2 = discord.Embed(
            description="Nya~", color=0xFFB6C1,
        )
        embed3 = discord.Embed(
            description="Nya~", color=0xFFE4E1,
        )
        randomnumber = random.randrange(100, 407)
        randomgiho = random.randrange(1, 3)
        print('?번째사진 : ' + str(randomnumber))
        print('기호 : ' + str(randomgiho))
        strandomnumber = str(randomnumber)
        file1 = '.png'
        file2 = '.jpg'
        file3 = '.jpeg'
        giho = '_'
        if randomgiho == 1:
            urlbase1 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file1
            urlbase2 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file2
            urlbase3 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file3
            embed.set_image(url=urlbase1)
            embed2.set_image(url=urlbase2)
            embed3.set_image(url=urlbase3)
            await ctx.send(content=None, embed=embed)
            await ctx.send(content=None, embed=embed2)
            await ctx.send(content=None, embed=embed3)
            await asyncio.sleep(int(random.choice(timer)))
        else:
            urlbase_1 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file1
            urlbase_2 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file2
            urlbase_3 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file3
            embed.set_image(url=urlbase_1)
            embed2.set_image(url=urlbase_2)
            embed3.set_image(url=urlbase_3)
            await ctx.send(content=None, embed=embed)
            await ctx.send(content=None, embed=embed2)
            await ctx.send(content=None, embed=embed3)
            await asyncio.sleep(int(random.choice(timer)))


@client.command()
async def l_neko(ctx):
    timer = [60, 40, 100]

    while True:
        embed = discord.Embed(
            title="Neko.Life", color=0xFF69B4,
        )
        embed2 = discord.Embed(
            description="Nya~", color=0xFFB6C1,
        )
        embed3 = discord.Embed(
            description="Nya~", color=0xFFE4E1,
        )
        randomnumber = random.randrange(100, 407)
        randomgiho = random.randrange(1, 3)
        print('?번째사진 : ' + str(randomnumber))
        print('기호 : ' + str(randomgiho))
        strandomnumber = str(randomnumber)
        file1 = '.png'
        file2 = '.jpg'
        file3 = '.jpeg'
        giho = '_'
        if randomgiho == 1:
            urlbase1 = "https://cdn.nekos.life/lewd/lewd_neko_" + strandomnumber + file1
            urlbase2 = "https://cdn.nekos.life/lewd/lewd_neko_" + strandomnumber + file2
            urlbase3 = "https://cdn.nekos.life/lewd/lewd_neko_" + strandomnumber + file3
            embed.set_image(url=urlbase1)
            embed2.set_image(url=urlbase2)
            embed3.set_image(url=urlbase3)
            await ctx.send(content=None, embed=embed)
            await ctx.send(content=None, embed=embed2)
            await ctx.send(content=None, embed=embed3)
            await asyncio.sleep(int(random.choice(timer)))
        else:
            urlbase_1 = "https://cdn.nekos.life/lewd/lewd_neko" + giho + strandomnumber + file1
            urlbase_2 = "https://cdn.nekos.life/lewd/lewd_neko" + giho + strandomnumber + file2
            urlbase_3 = "https://cdn.nekos.life/lewd/lewd_neko" + giho + strandomnumber + file3
            embed.set_image(url=urlbase_1)
            embed2.set_image(url=urlbase_2)
            embed3.set_image(url=urlbase_3)
            await ctx.send(content=None, embed=embed)
            await ctx.send(content=None, embed=embed2)
            await ctx.send(content=None, embed=embed3)
            await asyncio.sleep(int(random.choice(timer)))



async def anime_pictures():
    await client.wait_until_ready()
    i_channel = client.get_channel(679904288658423867)
    timer = [300, 600, 900]

    while not client.is_closed():
        print("==== animation_pictures_start ====")
        now = time.strftime('%y-%m-%d %H:%M:%S')
        print("======= " + now + " ========")
        print("==================================")

        f = open("./animation_num.txt", 'r')
        lastnum = f.readline()
        f.close()

        l_url = []
        l_d_url = []
        l_num = []

        session = requests.session()
        site = "https://anime-pictures.net/pictures/view_posts/0?lang=en"
        r = session.post(site)
        html = r.text

        soup = BeautifulSoup(html, 'html.parser')
        img = soup.find_all('img', {'class': 'img_cp'})
        res = str(img).split(',')

        # 실제 주소
        p = re.compile(r'[a-z]+_[a-z]+_[a-z]+_\d+')
        data = p.findall(str(res))
        p = re.compile('\d+')
        data = p.findall(str(data))

        # 이미지 다운 주소
        p = re.compile(
            r'cdn.\w+-\w+.\w{3}/\w+_\w+/[a-zA-Z0-9]+/[a-zA-Z0-9]+_cp.png|cdn.\w+-\w+.\w{3}/\w+_\w+/[a-zA-Z0-9]+/[a-zA-Z0-9]+_cp.jpg')
        data1 = p.findall(str(res))

        print("First Number: " + str(data[0]))

        # 이미지 번호 대조
        for lists in range(len(data)):
            print("Last Number: " + str(lastnum))
            print("Image Number: " + str(data[lists]))
            if (str(lastnum) == str(data[lists])):
                print("=========== animation ============")
                now = time.strftime('%y-%m-%d %H:%M:%S')
                print("======= " + now + " ========")
                print("==================================")
                print("\n")
                break
            else:
                print("\n")

            url = "https://anime-pictures.net/pictures/view_post/" + data[lists] + "?lang=en"
            d_url = "http://" + str(data1[lists])

            l_url.insert(0, url)
            l_d_url.insert(0, d_url)
            l_num.insert(0, data[lists])

        # 출력
        for l_list in range(len(l_url)):
            embed = discord.Embed(title="Anime Illust", description="Image number is " + str(l_num[l_list]),
                                  color=0xFF69B4, url=l_url[l_list])
            embed.set_image(url=l_d_url[l_list])
            await i_channel.send(content=None, embed=embed)

        # lastnum 기록
        f = open("./animation_num.txt", 'w')
        f.write(str(data[0]))
        f.close()

        await asyncio.sleep(int(random.choice(timer)))


async def yandere_pictures():
    await client.wait_until_ready()
    i_channel = client.get_channel(679903966070308872)
    timer = [300, 600, 900]

    while not client.is_closed():
        print("===== yandere_pictures_start =====")
        now = time.strftime('%y-%m-%d %H:%M:%S')
        print("======= " + now + " ========")
        print("==================================")

        f = open("./yandere_num.txt", 'r')
        lastnum = f.readline()
        f.close()

        l_url = []
        l_d_url = []
        l_num = []

        session = requests.session()
        site = "https://yande.re"
        r = session.post(site)
        html = r.text

        # 실제 주소-1
        soup = BeautifulSoup(html, 'html.parser')
        img = soup.find_all('span', {'class': 'plid'})
        res = str(img).split(',')

        # 실제 주소-2
        p = re.compile(r'https://yande.re/post/show/\d+')
        data = p.findall(str(res))
        p = re.compile('\d+')
        data = p.findall(str(data))

        # 이미지 다운 주소-1
        soup = BeautifulSoup(html, 'html.parser')
        img = soup.find_all('img', {'class': 'preview'})
        res1 = str(img).split(',')

        # 이미지 다운 주소-2
        p = re.compile(
            r'https://assets.yande.re/data/preview/[a-zA-Z0-9]+/[a-zA-Z0-9]+/[a-zA-Z0-9]+.jpg|https://assets.yande.re/data/preview/[a-zA-Z0-9]+/[a-zA-Z0-9]+/[a-zA-Z0-9]+.png')
        data1 = p.findall(str(res1))

        print("First Number: " + str(data[0]))

        # 이미지 번호 대조
        for lists in range(len(data)):
            print("Last Number: " + str(lastnum))
            print("Image Number: " + str(data[lists]))
            if (str(lastnum) == str(data[lists])):
                print("============ yandere =============")
                now = time.strftime('%y-%m-%d %H:%M:%S')
                print("======= " + now + " ========")
                print("==================================")
                print("\n")
                break
            else:
                print("\n")

            url = "https://yande.re/post/show/" + data[lists]
            d_url = str(data1[lists])

            l_url.insert(0, url)
            l_d_url.insert(0, d_url)
            l_num.insert(0, data[lists])

        # 출력
        for l_list in range(len(l_url)):
            embed = discord.Embed(title="Yande.re", description="Image number is " + str(l_num[l_list]), color=0xFF69B4,
                                  url=l_url[l_list])
            embed.set_image(url=l_d_url[l_list])
            await i_channel.send(content=None, embed=embed)

        # lastnum 기록
        f = open("./yandere_num.txt", 'w')
        f.write(str(data[0]))
        f.close()

        await asyncio.sleep(int(random.choice(timer)))


async def konachan_pictures():
    await client.wait_until_ready()
    i_channel = client.get_channel(677909014545432586)
    timer = [300, 600, 900]

    while not client.is_closed():
        print("===== konachan_pictures_start ====")
        now = time.strftime('%y-%m-%d %H:%M:%S')
        print("======= " + now + " ========")
        print("==================================")
        print("\n")

        f = open("./konachan_num.txt", 'r')
        lastnum = f.readline()
        f.close()

        l_url = []
        l_d_url = []
        l_num = []

        session = requests.session()
        site = "http://konachan.net/post"
        r = session.post(site)
        html = r.text

        soup = BeautifulSoup(html, 'html.parser')
        img = soup.find_all('a', {'class': 'thumb'})
        res = str(img).split(',')

        # 실제 주소
        p = re.compile(r'/post/show/\d+')
        data = p.findall(str(res))
        p = re.compile('\d+')
        data = p.findall(str(data))

        # 이미지 다운 주소
        p = re.compile(
            r'https://konachan.net/data/preview/\w+/\w+/\w+.png|https://konachan.net/data/preview/\w+/\w+/\w+.jpg')
        data1 = p.findall(str(res))

        print("First Number: " + str(data[0]))

        # 이미지 번호 대조
        for lists in range(len(data)):
            print("Last Number: " + str(lastnum))
            print("Image Number: " + str(data[lists]))
            if (str(lastnum) == str(data[lists])):
                print("============ konachan ============")
                now = time.strftime('%y-%m-%d %H:%M:%S')
                print("======= " + now + " ========")
                print("==================================")
                print("\n")
                break
            else:
                print("\n")

            url = "http://konachan.net/post/show" + data[lists]
            d_url = str(data1[lists])

            l_url.insert(0, url)
            l_d_url.insert(0, d_url)
            l_num.insert(0, data[lists])

        # 출력
        for l_list in range(len(l_url)):
            embed = discord.Embed(title="Konachan", description="Image number is " + str(l_num[l_list]), color=0xFF69B4,
                                  url=l_url[l_list])
            embed.set_image(url=l_d_url[l_list])
            await i_channel.send(content=None, embed=embed)

        # lastnum 기록
        f = open("./konachan_num.txt", 'w')
        f.write(str(data[0]))
        f.close()

        await asyncio.sleep(int(random.choice(timer)))

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
client.loop.create_task(prescence())
client.loop.create_task(neko())
client.loop.create_task(anime_pictures())
client.loop.create_task(yandere_pictures())
client.loop.create_task(konachan_pictures())
