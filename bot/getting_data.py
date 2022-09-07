import aiohttp
from .config import proxy


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy) as response:
            return await response.json()
