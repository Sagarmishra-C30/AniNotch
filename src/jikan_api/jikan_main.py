# src/main.py
import asyncio
import json
from jikan_api.jikan_client import APIClient # type: ignore
from jikan_api.jikan_handler import JikanHandler # type: ignore
from logging_config import data_logger, app_logger, error_logger # type: ignore

async def main():
    app_logger.info("Starting the main function")
    try:
        client = APIClient()
        handler = JikanHandler(client)

        app_logger.info("Fetching top anime")
        top_anime = await handler.get_top_anime()
        app_logger.info("Fetched top anime successfully")
        data_logger.info("Top Anime Data: %s", json.dumps(top_anime, indent=4))

        app_logger.info("Fetching anime details for ID 1")
        anime_details = await handler.get_anime_by_id(2)
        app_logger.info("Fetched anime details successfully")
        data_logger.info("Anime Details Data: %s", json.dumps(anime_details, indent=4))

        app_logger.info("Searching for anime 'One Punch Man'")
        search_results = await handler.search_anime("One Punch Man")
        app_logger.info("Fetched search results successfully")
        data_logger.info("Search Results Data: %s", json.dumps(search_results, indent=4))

        app_logger.info("Fetching character details for ID 1")
        character_details = await handler.get_character_by_id(5)
        app_logger.info("Fetched character details successfully")
        data_logger.info("Character Details Data: %s", json.dumps(character_details, indent=4))

        await client.close()
        app_logger.info("Closed API client")
    except Exception as e:
        app_logger.error("An error occurred: %s", e)
        raise

def run():
    asyncio.run(main())

if __name__ == "__main__":
    run()
