
from craigslist import CraigslistForSale

cl_e30 = CraigslistForSale(site='boston', category='cta',
        filters={'make': 'bmw', 'auto_transmission': ['manual'], 'min_year': 1987, 'max_year': 1991, 'search_distance': 1000})

for result in cl_e30.get_results(sort_by='newest'):
    print(result)
