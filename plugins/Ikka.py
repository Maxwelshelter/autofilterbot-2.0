#created by by @Arjun_La_Lis_A - tg
#use with proper credits

import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


IKKA_STRINGS = (
    "CAACAgUAAxkBAALhS2LNJAX-zxYGjveNYElJXI-NEBdLAAIoAgAChwE5VuOe6yHppi8EHgQ",
    "CAACAgUAAxkBAALhTGLNJA7NAvK67HNAyOEpTE7ajN-NAAJbAgACytc4VsF8w1nc8dWfHgQ",
    "CAACAgUAAxkBAALhTWLNJBQSNLvf34BEo27EQ6GbE0tGAAKWAgAC-TpJVrI9K2-82cdBHgQ",
    "CAACAgUAAxkBAALhTmLNJCIGPZCKII5aO4lDX_XN0MNBAALAAgACtttIVjy-z2iRr7yYHgQ",
    "CAACAgUAAxkBAALhT2LNJCn9JX0cSYz1q1gIbWxitryiAAJRAwACRs9RVjPadYV0Dpt8HgQ",
    "CAACAgUAAxkBAALhUGLNJDVjESc9cRGi1aqicPG49N7KAALYAQACxWFwVlj-FJKPH6zkHgQ",
    "CAACAgUAAxkBAALhUWLNJEMTIr1Iqb5HpBbmKfzNA4DWAAKmAwACfoBwVpq8Q6mXd3mjHgQ",
    "CAACAgUAAxkBAALhUmLNJFXDYN52k312IgS4IveKdkknAAIrAgACtHqRVtijwDY-iGHwHgQ",
    "CAACAgUAAxkBAALhU2LNJGKne8u65UKaiVcAAcTtCWx_1AACuAEAAkoaqVba6Tz6gtkwlB4E",
    "CAACAgUAAxkBAALhVGLNJGw8aBhWRhJh0yCH2YV1md3vAAIQAgAC2p6pVsbrIgAB-ZTwXh4E",
    "CAACAgUAAxkBAALhVWLNJHDjEaU6L37iAfj1BQpFJHj-AALPAAOQzUYxpm5eATF7NNUeBA",
    "CAACAgUAAxkBAALhVmLNJHblo-WNuv2iKUxodokDbJSkAAJuAQACMJ45V-NtuG7cIVEiHgQ",
    "CAACAgUAAxkBAALhV2LNJHwTlETQbSwfvWagLDaqCaDbAAIEAAPFsQo6NbLLKxbcR1seBA",
    "CAACAgQAAxkBAALhWGLNJIRlXQfGzcy1SLv3u576s_tRAAJzCAAC6zvQU3KioQXpsh6YHgQ",
)


@Client.on_message(
    filters.command("meme", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def ikka(_, message):
    """ /meme strings """
    effective_string = random.choice(IKKA_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_sticker(effective_string)
    else:
        await message.reply_sticker(effective_string)
