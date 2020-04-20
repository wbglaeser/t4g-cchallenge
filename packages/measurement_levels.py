import requests
import copy
from datetime import datetime
from collections import OrderedDict

class MeasurementLevels:

    URL="""https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/{id}/{type}/currentmeasurement.json"""
    TREND_NUM_TO_STR={
        1:"Ansteigend",
        0:"Stabil",
        -1:"Abfallend"
    }
    VALUE_TO_MELDESTUFE={
        "LEVEL_4":850,
        "LEVEL_3":770,
        "LEVEL_2":740,
        "LEVEL_1":700,
    }

    def fetch_individual_station(self, station: dict) -> dict:
        """ fetch measurement levels for individual station """

        # request api
        response = requests.get(self.URL.format(
            id=station["id"],
            type=station["type"]
        ))

        # make sure we get valid response
        assert response.status_code == 200, f"Request failed with status code {response.status_code}"

        return response.json()

    @classmethod
    def fetch_all_stations(cls, measurement_stations) -> dict:
        """ fetch measurement levels for all stations """

        # initialse fetcher class
        ml = cls()

        # update measure stations with fetched values
        for station in measurement_stations:

            # fetch response json
            res_json = ml.fetch_individual_station(station)

            # update measurement station
            station["current_value"] = res_json["value"]
            station["trend"] = res_json["trend"]
            station["trend_str"] = ml.translate_trend(res_json["trend"])
            station["current_value"] = ml.translate_value_to_meldestufe(res_json["value"])
            station["last_update"] = ml.parse_timestamp(res_json["timestamp"])

        return measurement_stations

    def translate_trend(self, trend: int) -> str:
        """ translate trend code to string """

        try:
            trend_str = self.TREND_NUM_TO_STR[trend]
        except Keyerror:
            print("Unknown trend parameter received")
            trend_str = "Unbekannter Trend parameter"

        return trend_str

    def translate_value_to_meldestufe(self, value: float) -> str:
        """ translate water level to meldestufe """

        meldestufe="Keine erhöhte Meldestufe"

        for key, _val in self.VALUE_TO_MELDESTUFE.items():
            if value >= _val:
                meldestufe=key
                break

        return meldestufe

    @staticmethod
    def parse_timestamp(timestamp: str) -> str:
        """ convert timestamp to easier to read format """

        timestamp_dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S+02:00")
        return timestamp_dt.strftime("%H:%M on %d-%m-%Y" )