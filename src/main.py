from src.scrapers.wikipedia import fetch_wiki 
from src.scrapers.esri import fetch_esri
from src.exporters.geojson import export_geojson


def main():
    wiki = fetch_wiki()
    esri = fetch_esri()
    export_geojson(wiki + esri)

if __name__ == "__main__":
    main()