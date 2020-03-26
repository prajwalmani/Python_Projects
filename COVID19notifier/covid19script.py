# This program only run on Windows 10 OS
# if you have linux flavours OS then u can use dbus module to communicate with the OS

# import modules
from win10toast import ToastNotifier #pip install win10toast
from bs4 import BeautifulSoup      #pip install bs4
import requests                   #pip install request
import time

# variable decalration
country = "India" # you u can add your country name or other place
notification_duration = 100  # seconds
refresh_time = 1# minutes
URLLink = "https://www.worldometers.info/coronavirus/"  # link
data_check =[]

#function to clean the data
def data_cleanup(array):
    L = []
    for i in array:
        i = i.replace("+", "")
        i = i.replace("-", "")
        i = i.replace(",", ".")
        if i == "":
            i = "0"
        L.append(i.strip())
    return L

#infinte loop
while True:
    try:
        html_page = requests.get(URLLink) #to fetch the contents of the link
    except requests.exceptions.RequestException as e:
        print(e)  # Connection error
        continue
    bs = BeautifulSoup(html_page.content, 'html.parser') #parsing of the data
    search = bs.select("div tbody tr td") #to select the data whch is inside this tag
    start = -1
    for i in range(len(search)):
        if search[i].get_text().find(country) != -1: # to find particular country data
            start = i
            break
    data = []
    for i in range(1, 8):
        try:
            data += [search[start + i].get_text()]
        except:
            data += [0]

    data = data_cleanup(data) #call the data_cleanup function

    # message that has to be displayed on notification bar
    message = "Total infected = {}, New Case = {}, Total Deaths = {}, New Deaths = {}, Recovred = {}, Active Case = {}, Serious Critical = {}".format(*data)
    # this if condition to display notification only if the data changes or else it will go to sleep
    # if you want the notification to be frequent then you should remove the below uf condition
    if data_check != data:
       data_check = data
       toaster = ToastNotifier() #create object for ToasrNotifier()
       toaster.show_toast("Coronovirus in {}".format(country), message, duration=notification_duration) # to show notification
    else:
     time.sleep(refresh_time * 60)
