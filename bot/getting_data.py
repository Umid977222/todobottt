import aiohttp
from .config import proxy, password, user


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy, auth=aiohttp.BasicAuth(user, password)) as response:
            return await response.text()
