import discord
import requests
import json

from discord.ext import commands

discordToken = ""
channelId = ""
prefix = ""

def initConfig():
    global discordToken, channelId, prefix

    f = open("config/config.json")
    data = json.load(f)

    discordToken = data["discordToken"]
    channelId = data["channelId"]
    prefix = data["prefix"]

    f.close()

def sendMessage(spoof, smsMessage, phoneNumber):
    messageUrl = "https://rest.clicksend.com/v3/sms/send"
    messageBody = {"messages":[{"source":"dashboard","from":spoof,"body":smsMessage,"schedule":None,"to":phoneNumber}]}
    messageHeaders = {"authority": "rest.clicksend.com", "method": "POST", "path": "/v3/sms/send", "accept": "application/json, text/plain, /", "authorization": "Bearer ecb129908e201c3fe2431d6f2ee13c628c0e7153b2cbc02d755f4f47ac9c74f22", "content-length": "102", "content-type": "application/json", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

    message = requests.post(messageUrl, data = json.dumps(messageBody), headers = messageHeaders)

    print(f"New spoof sms send to {phoneNumber}. Content: {smsMessage}")

initConfig()

client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Spoof SMS System", url="https://www.twitch.tv/monstercat"))
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def send(ctx, spoof, phoneNumber, *, message):
    if ctx.channel.id != channelId:
        return

    try:
        sendMessage(spoof, message, phoneNumber)
        await ctx.channel.send(":white_check_mark: The message `" + message + "` has been successfully sent to `" + phoneNumber + "`.")
    except:
        await ctx.channel.send(":x: An error occured. Usage !send <spoof> <phoneNumber ex.0606060606> <message>")

client.run(discordToken)
