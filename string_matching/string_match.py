# -*- coding: utf-8 -*-
"""
ENGY644 Spring 2020
"""

from __future__ import print_function
from fuzzywuzzy import process
import pandas as pd

# https://github.com/seatgeek/fuzzywuzzy
# https://en.wikipedia.org/wiki/Levenshtein_distance

population = pd.read_csv('2015_population_by_county.csv')
wind_capacity = pd.read_csv('2015_wind_by_county.csv')

counties_wind = list(wind_capacity['county & state'].values)
counties_pop = list(population['county & state'].values)

pop = list(population['2015 Total Population (Esri)'].values)
cap = list(wind_capacity['2015 Capacity Onshore Wind (GW)'].values)

############################################################################
##
## QUESTION: HOW MANY PEOPLE IN 2015 LIVED IN A COUNTY WITH A WIND TURBINE?
## Fill in the three lines with ???
##
###########################################################################

# start a running total of the population that lived near a wind turbine
population_near_wind = 0
for county in counties_wind:
    ## figure out which county from the population list matches the county in question
    ## hint: check out process.extractOne(string, choices) in the fuzzywuzzy documentation: https://github.com/seatgeek/fuzzywuzzy
    matching_county = process.extractOne(county, counties_pop)
    ## print the match as we go along
    print('{} matched with {}'.format(county, matching_county))
    ## figure out the index of the county that we matched to. Hint: look up the index function (google "python index of value in list")
    index_of_matched_county = counties_pop.index(matching_county[0])
    population_of_matched_county = pop[index_of_matched_county]
    ## add the population from our matching county to our running total
    population_near_wind += population_of_matched_county


total_population = sum(pop)
print('The total population in 2015 that lived in a county with a wind turbine was {}. \
This was {}% of the total population'.format(population_near_wind, round(population_near_wind/float(total_population)*100,1)))

# Answer: The total population in 2015 that lived in a county with a wind turbine was 37573486. This was 11.8% of the total population
