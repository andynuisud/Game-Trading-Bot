import json
from config import TRADES_API, HEADERS
import httpx

async def get_trade_list():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TRADES_API}/getmytrades", headers=HEADERS)
        if response.status_code != 200:
            raise Exception("Failed to fetch trades. Check your cookie.")
        return json.loads(json.loads(response.text)['d'])['Data']

async def get_trade_details(session_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TRADES_API}/tradedetails/{session_id}", headers=HEADERS)
        return json.loads(response.text) if response.status_code == 200 else None
