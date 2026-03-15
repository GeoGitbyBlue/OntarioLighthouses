import pandas as pandas

from src.models.lighthouse import Lighthouse

url = "https://en.wikipedia.org/wiki/List_of_lighthouses_in_Ontario"
# https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy
HEADERS = {"User-Agent": "GISResearchBot/1.0 (contact: geogitpy@gmail.com)"}

def fetch_wiki():
    df= pandas.read_html(url, storage_options = HEADERS)[0]
    df.columns = df.columns.str.replace("\ufeff", "")
    
    lighthouses = []

    for row in df.itertuples():
        lat , lon = split_location(row.Location)
        name = row.Name

        lh = Lighthouse(
            name = name,
            lat =lat,
            lon = lon,
            source = "Wikipedia"
        )
        lighthouses.append(lh)

    return lighthouses


def split_location(location_str: str):
    decimal = location_str.split("/")[-1].strip().lstrip("\ufeff")
    lat, lon = decimal.split()
    return normalize_coord(lat), normalize_coord(lon)

def normalize_coord(coord: str) -> float | None:
    """Convert 42.64°N format to signed decimal degrees"""
    coord = coord.strip().replace("°", "")

    if coord.endswith("N") or coord.endswith("E"):
        return float(coord[:-1])

    if coord.endswith("S") or coord.endswith("W"):
        return -float(coord[:-1])

    return float(coord)

fetch_wiki()