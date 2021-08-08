from datetime import datetime


# Base class
class Summary:
    def __init__(self, summary_data):
        # # self._latest_date: datetime.date = datetime.strptime(summary_data['data'][0]['latest_date'], '%Y-%m-%d')
        # self._change_cases: int = int(summary_data['data'][0]['change_cases'])
        # self._change_fatalities: int = int(summary_data['data'][0]['change_fatalities'])
        # self._change_tests: int = int(summary_data['data'][0]['change_tests'])
        # self._change_hospitalizations: int = int(summary_data['data'][0]['change_hospitalizations'])
        # self._change_criticals: int = int(summary_data['data'][0]['change_criticals'])
        # self._change_recoveries: int = int(summary_data['data'][0]['change_recoveries'])
        # self._change_vaccinations: int = int(summary_data['data'][0]['change_vaccinations'])
        # self._change_vaccinated: int = int(summary_data['data'][0]['change_vaccinated'])
        # self._change_vaccines_distributed: int = int(summary_data['data'][0]['change_vaccines_distributed'])
        # self._total_cases: int = int(summary_data['data'][0]['total_cases'])
        # self._total_fatalities: int = int(summary_data['data'][0]['total_fatalities'])
        # self._total_tests: int = int(summary_data['data'][0]['total_tests'])
        # self._total_hospitalizations: int = int(summary_data['data'][0]['total_hospitalizations'])
        # self._total_criticals: int = int(summary_data['data'][0]['total_criticals'])
        # self._total_recoveries: int = int(summary_data['data'][0]['total_recoveries'])
        # self._total_vaccinations: int = int(summary_data['data'][0]['total_vaccinations'])
        # self._total_vaccinated: int = int(summary_data['data'][0]['total_vaccinated'])
        # self._total_vaccines_distributed: int = int(summary_data['data'][0]['total_vaccines_distributed'])
        # self._last_updated: datetime.date = datetime.strptime(summary_data['last_updated'], '%Y-%m-%d %H:%M:%S')


        # self._latest_date: datetime.date = datetime.strptime(summary_data['data'][0]['latest_date'], '%Y-%m-%d')
        self._change_cases: int = int(summary_data['change_cases'])
        self._change_fatalities: int = int(summary_data['change_fatalities'])
        self._change_tests: int = int(summary_data['change_tests'])
        self._change_hospitalizations: int = int(summary_data['change_hospitalizations'])
        self._change_criticals: int = int(summary_data['change_criticals'])
        self._change_recoveries: int = int(summary_data['change_recoveries'])
        self._change_vaccinations: int = int(summary_data['change_vaccinations'])
        self._change_vaccinated: int = int(summary_data['change_vaccinated'])
        self._change_vaccines_distributed: int = int(summary_data['change_vaccines_distributed'])
        self._total_cases: int = int(summary_data['total_cases'])
        self._total_fatalities: int = int(summary_data['total_fatalities'])
        self._total_tests: int = int(summary_data['total_tests'])
        self._total_hospitalizations: int = int(summary_data['total_hospitalizations'])
        self._total_criticals: int = int(summary_data['total_criticals'])
        self._total_recoveries: int = int(summary_data['total_recoveries'])
        self._total_vaccinations: int = int(summary_data['total_vaccinations'])
        self._total_vaccinated: int = int(summary_data['total_vaccinated'])
        self._total_vaccines_distributed: int = int(summary_data['total_vaccines_distributed'])
        # self._last_updated: datetime.date = datetime.strptime(summary_data['last_updated'], '%Y-%m-%d %H:%M:%S')



    @property
    def change_cases(self) -> int:
        return self._change_cases

    # @property
    # def latest_date(self) -> datetime.date:
    #     return self._latest_date

    @property
    def change_fatalities(self) -> int:
        return self._change_fatalities

    @property
    def change_tests(self) -> int:
        return self._change_tests

    @property
    def change_hospitalizations(self) -> int:
        return self._change_hospitalizations

    @property
    def change_criticals(self) -> int:
        return self._change_criticals

    @property
    def change_recoveries(self) -> int:
        return self._change_recoveries

    @property
    def change_vaccinations(self) -> int:
        return self._change_vaccinations

    @property
    def change_vaccinated(self) -> int:
        return self._change_vaccinated

    @property
    def change_vaccines_distributed(self) -> int:
        return self._change_vaccines_distributed

    @property
    def total_cases(self) -> int:
        return self._total_cases

    @property
    def total_fatalities(self) -> int:
        return self._total_fatalities

    @property
    def total_tests(self) -> int:
        return self._total_tests

    @property
    def total_hospitalizations(self) -> int:
        return self._total_hospitalizations

    @property
    def total_criticals(self) -> int:
        return self._total_criticals

    @property
    def total_recoveries(self) -> int:
        return self._total_recoveries

    @property
    def total_vaccinations(self) -> int:
        return self._total_vaccinations

    @property
    def total_vaccinated(self) -> int:
        return self._total_vaccinated

    @property
    def total_vaccines_distributed(self) -> int:
        return self._total_vaccines_distributed


class SummaryAll(Summary):
    def __init__(self, summary_data):
        clean_data = summary_data['data'][0]
        super().__init__(clean_data)
        self._latest_date: datetime.date = datetime.strptime(clean_data['latest_date'], '%Y-%m-%d')
        self._last_updated: datetime.date = datetime.strptime(summary_data['last_updated'], '%Y-%m-%d %H:%M:%S')

    @property
    def latest_date(self) -> datetime.date:
        return self._latest_date

    @property
    def last_updated(self) -> datetime.date:
        return self._last_updated


class ProvinceSummary(Summary):
    def __init__(self, province_summary_data):
        super().__init__(province_summary_data)
        self._province: str = province_summary_data['province']
        self._date: datetime.date = datetime.strptime(province_summary_data['date'], '%Y-%m-%d')

    @property
    def province(self) -> str:
        return self._province

    @property
    def date(self) -> datetime.date:
        return self._date


class HealthRegionSummary(Summary):
    def __init__(self, health_region_summary_data):
        super().__init__(health_region_summary_data)
        self._hr_uid: int = health_region_summary_data['hr_uid']
        self._date: datetime.date = datetime.strptime(health_region_summary_data['date'], '%Y-%m-%d')

    @property
    def hr_uid(self) -> int:
        return self._hr_uid

    @property
    def date(self) -> datetime:
        return self._date
