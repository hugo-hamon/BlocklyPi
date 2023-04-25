from .francaster_controller import FrancasterController
from .all_bot_controller import AllBotController
from typing import Tuple


class Controller(FrancasterController, AllBotController):
    
    def __init__(self, host: str, port: int, server: Tuple[str, int]) -> None:
        super().__init__(host, port, server)