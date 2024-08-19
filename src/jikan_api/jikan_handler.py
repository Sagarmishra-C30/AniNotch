# src/jikan_api/jikan_handler.py

from jikan_api.anime_handler import AnimeHandler
from jikan_api.characters_handler import CharactersHandler
from jikan_api.clubs_handler import ClubsHandler
from jikan_api.genres_handler import GenresHandler
from jikan_api.magazines_handler import MagazinesHandler
from jikan_api.manga_handler import MangaHandler
from jikan_api.people_handler import PeopleHandler
from jikan_api.producers_handler import ProducersHandler
from jikan_api.random_handler import RandomHandler
from jikan_api.recommendations_handler import RecommendationsHandler
from jikan_api.reviews_handler import ReviewsHandler
from jikan_api.schedules_handler import SchedulesHandler
from jikan_api.users_handler import UsersHandler
from jikan_api.seasons_handler import SeasonsHandler
from jikan_api.top_handler import TopHandler
from jikan_api.watch_handler import WatchHandler
from jikan_api.jikan_client import APIClient

class JikanHandler:
    def __init__(self, client: APIClient):
        self.client = client
        self.anime_handler = AnimeHandler(client)
        self.character_handler = CharactersHandler(client)
        self.clubs_handler = ClubsHandler(client)
        self.genres_handler = GenresHandler(client)
        self.magazines_handler = MagazinesHandler(client)
        self.manga_handler = MangaHandler(client)
        self.people_handler = PeopleHandler(client)
        self.producers_handler = ProducersHandler(client)
        self.random_handler = RandomHandler(client)
        self.recommendations_handler = RecommendationsHandler(client)
        self.reviews_handler = ReviewsHandler(client)
        self.schedules_handler = SchedulesHandler(client)
        self.users_handler = UsersHandler(client)
        self.seasons_handler = SeasonsHandler(client)
        self.top_handler = TopHandler(client)
        self.watch_handler = WatchHandler(client)

    def __getattr__(self, name):
        # Delegate method calls to the appropriate handler
        for handler in [
            self.anime_handler,
            self.character_handler,
            self.clubs_handler,
            self.genres_handler,
            self.magazines_handler,
            self.manga_handler,
            self.people_handler,
            self.producers_handler,
            self.random_handler,
            self.recommendations_handler,
            self.reviews_handler,
            self.schedules_handler,
            self.users_handler,
            self.seasons_handler,
            self.top_handler,
            self.watch_handler,
        ]:
            if hasattr(handler, name):
                return getattr(handler, name)
        
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    async def close(self):
        await self.client.close()
