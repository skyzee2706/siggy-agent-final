import os
import asyncio
from dotenv import load_dotenv

# Load environment variables before importing local modules
load_dotenv()

from src.bot import SiggyBot

async def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("Missing DISCORD_TOKEN in .env")
        return

    bot = SiggyBot()
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
