import json, requests

#https://www.bankturov.ru/search-online?presearch=1&presearch_type=otour&departure=12&destination=3_18,17,16&date_from=02.01.2020&date_till=02.01.2020&man=2

url = 'https://search.bankturov.ru/api/mobile/v1/search?departure_id=12&destination_id=3&adult_num=2&child_num=1&child_ages%5B%5D=1&arrivalDateFrom=02.01.2020&arrivalDateTo=02.01.2020&nonstop=true&ticket=true&nightsStart=6&nightsEnd=14&resort_id%5B%5D=16&minCost=0&maxCost=150000&valute=RUB&offer_currency=RUB'

data = requests.get(url=url)
binary = data.content
jres = json.loads(binary)
cost = 0

#print (jres["data"]["rows"])

for data in jres["data"]["rows"]:
    print data["to_class"]
    print data["costValues"]

print ("---")
