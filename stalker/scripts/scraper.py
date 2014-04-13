def run():
    import urllib2
    from stalker.models import Asteroid
    from bs4 import BeautifulSoup
    import re
    from datetime import datetime

    target_url = 'http://neo.jpl.nasa.gov/ca/'
    page = urllib2.urlopen(target_url)
    soup = BeautifulSoup(page.read())
    showed_asteroids = Asteroid.objects.filter(next_to_earth=True)
    for asteroid in showed_asteroids:
        asteroid.next_to_earth = False
        asteroid.save()
    for tr in soup.find_all('table')[9].find_all('tr')[3:-2]:
        asteroid = tr.find_all('td')
        url = asteroid[0].contents[0].contents[0].get('href')
        name = asteroid[0].contents[0].contents[0].contents[0]
        name = ' '.join(name.split())
        name= re.sub('[()]', '', name)
        print url
        print name
        date =  asteroid[1].contents[0].contents[0]
        date = ' '.join(date.split())
        date = datetime.strptime(date, '%Y-%b-%d').date()
        print date
        distance =  float(asteroid[2].contents[0].contents[0]) * 149597870.691
        print distance
        diameter = asteroid[4].contents[0].contents[0]
        print diameter
        velocity = float(asteroid[6].contents[0].contents[0])
        if Asteroid.objects.filter(name=name).exists():
            asteroid = Asteroid.objects.get(name=name)
            asteroid.closest_date = date
            asteroid.closest_distance = distance
            asteroid.diameter = diameter
            asteroid.velocity = velocity
            asteroid.next_to_earth = True
            asteroid.save()
        else:
            new_asteroid = Asteroid(name=name, closest_date=date, closest_distance=distance, diameter=diameter, velocity=velocity, next_to_earth=True)
            new_asteroid.save()
