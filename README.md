# SMS-Spoofer
SMS spoofer using free api, (2$ free credit). you can send with a webhook.

**How to use**

- Create a discord bot
- Create a discord Server
- Invite your bot in server
- Copy the token of bot and put in config.json
- Create a chat in discord server and copy the id 
- put the id in config.json
- go to https://rest.clicksend.com/v3/sms/send press F12 send a test message to random phone
- and find in network headers the auto "authorization": "Bearer 
- copy and paste it in bot.py 

Open the .py and go to discord.
to send message : !send THENAMEOFSENDER THENUMBEROFVICTIME YOUMESSSAGE 
press enter and done ! ez