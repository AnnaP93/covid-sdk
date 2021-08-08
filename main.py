from CovidSDK import CovidSdk
from Provinces import Provinces



if __name__ == '__main__':
    summary_all = CovidSdk.summary(Provinces.All)
    print(summary_all.total_cases)

    summary_qc = CovidSdk.summary(province=Provinces.Quebec)
    print(summary_qc.total_cases)
    summary_yk = CovidSdk.summary(province=Provinces.Yukon)
    print(summary_yk.total_cases)














