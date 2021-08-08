import requests

# class ProvinceSummary
class SummarySplit:
    def __init__(self, summary_split_data=None):
        if summary_split_data is None:
            return

        self._province: str = summary_split_data['province']
        self._change_cases: int = int(summary_split_data['change_cases'])
        self._change_fatalities: int = int(summary_split_data['change_fatalities'])
        self._change_tests: int = int(summary_split_data['change_tests'])

    @staticmethod
    def split_by_province(province):
        province_split_response = requests.get('https://api.covid19tracker.ca/summary/split')
        province_split_data = province_split_response.json()
        for item in province_split_data['data']:
            if item['province'] == province:
                x = SummarySplit(item)
                return x

    @property
    def change_cases(self) -> int:
        return self._change_cases

    def __repr__(self):
        return 'Change cases: {0}'.format(self._change_cases)

# ontario_data = SummarySplit.split_by_province('ON')
# print(ontario_data.change_cases)

#quebec_data = SummarySplit.split_by_province('QC')
#print(quebec_data.change_cases)


    # define properties
# create method for each province: SummarySplit.Ontario(); SummarySplit.Quebec()

