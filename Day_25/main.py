import pandas

data=pandas.read_csv("Day_25/weather_data.csv")
data_dict=data["temp"]
print(data_dict.max())
    
