import aiohttp
from fake_useragent import UserAgent


class Service:
    user_agent = UserAgent()

    def __init__(self, phone, phone_code):
        self.phone = phone
        self.phone_code = phone_code
        self.formatted_phone = self.phone_code + self.phone
        self.client = aiohttp.ClientSession()

        self.client.headers = {'User-Agent': self.generate_random_user_agent()}

    @staticmethod
    def generate_random_user_agent():
        return Service.user_agent.random

    async def post(self, url: str, data=None, params=None, json=None):
        if params is None:
            params = {}
        if json is None:
            await self.client.post(url, data=data, params=params)
        elif data is None:
            await self.client.post(url, json=json, params=params)
        await self.client.close()

    async def get(self, url, params):
        await self.client.post(url, params=params)
        await self.client.close()

