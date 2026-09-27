import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Bot online sebagai {bot.user}")

@bot.command()
async def embed(ctx):
    embed = discord.Embed(
        title="📢 Informasi",
        description="Ini adalah pesan embed dari bot KF.",
        color=0x5865F2
    )

    embed.add_field(
        name="Server",
        value="KF Community",
        inline=False
    )

    embed.set_footer(text="KF Community")

    await ctx.send(embed=embed)

bot.run("TOKEN_BOT_KAMU")
