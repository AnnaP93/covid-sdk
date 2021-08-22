from CovidSDK import CovidSdk
from Provinces import Provinces
from SummaryAll import SummaryAll
from SummaryByRegion import SummaryByRegion

if __name__ == '__main__':
    summary_all = CovidSdk.summary(Provinces.All)
    print(summary_all.total_cases)

    summary_qc = CovidSdk.summary(province=Provinces.Yukon)
    print(summary_qc.change_criticals)

    summary_yk = CovidSdk.summary(province=Provinces.Yukon)
    print(summary_yk.date)

    summary_hr = CovidSdk.summary_by_region(3526)
    if isinstance(summary_hr, SummaryByRegion):
        print(summary_hr.change_cases)
    else:
        print("The health region ID is not found. Please try entering it again.")


# NorthYorkHealthRegion = CovidSdk.summary_by_region(north_york_id)
# NorthYorkHealthRegion = CovidSdk.health_region(north_york_id).summary()











