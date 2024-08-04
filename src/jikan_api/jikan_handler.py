# src/jikan_handler.py
from typing import Dict, Any
from jikan_api.jikan_client import APIClient # type: ignore

class JikanHandler:
    def __init__(self, client: APIClient):
        self.client = client

    async def get_top_anime(self) -> Dict[str, Any]:
        return await self.client._get('/anime/top')

    async def get_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}')

    async def search_anime(self, query: str) -> Dict[str, Any]:
        return await self.client._get('/anime', params={'q': query})

    async def get_character_by_id(self, character_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/characters/{character_id}')

    # Add more methods as needed
