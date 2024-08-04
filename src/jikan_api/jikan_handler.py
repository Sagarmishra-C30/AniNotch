# src/jikan_handler.py
from typing import Dict, Any
from jikan_api.jikan_client import APIClient # type: ignore

class JikanHandler:
    def __init__(self, client: APIClient):
        self.client = client

    async def get_top_anime(self) -> Dict[str, Any]:
        return await self.client._get('/top/anime')

    async def search_anime(self, query: str) -> Dict[str, Any]:
        return await self.client._get('/anime', params={'q': query})

    async def get_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}')

    async def get_anime_full_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/full')

    async def get_character_by_id(self, character_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/characters/{character_id}')

    async def get_episodes_for_anime_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/episodes')

    async def get_episode_for_anime_by_id(self, anime_id: int, episode_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/episodes/{episode_id}')

    async def get_videos_for_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/videos')
    
    async def get_video_episodes_for_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/videos/episodes')

    async def get_picture_for_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/pictures')
    
    async def get_statistics_for_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/statistics')

    async def get_more_info_on_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/moreinfo')
    
    async def get_recommendations_for_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/recommendations')
    
    async def get_reviews_for_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/reviews')
    
    async def get_relations_for_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/relations')
    
    async def get_themes_for_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/themes')
    
    async def get_external_for_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/external')
    
    async def get_streaming_for_anime_by_id(self, anime_id: int) -> Dict[str, Any]:
        return await self.client._get(f'/anime/{anime_id}/streaming')
    

    

    # Add more methods as needed
