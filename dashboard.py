import wbdata
import pandas
import matplotlib.pyplot as plt
import datetime
countries = ["AR"]
date = (datetime.datetime(2002, 1, 1), datetime.datetime.now())
indicators_gdp = {'NY.GDP.MKTP.CD': 'GDP'}
df_gdp = wbdata.get_dataframe(indicators_gdp, country="AR", data_date=date)
indicators_unemploy = {'UNEMPSA_': 'unemployment rate%'}
df_unemploy = wbdata.get_dataframe(indicators_unemploy, country="AR", data_date=date)
df_gdp = df_gdp.iloc[::-1] / 1000000000
df_unemploy = (df_unemploy.iloc[::-1])


def make_dashboard(gdp, unemploy, title):
    fig, ax = plt.subplots()
    ax.plot(gdp, color="red", marker="o")
    ax.set_xlabel("year", fontsize=14)
    ax.set_ylabel("GDP(billion)", color="red", fontsize=14)
    ax2 = ax.twinx()
    ax2.plot(unemploy, color="blue", marker="o")
    ax2.set_ylabel("unemployment rate%", color="blue", fontsize=14)
    plt.title(title)
    plt.show()


title = "relationship between gdp and unemployment rate in Argentina"
make_dashboard(df_gdp, df_unemploy, title)
