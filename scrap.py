# ............. opentender .............
import requests
from bs4 import BeautifulSoup
url = 'https://opentender.eu/start'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find_all('li', class_='portal-link')

f = open('TendorData.csv','w')
f.write('Country Name,No of Tendors \n')
#          ---------onle ONE Class used  ---------> First Method
class TendorClass: 
    for i in data:
        country = i.find('a').text
        # print(country)
        
        tendor = i.find('div').text
        tendor_data =  ''.join(i for i in tendor.split(','))
        # print(tendor_data)
        f.write(f'{country},{tendor_data}\n')
        print('\n')
    f.close()

TendorClass()



#          ----------- Class & Function/Method used  ---------> Second Method
# class TendorClass: 
#     def data():
#         for i in data:
#             country = i.find('a').text
#             # print(country)
            
#             tendor = i.find('div').text
#             tendor_data =  ''.join(i for i in tendor.split(','))
#             # print(tendor_data)

#             f.write(f'{country},{tendor_data}\n')
#         f.close()
# TendorClass.data()



#          ----------- Clss & Functions/ Method  with Positional Arguments ---------> Third Method
# class TendorClass: 
#     def data(self):
#         for i in data:
#             country = i.find('a').text
#             print(country)
            
#             tendor = i.find('div').text
#             tendor_data =  ''.join(i for i in tendor.split(','))
#             # print(tendor_data)
# object = TendorClass()
# object.data()












