from src.models.lighthouse import Lighthouse
import geojson


def export_geojson(lighthouses: list[Lighthouse]) -> None:
    features = []

    for lh in lighthouses:
        point = geojson.Point((lh.lon, lh.lat))
        features.append(
            geojson.Feature(
                geometry=point, properties={"name": lh.name, "source": lh.source}
            )
        )

    fc = geojson.FeatureCollection(features)

    with open("lighthouses.geojson", "w") as f:
        geojson.dump(fc, f, indent=2)
