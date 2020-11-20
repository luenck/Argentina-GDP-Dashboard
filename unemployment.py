import wbdata
import pandas
countries = ["AR"]
#index = wbdata.search_indicators("unemployment rate", source=None, topic=None)
#print(index)
indicators_unemploy = {'UNEMPSA_': 'unemployment rate%'}
df_unemploy = wbdata.get_dataframe(indicators_unemploy, country="AR", convert_date=False)
print(df_unemploy.head(5))
print(type(df_unemploy))