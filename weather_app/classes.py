from dataclasses import dataclass
from datetime import datetime

@dataclass
class Weather:
    date: datetime
    details: dict
    temp: str
    weather: [dict]
    description: str
    
    def __str__(self) -> str:
        return f"[{self.date:%H:%M}] {self.temp}Celsius ({self.description})"