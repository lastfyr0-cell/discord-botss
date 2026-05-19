"""
بوت 1 - ديسكورد
يبقى في الروم الصوتي للأبد
"""

import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

BOT_TOKEN = "MTQ5ODM5NTIzNjc5ODMwMDI1Ng.G9gLY6.kET9Ti382ZjJB4jL-QVaOSeQJoLrw-GSDyWJ3k"
GUILD_ID = 1346238254348767266
VOICE_CHANNEL_ID = 1475641096985120768

@bot.event
async def on_ready():
    print(f"✅ بوت 1 شغال: {bot.user}")
    bot.loop.create_task(stay_in_voice())

async def stay_in_voice():
    while True:
        try:
            guild = bot.get_guild(GUILD_ID)
            voice_channel = guild.get_channel(VOICE_CHANNEL_ID)
            voice_client = None
            for vc in bot.voice_clients:
                if vc.guild.id == GUILD_ID:
                    voice_client = vc
                    break
            if voice_client is None or not voice_client.is_connected():
                await voice_channel.connect()
                print(f"✅ بوت 1: تم الدخول للروم الصوتي")
            await asyncio.sleep(10)
        except Exception as e:
            print(f"❌ بوت 1 خطأ: {e}")
            await asyncio.sleep(20)

bot.run(BOT_TOKEN)
