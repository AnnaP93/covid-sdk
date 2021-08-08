
import requests
from Summary import Summary
from Provinces import Provinces
from Summary import SummaryAll, ProvinceSummary, HealthRegionSummary


class CovidSdk:
    __split_data = None
    @staticmethod
    def summary(province: Provinces) -> Summary:
        if province == Provinces.All:
            data = requests.get('https://api.covid19tracker.ca/summary')
            return SummaryAll(data.json())
        else:
            if CovidSdk.__split_data is None:
                CovidSdk.__split_data = requests.get('https://api.covid19tracker.ca/summary/split')
            province_split_data = CovidSdk.__split_data.json()
            for item in province_split_data['data']:
                if item['province'] == province.value:
                    province_breakdown = ProvinceSummary(item)
                    return province_breakdown




