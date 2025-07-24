import httpx
from config import ROLIMONS_API

async def get_rolimons_values():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(ROLIMONS_API)
            return response.json()['items']
        except Exception as e:
            print(f"Error fetching Rolimons values: {e}")
            return {}
