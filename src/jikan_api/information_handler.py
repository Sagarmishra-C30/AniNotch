from typing import Dict, Any
from jikan_api.jikan_client import APIClient # type: ignore

class InformationHandler:
    def __init__(self, client: APIClient):
        self.client = client
