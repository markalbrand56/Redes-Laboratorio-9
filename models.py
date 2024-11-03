from dataclasses import dataclass
from typing import Literal

@dataclass
class Data:
    temperature: float
    humidity: float
    wind_direction: Literal["N", "NO", "O", "SO", "S", "SE", "E", "NE"]