#!usr/bin/env python3

import discord

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

from config import BABYTOKEN


#hello maggle
client = discord.Client()
DEVELOPER_KEY = "AIzaSyAtlS6Mf3ONECnN8y9BHhESN8AEy549zK0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(options, max=5):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(q=options, part="id,snippet", maxResults=max).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                        search_result["id"]["videoId"]))

    print("Videos:\n", "\n".join(videos), "\n")


    if __name__ == "__main__":
        argparser.add_argument("--q", help="Search term", default="Google")
        argparser.add_argument("--max", help="Max", default=25)
        args = argparser.parse_args()

    # try:
    youtube_search(args)
    # except HttpError e:
    #     print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))




@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!yo'):
        msg = 'Yo ma grosse {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!wesh'):
        msg = 'Ayo fraté {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('!play'):
        words = message.content.split()
        important_words = words[1:]
        await client.send_message(message.channel, youtube_search(important_words))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#connexion de mon bot sur discord
client.run(BABYTOKEN)


