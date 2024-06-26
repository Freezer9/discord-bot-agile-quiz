from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# Load the token from the .env file
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot Setup
intents: Intents = Intents.default()
intents.message_content = True 
client: Client = Client(intents=intents)

# Message Functionality
async def send_message(message: Message, user_message: str) -> None:
  if not user_message:
    print('User message is empty')
    return

  if is_private := user_message[0] == '?':
    user_message = user_message[1:] 

  try:
    response: str = get_response(user_message)
    if is_private:
      await message.author.send(response) 
    else:
      await message.channel.send(response) 
  except Exception as e:
    await message.channel.send('Sorry, I am unable to process your request at the moment.', e)

# Handling startup Bot
@client.event
async def on_ready() -> None:
  print(f'{client.user} has connected to Discord!')

# Handling messages
@client.event
async def on_message(message: Message) -> None:
  if message.author == client.user:
    return 

  username: str = str(message.author)
  user_message: str = message.content
  channel: str = str(message.channel)

  print(f'{username} in {channel} sent: {user_message}')

  await send_message(message, user_message)

# Main Function
def main() -> None:
  client.run(TOKEN)

if __name__ == '__main__':
  main()
  