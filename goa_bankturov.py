import json, requests

#https://www.bankturov.ru/search-online?presearch=1&presearch_type=otour&departure=12&destination=3_18,17,16&date_from=02.01.2020&date_till=02.01.2020&man=2

url = 'http://search.bankturov.ru/search/?SID=null&departure_id=12&destination_id=3_18,17,16&adult_num=2&child_num=1&child_ages=2%5B%5D=0&arrivalDateFrom=02.01.2019&arrivalDateTo=02.01.2019&nonstop=true&ticket=true&nightsStart=6&nightsEnd=14&hotelStars=&hotels%5B%5D=39564&mealType=&valute=RUB&offer_currency=RUB'

#&source=search_online_page_otour&_=1542555642619'

data = requests.get(url=url)
binary = data.content
jres = json.loads(binary)
cost = 0

for data in jres['data']:
    print (data['residenses']['room_name']) 

#    if data['residenses']['room_name']=="Superior Garden View A":
#    	print data['date']
#    	print data['residenses']['original_hotel_name']
#    	print data['residenses']['room_name']
#    	print data['costValues']['RUB']['source'],"RUB"
#    	print data['costValues']['RUB']['surcharged'],"RUB"
#    	print "-"
#    	cost = data['costValues']['RUB']['surcharged']

maxcost = 0
mincost = 999999
lastcost = 0

#off
"""

try:
	f = open('goa_bankturov.txt')
	line = f.readline()
	while line:
 	   if maxcost<int(line): 
		maxcost = int(line)
 	   if mincost>int(line): 
		mincost = int(line)
	   lastcost = int(line)
 	   line = f.readline()
	f.close()
except:
	print ""

f = open('goa_bankturov.txt', 'a')
if (cost!=0):
	f.write(str(cost))
f.write("\n")
f.close()

"""
#end off


diff = lastcost - cost

print ("diff:",diff)
print ("max:",maxcost)
print ("min:",mincost)

print ("---")