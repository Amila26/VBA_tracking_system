import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import os
from pathlib import Path

html_path = Path(r'C:\Users\Amila Indika\Desktop\Highlander\planday\PlandayMay.html')


with open(html_path, 'r', encoding='utf-8') as file: # Set html File Path
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

date_period = soup.find('span', class_="date-bar__label").text # Extract_date_period
month = date_period[-3:] # Extract Month
Year = datetime.datetime.now().year




shiftName = soup.find("div" , class_="styled__StyledSummaryDiv-sc-fz2x68-1 kchBke").text
print(shiftName)

extract_data = pd.DataFrame(columns=["Date","EmpName", "InOutTime"])


# print(soup.prettify())
print(date_period)
calender_cell = soup.findAll('div', class_="calendar__cell")
# print(type((soup.findAll('div',class_="calendar__cell")[0].get('class')))
#print(" ".join(eliment.get("class")) == "calendar__cell calendar__cell--passive")

print(calender_cell[0])
# remove calander__cell--passive only keep  active clander cell

active_calender_cell = []
print(len(calender_cell))
for eliment in calender_cell:
    if len(eliment.get('class')) != 2:
        active_calender_cell.append(eliment)




print(active_calender_cell)
for entry in active_calender_cell:
    date = entry.find("div",class_="calendar__cell__date calendar__cell__date--active").text # active Date
    shift = entry.findAll("div",class_="calendar__cell__element shift-strip shift-strip--approved")
    Date = []
    Emp_Name = []
    InOut = []
    Data_dict = {}
    for individual in shift:
        active_date = str(Year)+"/"+month+"/"+str(date)
        emp_name = individual.find("span", class_="shift-strip__title").text
        In_Out = individual.find("span",class_="shift-strip__time").text

        Date.append(active_date)
        Emp_Name.append(emp_name)
        InOut.append(In_Out)

    Data_dict["Date"] = Date
    Data_dict["EmpName"] = Emp_Name
    Data_dict["InOutTime"] = InOut

    df1 = pd.DataFrame(Data_dict)

    extract_data = pd.concat([extract_data, df1],ignore_index=True)


print(extract_data)

file_name = shiftName+"_"+date_period.replace(" ","")+".xlsx"
folder_path = r"C:\Users\Amila Indika\Desktop\Highlander\planday\timesheet"
file_path = os.path.join(folder_path,file_name)
extract_data.to_excel(file_path,index=False)











