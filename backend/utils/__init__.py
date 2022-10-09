import asyncio
from aiohttp import ClientSession


async def async_fetch(session, url, **kwargs):
    """Fetch the specified url using the given aiohttp session"""
    response = await session.get(url, **kwargs)
    return response