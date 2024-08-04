# src/jikan_client.py
import httpx
from typing import Dict, Any, Optional

class APIClient:
    def __init__(self, base_url: str = 'https://api.jikan.moe/v4', timeout: int = 10):
        self.base_url = base_url
        self.timeout = timeout
        self.client = httpx.AsyncClient(base_url=self.base_url, timeout=timeout)

    async def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        try:
            response = await self.client.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return {}
        except Exception as err:
            print(f"Other error occurred: {err}")
            return {}

    async def close(self):
        await self.client.aclose()
