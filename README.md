# Roblox Trade Bot

This project is a Python-based trade automation bot for Roblox that intelligently evaluates incoming trades using real-time Rolimons RAP data and automatically accepts trades that meet a customizable profit threshold.

### Features

- Fetches active inbound trades from the Roblox API
- Calculates trade values using the [Rolimons](https://www.rolimons.com/itemapi) item database
- Automatically accepts trades if they meet or exceed the configured profit margin
- Built with modular, scalable architecture using `httpx` and `asyncio`
- Easily configurable via `config.py` (e.g., cookie, threshold, headers)

### Technologies Used

- Python 3
- Asyncio + HTTPX
- Regular Expressions
- Clean modular structure with reusable components

### Ideal For

- Practicing REST API consumption and asynchronous design
- Learning about value-based trading bots
- Demonstrating full-stack logic and modular software design for internship projects
