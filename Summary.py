from datetime import datetime


# Base class
from typing import Union


class Summary:
    def transform(self, data):
        if data is not None:
            return int(data)
        else:
            return 0

    def __init__(self, summary_data):
        self._change_cases: int = self.transform(summary_data['change_cases'])
        self._change_fatalities: int = self.transform(summary_data['change_fatalities'])
        self._change_tests:int = self.transform(summary_data['change_tests'])
        self._total_cases: int = self.transform(summary_data['total_cases'])
        self._change_hospitalizations: int = self.transform(summary_data['change_hospitalizations'])
        self._change_criticals: int = self.transform(summary_data['change_criticals'])
        self._change_recoveries: int = self.transform(summary_data['change_recoveries'])
        self._change_vaccinations: int = self.transform(summary_data['change_vaccinations'])
        self._change_vaccinated: int = self.transform(summary_data['change_vaccinated'])
        self._total_fatalities: int = self.transform(summary_data['total_fatalities'])
        self._total_tests: int = self.transform(summary_data['total_tests'])
        self._total_hospitalizations: int = self.transform(summary_data['total_hospitalizations'])
        self._total_criticals: int = self.transform(summary_data['total_criticals'])
        self._total_recoveries: int = self.transform(summary_data['total_recoveries'])
        self._total_vaccinations: int = self.transform(summary_data['total_vaccinations'])
        self._total_vaccinated: int = self.transform(summary_data['total_vaccinated'])

    @property
    def change_cases(self) -> int:
        return self._change_cases

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




