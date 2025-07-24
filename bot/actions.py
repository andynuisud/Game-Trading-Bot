from config import HEADERS, TRADES_API
import httpx

async def execute_trade(session_id, action):
    async with httpx.AsyncClient() as client:
        endpoint = f"{TRADES_API}/action/{action}/{session_id}"
        response = await client.post(endpoint, headers=HEADERS)
        if response.status_code == 200:
            print(f"Successfully {action}ed trade #{session_id}")
        else:
            print(f"Failed to {action} trade #{session_id}: {response.status_code}")
