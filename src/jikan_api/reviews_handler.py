from typing import Dict, Any
from jikan_api.jikan_client import APIClient # type: ignore

class ReviewsHandler:
    def __init__(self, client: APIClient):
        self.client = client
