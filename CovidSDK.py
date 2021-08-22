from typing import Union, List

import requests
from Summary import Summary
from Provinces import Provinces
from SummaryAll import SummaryAll
from SummaryByProvince import SummaryByProvince
from SummaryByRegion import SummaryByRegion


class CovidSdk:
    __split_data = None

    @staticmethod
    def summary(province: Provinces) -> Union[SummaryAll, SummaryByProvince]:
        if province == Provinces.All:
            data = requests.get('https://api.covid19tracker.ca/summary')
            return SummaryAll(data.json())
        else:
            if CovidSdk.__split_data is None:
                CovidSdk.__split_data = requests.get('https://api.covid19tracker.ca/summary/split')
            province_split_data = CovidSdk.__split_data.json()
            for item in province_split_data['data']:
                if item['province'] == province.value:
                    province_breakdown = SummaryByProvince(item)
                    return province_breakdown

    @staticmethod
    def summary_by_region(region_id) -> SummaryByRegion:
        hr_data_split = requests.get('https://api.covid19tracker.ca/summary/split/hr')
        all_regions_summary = hr_data_split.json()
        for item in all_regions_summary['data']:
            if item['hr_uid'] == region_id:
                region_summary = SummaryByRegion(item)
                return region_summary












