import redis.asyncio as redis


class VectorCache:
    def __init__(self, url="redis://localhost"):
        self.client = redis.from_url(url)

    async def get(self, key):
        return await self.client.get(key)

    async def set(self, key, value, expire=None):
        await self.client.set(key, value, ex=expire)
