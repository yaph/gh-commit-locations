# -*- coding: utf-8 -*-
# This is by far the ugliest Python script I ever wrote
# withoud cities 14954 location string remain unresovled
# with unique city names 6345 (number is not up to date) location string remain unresovled
# with largest city name 4623 location string remain unresovled
# with manually resolved locations 3333 location string remain unresovled

import csv, json, re
from geonamescache import GeonamesCache
from loclists import check_unresolved

commits_by_countries = {}
countries_by_locstr = {}
gc = GeonamesCache()
countries = gc.get_countries()
countries_by_names = gc.get_countries_by_names()
us_states = gc.get_us_states()
us_states_by_names = gc.get_us_states_by_names()

re_ignore = re.compile(r'[\.\(\)\d-]')
re_ws = re.compile(r'\s{2,}')


def test_locs(locs):
    for loc in locs:
        loc = loc.strip().lower()
        loctitle = loc.title()
        locupper = loc.upper()
        if loc in countries_by_names:
            return loc
        elif loctitle in countries_by_names:
            return loctitle
        elif 2 == len(loc) and locupper in us_states:
            return 'United States'
        elif loc in us_states_by_names or loctitle in us_states_by_names:
            return 'United States'
        elif locupper in ['USA', 'US']:
            return 'United States'
        elif locupper in ['GB', 'UK']:
            return 'United Kingdom'
        elif locupper in countries:
            return countries[locupper]['name']
        elif locupper in countries:
            return countries[locupper]['name']
        else:
            for ll in [loc, loctitle]:
                cities = gc.get_cities_by_name(ll)
                # unique city names
                lencities = len(cities)
                if 1 == lencities:
                    return countries[cities[0].values()[0]['countrycode']]['name']
                # assume the largest city
                elif lencities > 1:
                    largestcity = sorted([(city['population'], city['countrycode']) for cdict in cities for gid, city in cdict.items()])[-1]
                    return countries[largestcity[-1]]['name']


def determine_country(locstr, langcnt):
    """Try to determine country from given location string."""

    locstr = re.sub(re_ws, ' ', re.sub(re_ignore, ' ', locstr)).strip()

    if locstr in countries_by_locstr:
        return countries_by_locstr[locstr]

    # try different split chars
    for sc in [',', '/', '-', ' ', ':', '#', '->']:
        country = test_locs(locstr.split(sc))
        if country is not None:
            countries_by_locstr[locstr] = country
            return country

    # check manually resolved locations
    country = check_unresolved(locstr.lower())
    if country is not None:
        countries_by_locstr[locstr] = country
        return country

    print('%s, %d' % (locstr, langcnt))


fcsv = open('langcnt_by_loc.csv', 'rb')
reader = csv.reader(fcsv)
headers = reader.next()
for record in reader:
    loc, langcnt, repository_language = record
    if loc.startswith('http://'): continue
    langcnt = int(langcnt)
    country = determine_country(loc, langcnt)
    if country is not None:
        if country not in commits_by_countries:
            commits_by_countries[country] = {'commits': 0}
        commits_by_countries[country]['commits'] += langcnt
fcsv.close()

# calc commit ratio per capita
for c in commits_by_countries:
    if c not in countries_by_names:
        print '### %s' % c
        continue
    popcnt = float(countries_by_names[c]['population'])
    if popcnt > 0:
        by_capita = commits_by_countries[c]['commits'] / popcnt
        by_100k = round(by_capita * 100000, 2)
    else:
        by_capita = 0
        by_100k = 0
    commits_by_countries[c]['commits_per_capita'] = by_capita
    commits_by_countries[c]['commits_per_100k'] = by_100k

# write data to csv
wcsv = open('github_commits_by_country.csv', 'wb')
writer = csv.writer(wcsv, quoting=csv.QUOTE_MINIMAL)
writer.writerow(['Country', 'Commit Count', 'Commits per Capita', 'Commits per 100,000 People', 'Population'])
for c in commits_by_countries:
    writer.writerow([c, commits_by_countries[c]['commits'], commits_by_countries[c]['commits_per_capita'], commits_by_countries[c]['commits_per_100k'], countries_by_names[c]['population']])
wcsv.close()
