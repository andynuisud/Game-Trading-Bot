import json
from bot.trades import get_trade_list, get_trade_details
from bot.rolimons import get_rolimons_values
from bot.utils import extract_item_ids, item_names, calculate_total_value
from bot.actions import execute_trade
from config import PROFIT_THRESHOLD

import asyncio

async def evaluate_trades():
    trades = await get_trade_list()
    values = await get_rolimons_values()
    print(f"Found {len(trades)} trades to review.\n")

    for i, trade_json in enumerate(trades, 1):
        session_id = int(json.loads(trade_json)['TradeSessionID'])
        trade_data = await get_trade_details(session_id)

        if not trade_data or 'data' not in trade_data:
            print(f"Skipping trade #{i}: Failed to fetch trade data.")
            continue

        trade_items = json.loads(trade_data['data'])['AgentOfferList']
        offer = trade_items[0]['OfferList']
        request = trade_items[1]['OfferList']

        offer_ids = extract_item_ids(offer)
        request_ids = extract_item_ids(request)

        offer_value = calculate_total_value(offer_ids, values)
        request_value = calculate_total_value(request_ids, values)
        profit = offer_value - request_value

        print(f"\nTrade #{i}")
        print(f"You give:    {item_names(request)} [{request_value} RAP]")
        print(f"You receive: {item_names(offer)} [{offer_value} RAP]")
        print(f"Net Gain: {profit} RAP")

        if profit >= PROFIT_THRESHOLD:
            print(f"Accepting trade #{i} (profit ≥ {PROFIT_THRESHOLD})")
            await execute_trade(session_id, "accept")
        else:
            print(f"Skipping trade #{i} (profit below threshold)")

if __name__ == '__main__':
    asyncio.run(evaluate_trades())
