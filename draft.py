from CovidSDK import CovidSdk
# summary = covid_sdk.summary()
# print(summary.total_cases) - PEOPLE WILL LOVE YOU
# print(summary.data[0]['total_cases']) - NO ONE WILL USE THIS!!!!!!

# http.get("https://api.covid19tracker.ca/vaccines/age-groups/province/ON")


# Using just "Summary" as a class might conflict with other packages. Thus, it's better to have a more descriptive and
# logical SDK point of entrance.
import requests


class Reports:
    pass


class Case:
    pass


# Option 1
class Cases:
    # Option 1
    @staticmethod
    def cases_all() -> list[Case]:
        cases = requests.get('https://api.covid19tracker.ca/cases')
        pass

    # Option 1
    @staticmethod
    def case(id) -> Case:
        cases = requests.get('https://api.covid19tracker.ca/cases/' + id)
        pass

class Fatalities:
    pass


# class CovidSdk:
#     @staticmethod
#     def summary() -> Summary:
#         data = requests.get('https://api.covid19tracker.ca/summary')
#         return Summary(data.json())
#
#     @staticmethod
#     def fatalities() -> Fatalities:
#         pass
#
#     # Option 1
#     @staticmethod
#     def cases() -> Cases:
#         return Cases()
#
#     # Option 2
#     @staticmethod
#     def cases_all() -> list[Case]:
#         cases = requests.get('https://api.covid19tracker.ca/cases')
#         pass
#
#     # Option 2
#     @staticmethod
#     def case(id) -> Case:
#         cases = requests.get('https://api.covid19tracker.ca/cases/' + id)
#         pass

cases = CovidSdk.cases()
CovidSdk.cases().cases_all()    # Option 1  #one method (in static class) is called via another method (in static class)
CovidSdk.cases().case(123)      # Option 1
CovidSdk.case(123)              # Option 2
CovidSdk.cases_all()            # Option 2  #final result is returned via a single touch point (via a single class)



# My version
# class SummaryTest():
#     def __init__(self):
#         self._summary_data = requests.get('https://api.covid19tracker.ca/summary')
#         self._latest_update = self._summary_data.json()['data'][0]['latest_date']
#
#     def refresh(self):
#         self.__init__()
#
#     @property
#     def latest_update(self) -> str:
#         #latest_update = self._summary_data.json()['data'][0]['latest_date']
#         #return latest_update
#         return self._latest_update
#
#     @property
#     def total_cases(self):
#         total_cases = int(self._summary_data.json()['data'][0]['total_cases'])
#         return total_cases
#
#
# if __name__ == '__main__':
#     object = SummaryTest()
#     latest_update = object.latest_update
#     latest_update2 = object.latest_update
#     object.refresh()
#     latest_update3 = object.latest_update
#     latest_update4 = object.latest_update
#     total_cases = object.total_cases
#
#     print(latest_update)
#     print(total_cases)








# option 1
# CovidSdk.summary().ON() - ontario province
# CovidSdk.summary().QC() - quebec province
# CovidSdk.summary().all() - all

# option 2 +
# CovidSdk.summary() - all
# CovidSdk.summary('ON') - ontario province
# CovidSdk.summary('QC') - ontario province

# option 3
# CovidSdk.summary() - all
# CovidSdk.summary(Provinces.Ontario) - ontario province
# CovidSdk.summary(Provinces.Quebec) - ontario province


# def summary2(province: Provinces):
#     print(province.value)
#
#
# def summary3(province: str):
#     print(province)
#
#
# summary2(province=Provinces.Ontario)
# summary3(province='newfoundland and labrador')