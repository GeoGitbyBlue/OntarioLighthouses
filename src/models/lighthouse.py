from dataclasses import dataclass

@dataclass
class Lighthouse:
    name: str | None
    lat: float 
    lon: float
    source: str