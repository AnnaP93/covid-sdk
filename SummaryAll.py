from Summary import Summary
from datetime import datetime


class SummaryAll(Summary):
    def transform(self, data):
        if data is not None:
            return data
        else:
            return 0

    def __init__(self, summary_data):
        clean_data = summary_data['data'][0]
        super().__init__(clean_data)
        self._latest_date: datetime.date = datetime.strptime(self.transform(clean_data['latest_date']), '%Y-%m-%d')
        self._last_updated: datetime.date = datetime.strptime(self.transform(summary_data['last_updated']), '%Y-%m-%d %H:%M:%S')
        self._change_vaccines_distributed: int = int(self.transform(clean_data['change_vaccines_distributed']))
        self._total_vaccines_distributed: int = int(self.transform(clean_data['total_vaccines_distributed']))

    @property
    def latest_date(self) -> datetime.date:
        return self._latest_date

    @property
    def last_updated(self) -> datetime.date:
        return self._last_updated

    @property
    def change_vaccines_distributed(self) -> int:
        return self._change_vaccines_distributed

    @property
    def total_vaccines_distributed(self) -> int:
        return self._total_vaccines_distributed
