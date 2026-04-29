import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

tips = [
    "Wyłącz światło gdy nie jest potrzebne 💡",
    "Krótszy prysznic = mniej zużytej wody 🚿",
    "Używaj transportu publicznego 🚌",
    "Nie marnuj jedzenia 🍽️",
    "Wyłącz ładowarkę z gniazdka gdy jej nie używasz 🔌",
    "Segreguj śmieci ♻️",
    "Używaj butelki wielokrotnego użytku 🧴",
    "Kupuj lokalne produkty 🥕",
    "Unikaj plastiku jednorazowego 🚫",
    "Sadź drzewa lub rośliny 🌳",
    "Zakręcaj wodę podczas mycia zębów 🚰",
    "Korzystaj z roweru zamiast auta 🚴",
    "Ogranicz używanie klimatyzacji ❄️",
    "Wybieraj produkty z recyklingu ♻️",
    "Nie drukuj jeśli nie musisz 🖨️",
    "Naprawiaj zamiast wyrzucać 🔧",
    "Używaj energooszczędnych żarówek 💡",
    "Gotuj tylko tyle ile zjesz 🍲",
    "Wyłącz komputer na noc 💻",
    "Używaj torby wielorazowej 🛍️"
]

quizy = [
    {"pytanie": "Czy plastik rozkłada się ponad 100 lat?", "odpowiedz": "tak"},
    {"pytanie": "Czy CO2 pomaga ochłodzić planetę?", "odpowiedz": "nie"},
    {"pytanie": "Czy drzewa produkują tlen?", "odpowiedz": "tak"},
    {"pytanie": "Czy jazda rowerem jest bardziej ekologiczna niż autem?", "odpowiedz": "tak"},
    {"pytanie": "Czy szkło można recyklingować?", "odpowiedz": "tak"},
    {"pytanie": "Czy energia słoneczna szkodzi środowisku?", "odpowiedz": "nie"},
    {"pytanie": "Czy zmiana klimatu jest realnym problemem?", "odpowiedz": "tak"},
    {"pytanie": "Czy samochody elektryczne emitują spaliny?", "odpowiedz": "nie"},
    {"pytanie": "Czy lodowce się kurczą przez ocieplenie?", "odpowiedz": "tak"},
    {"pytanie": "Czy papier zawsze można wyrzucić do plastiku?", "odpowiedz": "nie"},
    {"pytanie": "Czy recykling pomaga środowisku?", "odpowiedz": "tak"},
    {"pytanie": "Czy wyłączanie światła oszczędza energię?", "odpowiedz": "tak"},
    {"pytanie": "Czy ocean pochłania CO2?", "odpowiedz": "tak"},
    {"pytanie": "Czy spalanie węgla jest ekologiczne?", "odpowiedz": "nie"},
    {"pytanie": "Czy globalne ocieplenie wpływa na pogodę?", "odpowiedz": "tak"}
]

wyzwania = [
    "Dziś spróbuj zużyć mniej prądu ⚡",
    "Nie używaj plastiku przez cały dzień 🚫",
    "Zrób spacer zamiast jechać autem 🚶",
    "Zgaś wszystkie niepotrzebne światła 💡",
    "Weź krótszy prysznic 🚿",
    "Nie kupuj dziś nic w plastiku 🛍️",
    "Wypij wodę z kranu zamiast z butelki 🚰",
    "Użyj roweru zamiast samochodu 🚴",
    "Posprzątaj śmieci w swojej okolicy 🧹",
    "Zjedz dziś coś bez mięsa 🥗",
    "Odłącz wszystkie nieużywane urządzenia 🔌",
    "Nie używaj windy – wybierz schody 🪜",
    "Zrób coś DIY zamiast kupować 🛠️",
    "Zgaś światło na 1 godzinę 🌙",
    "Namów kogoś do ekologicznego działania 👥",
    "Użyj torby wielorazowej 🛍️",
    "Ogranicz czas spędzony na elektronice 📵",
    "Zrób listę rzeczy które możesz robić bardziej eko 📝",
    "Posadź roślinę 🌱",
    "Nie marnuj jedzenia przez cały dzień 🍽️"
]

aktywny_quiz = {}

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.id in aktywny_quiz:
        poprawna = aktywny_quiz[message.author.id]["odpowiedz"]

        if message.content.lower() == poprawna:
            embed = discord.Embed(
                title="✅ Dobrze!",
                description="Poprawna odpowiedź 🎉",
                color=0x2ecc71
            )
        else:
            embed = discord.Embed(
                title="❌ Źle!",
                description="Nie poprawna odpowiedź 😭",
                color=0xe74c3c
            )

        await message.channel.send(embed=embed)
        del aktywny_quiz[message.author.id]
        return

    await bot.process_commands(message)

@bot.command()
async def tip(ctx):
    t = random.choice(tips)

    embed = discord.Embed(
        title="🌍 Tip klimatyczny",
        description=t,
        color=0x2ecc71
    )

    await ctx.send(embed=embed)


@bot.command()
async def quiz(ctx):
    q = random.choice(quizy)

    aktywny_quiz[ctx.author.id] = q

    embed = discord.Embed(
        title="🧠 Quiz klimatyczny",
        description=q["pytanie"] + "\n\nOdpowiedz: tak / nie",
        color=0x3498db
    )

    await ctx.send(embed=embed)


@bot.command()
async def wyzwanie(ctx):
    w = random.choice(wyzwania)

    embed = discord.Embed(
        title="🔥 Wyzwanie dnia",
        description=w,
        color=0xf1c40f
    )

    await ctx.send(embed=embed)

@bot.command()
async def mem(ctx):
    imgs = os.listdir('images')

    imgs = [img for img in imgs if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    img_name = random.choice(imgs)

    file = discord.File(f'images/{img_name}', filename=img_name)

    embed = discord.Embed(
        title="😂 Losowy mem",
        color=0x9b59b6
    )

    embed.set_image(url=f"attachment://{img_name}")

    await ctx.send(file=file, embed=embed)





































































    