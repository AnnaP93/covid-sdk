from Summary import Summary
from datetime import datetime


class SummaryByRegion(Summary):
    def transform(self, data):
        if data is not None:
            return data
        else:
            return 0

    def __init__(self, health_region_summary_data):
        super().__init__(health_region_summary_data)
        self._hr_uid: int = int(self.transform(health_region_summary_data['hr_uid']))
        self._date: datetime.date = self.transform(datetime.strptime(health_region_summary_data['date'], '%Y-%m-%d'))

    @property
    def hr_uid(self) -> int:
        return self._hr_uid

    @property
    def date(self) -> datetime:
        return self._date
