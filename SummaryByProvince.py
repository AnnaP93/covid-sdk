from Summary import Summary
from datetime import datetime


class SummaryByProvince(Summary):
    def transform(self, data):
        if data is not None:
            return data
        else:
            return 0

    def __init__(self, province_summary_data):
        super().__init__(province_summary_data)
        self._province: str = str(self.transform(province_summary_data['province']))
        self._date: datetime.date = datetime.strptime(self.transform(province_summary_data['date']), '%Y-%m-%d')
        self._change_vaccines_distributed: int = int(self.transform(province_summary_data['change_vaccines_distributed']))
        self._total_vaccines_distributed: int = int(self.transform(province_summary_data['total_vaccines_distributed']))

    @property
    def province(self) -> str:
        return self._province

    @property
    def date(self) -> datetime.date:
        return self._date

    @property
    def change_vaccines_distributed(self) -> int:
        return self._change_vaccines_distributed

    @property
    def total_vaccines_distributed(self) -> int:
        return self._total_vaccines_distributed
