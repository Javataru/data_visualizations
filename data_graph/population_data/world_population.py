import json
import pygal
from pygal.style import RotateStyle
from country_codes import get_country_code

"""load population data into a list"""

filename = 'population_json.json'

with open(filename) as f:
    pop_data = json.load(f)

"""build a dictionary of population data"""
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

"""group countries into 3 population levels."""
cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop

"""see how many countries are at each level"""
print(len(cc_pops1), len(cc_pops2), len(cc_pops3))


wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops1)
wm.add('10m-1bn', cc_pops2)
wm.add('>1bn', cc_pops3)


wm.render_to_file('world_population.svg')
