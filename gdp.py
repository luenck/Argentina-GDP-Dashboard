import wbdata
import pandas
countries = ["AR"]
indicators_gdp = {'NY.GDP.MKTP.CD': 'GDP'}
df_gdp = wbdata.get_dataframe(indicators_gdp, country="AR", convert_date=False)
print(df_gdp.head())
print(type(df_gdp))
