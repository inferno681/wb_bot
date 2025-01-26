from httpx import AsyncClient

from config import config


class ProductService:
    def __init__(self):
        """Service initialization."""
        self.BASE_URL = config.api.base_url
        self.client = AsyncClient()

    async def close(self):
        """Close client method."""
        await self.client.aclose()

    async def request(self, method: str, endpoint: str, **kwargs):
        """Base HTTP-request method."""
        url = f'{self.BASE_URL}/{endpoint}'
        response = await self.client.request(method, url, **kwargs)
        if response.status_code != 200:
            return response.json().get('detail', 'Ошибка при получении данных')
        else:
            return str(response.json())

    async def get_product(self, article: int):
        return await self.request('GET', f'products/{article}')

    async def collect_data(self, article: int):
        return await self.request(
            'POST', 'products', json={'artikul': article}
        )

    async def sub_activation(self, article: int):
        return await self.request('GET', f'subscription/{article}')

    async def sub_deactivation(self, article: int):
        return await self.request('DELETE', f'subscription/{article}')


service = ProductService()
