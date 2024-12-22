from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from discord.ext import commands

# STEP 0: Load the environment variables
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
print(TOKEN)

# STEP 1: Create a new Discord client
intents : Intents = Intents.default()
intents.message_content = True
client : Client = Client(intents=intents)


# STEP 2: Define the message event handler
async def send_response(message: Message, user_message: str) -> None:
    if not user_message:
        print('Intents not working')
        return
    
    if '/claire' in user_message:
        await message.channel.send('Oh, you mentioned me, darling~? How can I assist you~?')
    
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
        
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        await message.channel.send(f"An error occurred: {e}")
        print(e)
        
        
# STEP 3: Register the message event handler
@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')
    
#STEP 4: Register the incoming message event handler
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    
    username: str = message.author.display_name
    user_message: str = message.content
    try:
        channel: str = message.channel.name
    except AttributeError:
        channel: str = 'Direct Message'
    
    
    print(f'{username} in {channel} says: {user_message}')
    
    await send_response(message, user_message)
    
    
# STEP 5: Main entry point
if __name__ == '__main__':
    client.run(TOKEN)