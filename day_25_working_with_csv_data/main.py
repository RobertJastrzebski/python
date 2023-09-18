# with open("weather_data.csv",mode="r") as file:
#     data = file.readlines()
#     print(data)

# -----------modół csv-----------------------------
# import csv
#
# with open("weather_data.csv") as data_file:
#     data= csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1]!= "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
# -----------------pandas - pandas traktuje kolumny jak atrybuty--------------------------------
import pandas

data= pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel= len(data[data["Primary Fur Color"]=="Gray"])
red_squirrel= len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel= len(data[data["Primary Fur Color"]=="Black"])

print(grey_squirrel)
print(red_squirrel)
print(black_squirrel)

data_dict = {
    "Fur Color" : ["Grey","Cinamon", "Black"],
    "Count": [grey_squirrel,red_squirrel,black_squirrel]
}
df=pandas.DataFrame(data_dict)
print(df)
# lista_temp =data["temp"].to_list()
# srednia= data["temp"].mean()
# max= data["temp"].max()
# print(max)
# print(data)
# print(data["day"])
# monday= data[data.day == "Monday"]
# print(data[data.temp==data.temp.max()])
# print(monday)



