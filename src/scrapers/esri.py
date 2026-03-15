from src.models.lighthouse import Lighthouse
import json
import requests

URL = "https://ws.lioservices.lrc.gov.on.ca/arcgis2/rest/services/LIO_OPEN_DATA/LIO_Open10/MapServer/14/query"
PARAMS = {
    "where": "CLASS_SUBTYPE='Lighthouse'",
    "outFields": "*", 
    "f": "json",
}

def fetch_esri() -> list[Lighthouse]:
    data = requests.get(url=URL, params=PARAMS).json()
    lighthouse_data = data.get("features")

    lighthouses = []

    for lighthouse in lighthouse_data:
        name = lighthouse.get("attributes").get("OFFICIAL_NAME")
        lon = lighthouse.get("geometry").get("x")
        lat = lighthouse.get("geometry").get("y")
        
        lh = Lighthouse(
            name = name,
            lon = lon,
            lat = lat,
            source = "Open Government"
        )
        lighthouses.append(lh)

    return lighthouses




fetch_esri()