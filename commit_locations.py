import csv, json
from geonamescache import GeonamesCache

gc = GeonamesCache()
countries = gc.get_countries()
countries_by_names = gc.get_countries_by_names()
us_states = gc.get_us_states()

def test_locs(locs):
    for loc in locs:
        loc = loc.strip().strip('.').lower().title()
        if loc in countries_by_names:
            return loc
        elif loc.upper() in us_states:
            return 'United States'
        elif loc.upper() in ['USA', 'US', 'U.S.', 'U.S.A.']:
            return 'United States'
        elif loc.upper() in ['GB', 'UK', 'U.K.']:
            return 'United Kingdom'
        elif loc.upper() in countries:
            return countries[loc.upper()]['name']

def determine_country(locstr):
    """Try to determine country from given location string."""

    # try different split chars, 1st comma, 2nd slash, 3rd hyphen, last space
    for sc in [',', '/', '-', ' ']:
        country = test_locs(locstr.split(sc))
        if country is not None:
            return country
#    print loc

commits_by_countries = {}

fcsv = open('langcnt_by_loc.csv', 'rb')
reader = csv.reader(fcsv)
headers = reader.next()
for record in reader:
    loc, langcnt, repository_language = record
    country = determine_country(loc)
    if country is not None:
        if country not in commits_by_countries:
            commits_by_countries[country] = {'commits': 0}
        commits_by_countries[country]['commits'] += int(langcnt)
fcsv.close()

# calc commit ratio per capita
for c in commits_by_countries:
    popcnt = countries_by_names[c]['population']
    commits_by_countries[c]['commits_per_capita'] = (commits_by_countries[c]['commits'] / float(popcnt)) if popcnt > 0 else 0

# write data to csv
wcsv = open('github_commits_by_country.csv', 'wb')
writer = csv.writer(wcsv, quoting=csv.QUOTE_MINIMAL)
writer.writerow(['Country', 'Commit Count', 'Commits per Capita', 'Population'])
for c in commits_by_countries:
    writer.writerow([c, commits_by_countries[c]['commits'], commits_by_countries[c]['commits_per_capita'], countries_by_names[c]['population']])
wcsv.close()
