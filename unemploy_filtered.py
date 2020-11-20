import wbdata
import pandas

countries = ["AR"]
# index = wbdata.search_indicators("unemployment rate", source=None, topic=None)
# print(index)
indicators_unemploy = {'UNEMPSA_': 'unemployment rate%'}
df_unemploy_fil = wbdata.get_dataframe(indicators_unemploy, country="AR", convert_date=False)
# print(df_unemploy)
df_unemploy_fil = df_unemploy_fil.reset_index()
for i in range(len(df_unemploy_fil)):
    if df_unemploy_fil.iloc[i,1] > 8.5:
        print(df_unemploy_fil.iloc[i, 0], df_unemploy_fil.iloc[i, 1])
