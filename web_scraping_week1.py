import requests
import os
import csv

api_key = 'DrP4hdZ7m6qTa3Zhm6fXgpx1esUUz27acB7BdwT8'

url = 'https://api.nasa.gov/neo/rest/v1/feed'
start_date = '2016-07-01'
end_date = '2016-07-08'
finish_date = '2016-07-30'

response1 = requests.get(url,params={
    'start_date':start_date,
    'end_date':end_date,
    'api_key':api_key
})
asteroids1 = response1.json()

#başlıklar için(csv dosyasının sistemde old knt et. yok ise bu başlıkları ekle.
liste = []
for i in (asteroids1['near_earth_objects']['2016-07-01'][0]).keys():
    liste.append(i)
if not os.path.exists("asteroids.cvs"):
    with open("asteroids.cvs", "a",newline="") as cvsfile:
        writer = csv.writer(cvsfile)
        liste = (asteroids1['near_earth_objects']['2016-07-01'][0]).keys()
        writer.writerow(liste)



liste = list(asteroids1['near_earth_objects']) #7 günlük tarih aralığını bulduk
liste.sort()# tarihe göre sıraladık
for i in liste[:-1]:
    new_list = asteroids1['near_earth_objects'][i]
    print(i)
    for i in new_list:
        print(i)

###
loop = True
while loop:

    print(asteroids1['links']['next'])
    url = asteroids1['links']['next']
    response1 = requests.get(url)
    asteroids1 = response1.json()

    liste = list(asteroids1['near_earth_objects'])  # 7 günlük tarih aralığını bulduk
    liste.sort()  # tarihe göre sıraladık

    for i in liste[:-1]:
        if i <= finish_date:
            new_list = asteroids1['near_earth_objects'][i]
            print(i)
            for i in new_list:
                print(i)
        else:
            loop = False
            break

