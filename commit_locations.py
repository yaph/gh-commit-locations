# -*- coding: utf-8 -*-
# This is by far the ugliest Python script I ever wrote
# withoud cities 14954 location string remain unresovled
# with unique city names 7754 location string remain unresovled

import csv, json, re
from geonamescache import GeonamesCache

commits_by_countries = {}
gc = GeonamesCache()
countries = gc.get_countries()
countries_by_names = gc.get_countries_by_names()
us_states = gc.get_us_states()
us_states_by_names = gc.get_us_states_by_names()

re_ignore = re.compile(r'[\.\(\)\d-]')
re_ws = re.compile(r'\w{2,}')


def test_locs(locs):
    for loc in locs:
        loc = loc.strip().lower().capitalize()
        locupper = loc.upper()
        if loc in countries_by_names:
            return loc
        elif locupper in us_states:
            return 'United States'
        elif locupper in us_states_by_names:
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
            cities = gc.get_cities_by_name(loc)
            # only consider unique city names
            if 1 == len(cities):
                return countries[cities[0].values()[0]['countrycode']]['name']


def determine_country(locstr, langcnt):
    """Try to determine country from given location string."""

    locstr = re.sub(re_ws, ' ', re.sub(re_ignore, ' ', locstr))
    # try different split chars, 1st comma, 2nd slash, 3rd hyphen, last space
    for sc in [',', '/', '-', ' ']:
        country = test_locs(locstr.split(sc))
        if country is not None:
            return country
    print('%s, %d' % (loc, langcnt))


fcsv = open('langcnt_by_loc.csv', 'rb')
reader = csv.reader(fcsv)
headers = reader.next()
for record in reader:
    loc, langcnt, repository_language = record
    country = determine_country(loc, langcnt)
    if country is not None:
        if country not in commits_by_countries:
            commits_by_countries[country] = {'commits': 0}
        commits_by_countries[country]['commits'] += int(langcnt)
fcsv.close()

# calc commit ratio per capita
for c in commits_by_countries:
    popcnt = float(countries_by_names[c]['population'])
    if popcnt > 0
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
