import discord
from discord.ext import commands
from src.agent import get_siggy_response

class SiggyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        # Allow bot to read messages in servers it is in
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f'Siggy is online!')
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('Ready to help the Ritual community.')
        print('------')

    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.user:
            return

        # Check if the bot is mentioned or if it's a DM
        is_dm = isinstance(message.channel, discord.DMChannel)
        is_mentioned = self.user.mentioned_in(message)

        if is_mentioned or is_dm:
            # Clean up the message content (remove the mention)
            # This makes the user input cleaner for the AI
            clean_content = message.content.replace(f'<@!{self.user.id}>', '').replace(f'<@{self.user.id}>', '').strip()
            
            if not clean_content and is_mentioned:
                await message.reply("Hey there! How can I help you today? Mention me and ask anything about Ritual or crypto!")
                return

            print(f"Processing message from {message.author}: {clean_content}")
            
            async with message.channel.typing():
                try:
                    # Get response from our LangChain agent
                    response = get_siggy_response(clean_content)
                    print(f"DEBUG: Bot received response: '{response}'")
                    
                    if not response or not response.strip():
                        print("DEBUG: Empty response detected, skipping message send.")
                        return
                    
                    # Split long responses if they exceed Discord's 2000 char limit
                    if len(response) > 2000:
                        chunks = [response[i:i+2000] for i in range(0, len(response), 2000)]
                        for chunk in chunks:
                            await message.reply(chunk)
                    else:
                        await message.reply(response)
                except Exception as e:
                    print(f"Error in on_message: {e}")
                    await message.reply("Oh no, something went wrong on my end. Can you try asking that again in a second?")

        # Still process commands if we add any later
        await self.process_commands(message)
