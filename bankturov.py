import json, requests

url = 'http://search.bankturov.ru/search/?SID=null&departure_id=1281&destination_id=59&adult_num=2&child_num=1&child_ages%5B%5D=0&arrivalDateFrom=02.03.2019&arrivalDateTo=16.03.2019&nonstop=true&ticket=true&nightsStart=18&nightsEnd=22&hotelStars=&hotels%5B%5D=39564&mealType=&valute=RUB&offer_currency=RUB&source=search_online_page_otour&_=1542555642619'

data = requests.get(url=url)
binary = data.content
jres = json.loads(binary)
cost = 0

for data in jres['data']:
    if data['residenses']['room_name']=="Deluxe Garden View B (with balcony)":
        print data['date']
        print data['residenses']['original_hotel_name']
        print data['residenses']['room_name']
        print data['costValues']['RUB']['source'],"RUB"
        print data['costValues']['RUB']['surcharged'],"RUB"
        print "-"
        cost = data['costValues']['RUB']['source']

maxcost = 0
mincost = 999999
lastcost = 0

try:
	f = open('bankturov.txt')
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

f = open('bankturov.txt', 'a')
if (cost!=0):
	f.write(str(cost))
f.write("\n")
f.close()

diff = lastcost - cost

print "diff:",diff
print "max:",maxcost
print "min:",mincost

print "---"