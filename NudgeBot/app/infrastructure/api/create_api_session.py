import aiohttp

async def create_api_session(base_url: str):
    timeout = aiohttp.ClientTimeout()
    connector = aiohttp.TCPConnector(

    )

    client = aiohttp.ClientSession(
        base_url=base_url
    )