# README

A geographic map that displays GitHub commits by countries. [View it at bl.ocks.org](http://bl.ocks.org/2727882)

## Map Data

User location data of 1,533,954 million commit messages from the GitHub timeline served as the basis to create this map. Data was obtained from the [GitHub Archive](http://www.githubarchive.org/) public dataset via Google's BigQuery service.

## Country Identification

Users can enter virtually anything they like in their GitHub Location setting, some real world examples include: "right behind you", "Earth", "The moon", "arrakis" and "The Internet". Fortunately, most provided locations are more realistic and allow for automatic identification of countries.

To do so I wrote some Python scripts you find in [this repo](https://github.com/yaph/gh-commit-locations) and a Python library called [geonamescache](https://github.com/yaph/geonamescache) that provides access to a small part of the data available from [GeoNames](http://www.geonames.org/) without requests to their Web service.

## Caveats

While the official names for the world's countries are unique, city names are not. There is more than one San Francisco, but when a user specified "San Francisco" I assumed the largest city with this name, i. e. the one in the US. The same applies for many other city names.

I also identified some countries manually, thanks [Google Search](https://www.google.com/), but had to draw the line at some point, so that location data from 41,054 commits (not included in the 1.5 million above) remain unresolved.

## What is on the Map

By default [the map](http://bl.ocks.org/2727882) displays the number of commits per 100,000 inhabitants using different color values from a diverging color range.

To make the map more interactive and hopefully more useful, I added controls to choose different regions of the world, other data ranges, i. e. total number of commits and country population, color schemes and the data range to be displayed.

The latter is especially important, because there is this GitHub user from [Pitcairn](http://en.wikipedia.org/wiki/Pitcairn_Islands), who is responsible for a huge gap from the highest commit ratio to the runner-ups. By adjusting the color range maximum you can highlight the different country ratios.

The map uses the HTML5 input range element and works best with Google Chrome.

## Credits

This visualization was created by [Ramiro Gómez](http://www.ramiro.org/) as part of the [GitHub Data Challenge](https://github.com/blog/1118-the-github-data-challenge) using [Google Chart Tools](https://developers.google.com/chart/), the [jQuery JavaScript library](http://jquery.com/) and [Twitter Bootstrap](http://twitter.github.com/bootstrap/). The color schemes are taken from [Colorbrewer](http://colorbrewer2.org/).

Last but not least hundreds of thousands of developers, who host their open source projects on [GitHub](https://github.com/), provided the foundation for this map project, thank you!
