# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
import pandas
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# length = len(temp_list)
#max = data["temp"].max()
# print(data[data.temp==data.temp.max()])

# data_dict = {
#     "student":["anis","sibber"],
#     "score":[20,23]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv   ")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel = data[data["Primary Fur Color"]=="Gray"]
print(gray_squirrel)















