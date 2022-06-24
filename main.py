import discord

class Client(discord.Client):
    async def on_ready(self):
        print("Jax evasion")

    async def on_message(self, message):


        mosthalal_champ_liste = ["fiddlesticks", "kayle", "draven", "ziggs", "zilean", "alistar", "jax", "mordekaiser", "nunu & willi", "nunu und willump", "nunu & willump", "nunu willump", "nunu & william", "nunu und william"]
        halal_champ_liste = ["ryze", "Lee sin", "bard", "darius", "nautilus", "scarner", "mordekaiser", "swain", "aatrox", "teemo", "jhin", "shaco", "pyke", "rengar", "maokai", "braum", "blitzcrank", "ornn", "aphelios", "sejuani", "nasus", "hecarim", "ivern", "tahm kench", "rammus", "renata glasc", "sett", "aurelion sol", "corki", "dr. mundo", "galio", "gankplank", "gragas", "heimerdinger", "illaoi", "karma", "karthus", "kled", "lillia", "malphite", "pantheon", "shen", "singed", "sion", "taric", "thresh", "trundle", "tryndamere", "twitch", "urgot", "vex", "warwick", "yorick"]
        mubah_champ_liste = ["zed", "azir", "garen", "xin zhao", "vayne", "senna", "talon", "leona", "fizz", "xerath", "kai'sa", "twisted fate", "renekton", "vel'koz", "volibear", "kassadin", "kayn", "kennen", "akali", "amumu", "brand", "ekko", "gnar", "kalista", "kha'zix", "malzahar", "olaf", "orianna", "poppy", "rumble", "taliyah", "udyr", "veigar", "wukong", "xayah", "zac", "zeri"]
        makruh_champ_liste = ["cho'gath", "riven", "yasuo", "samira", "viego", "rell", "irelia", "cassiopeia", "vladimir", "shyvana", "yone", "nocturne", "soraka", "anivia", "ashe", "camille", "elise", "graves", "jarvan", "jayce", "katarina", "kindred", "kog'maw", "lissandra", "master yi", "quinn", "rek'sai", "tristana", "vi", "caitlyn"]
        haram_champ_liste = ["evelynn", "qiyana", "syndra", "ahri", "akshan", "diana", "fiora", "gwen", "janna", "leblanc", "miss fortune", "morgana", "nami", "neeko", "nidalee", "sona", "sylas", "sivir", "varus", "zyra"]
        mostharam_champ_liste = ["lucian", "rakan", "seraphine", "lux", "zoe", "annie", "bel'veth", "ezreal", "jinx", "lulu", "zoe", "nilah"]
        if message.author == client.user:
            return
        if message.content == "$help":
            await message.channel.send("Active: Jax enters Evasion, a defensive stance, for up to 2 seconds, causing all basic attacks against him to miss. Jax also takes 25% reduced damage from all champion area of effect abilities. After 1 second, Jax can reactivate to end it immediately.")

        m = str(message.content)
        n = m.lower()

        for element in range(len(mosthalal_champ_liste)):
            if mosthalal_champ_liste[element] in n:
                x = ""
                x = x+mosthalal_champ_liste[element]
                x = x.upper()
                if x == "JAX":
                    await message.channel.send("JAQX is most halal")
                elif x == "DRAVEN":
                    await message.channel.send("DROBEN is most halal")
                else:
                    await message.channel.send(x + " is most halal")
        for element in range(len(halal_champ_liste)):
            if halal_champ_liste[element] in n:
                x = ""
                x = x + halal_champ_liste[element]
                x = x.upper()
                await message.channel.send(x + " is halal")
        for element in range(len(mubah_champ_liste)):
            if mubah_champ_liste[element] in n:
                x = ""
                x = x+mubah_champ_liste[element]
                x = x.upper()
                await message.channel.send(x + " is mubah")
        for element in range(len(makruh_champ_liste)):
            if makruh_champ_liste[element] in n:
                x = ""
                x = x+makruh_champ_liste[element]
                x = x.upper()
                await message.channel.send(x + " is makruh")
        for element in range(len(haram_champ_liste)):
            if haram_champ_liste[element] in n:
                x = ""
                x = x+haram_champ_liste[element]
                x = x.upper()
                await message.channel.send(x + " is haram")
        for element in range(len(mostharam_champ_liste)):
            if mostharam_champ_liste[element] in n:
                x = ""
                x = x+mostharam_champ_liste[element]
                x = x.upper()
                await message.channel.send(x + " is most haram")



    async def on_typing(self, channel, user, when):
        pass

    async def on_message_edit(self, before, after):
        pass

    async def on_reaction_add(self, user):
        pass

    async def on_raw_reaction_add(self, payload):
        pass


client = Client()
client.run("")
