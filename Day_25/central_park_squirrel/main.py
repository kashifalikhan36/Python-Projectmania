import pandas

data=pandas.read_csv("Day_25/central_park_squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_csv=data.to_csv
color_data=data["Primary Fur Color"]

new_data={}
gray=0
cinnamon=0
black=0
for i in color_data:
    if i=="Gray":
        gray+=1
    elif i=="Cinnamon":
        cinnamon+=1
    elif i=="Black":
        black+=1
new_data={
    "fur color": ["Gray","Cinnamon","Black"],
    "Count": [gray,cinnamon,black]
}

last_output=(pandas.DataFrame(new_data)).to_csv("Day_25/central_park_squirrel/output.csv")
print(f"Gray Bird: {gray} Cinnamon Bird: {cinnamon} Black Bird: {black}")
