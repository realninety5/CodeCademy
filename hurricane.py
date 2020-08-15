




# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

"""Returns damages(a list of string objects) as a list of float objects."""
def new_damages(list_obj):
  new_list = []
  for i in list_obj:
    if "D" in i:
      new_list.append(i)
      continue
    elif "M" in i:
      i = i[:-1]
      new_list.append(float(i) * 1000000)
    elif "B" in i:
      i = i[:-1]
      new_list.append(float(i) * 1000000000)
  return new_list





# write your construct hurricane dictionary function here:

#Return a dictionary of each related items in the list
def new_combo(name):
  hur_details = {}
  try:
    i = names.index(name)
  except ValueError as ve:
    print(ve+" not valid.")
  #print(i)
  hur_details.update({names[i]: {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Death': deaths[i], 'Damage': damages[i]}})
  return hur_details





# write your construct hurricane by year dictionary function here:
#Returns Hurricanes that happened in a particular year
def year_hur(year):
   listy = []
   for i in range(len(years)):
    if year == years[i]:
      in_year ={}
      in_year.update({'Name': names[i]})
      in_year.update({'Month': months[i]})
      in_year.update({'Year': years[i]})
      in_year.update({'Max Sustained Wind': max_sustained_winds[i]})
      in_year.update({'Areas Affected': areas_affected[i]})
      in_year.update({'Death': deaths[i]})
      in_year.update({'Damage': damages[i]})
      listy.append(in_year)
   return {year:listy}






# write your count affected areas function here:


def frequency():
  freq = {}
  list_area = []
  for i in areas_affected:
    for j in i:
      if j not in list_area:
        list_area.append(j)
  # check for freqiencies
  for i in list_area:
    count = 0
    for j in areas_affected:
      if i in j:
        count += 1
    freq.update({i: count})
  return freq




# write your find most affected area function here:


# Finds and area and return now many times it has been afrected
def find_area(area):
  temp = frequency()
  for k, v in temp.items():
    if area == k:
      return {k: v}
      break




# write your greatest number of deaths function here:

# Check for the greatest number of deaths
def worst_hur():
  temp = 0
  for i in range(len(deaths)):
    if temp < deaths[i]:
      temp = deaths[i]
      name = names[i]
  return {name: temp}





# write your catgeorize by mortality function here:

def death_scale():
  keys = [0, 1, 2, 3, 4, 5]
  zero = []; one = []; two = []; three = []; four = []; five = []
  for i in range(len(deaths)):
    if deaths[i] == 0:
      zero.append(names[i])
    elif deaths[i] <= 100 and deaths[i] > 0:
      one.append(names[i])
    elif deaths[i] <= 500 and deaths[i] > 100:
      two.append(names[i])
    elif deaths[i] <= 1000 and deaths[i] > 500:
      three.append(names[i])
    elif deaths[i] <= 10000 and deaths[i] > 1000:
      four.append(names[i])
    elif deaths[i] > 10000:
      five.append(names[i])
  listy = [i for i in [zero, one, two, three, four, five]]
  death_scl = dict(zip(keys, listy))
  return death_scl





# write your greatest damage function here:
def greatest_damage():
  temp = 0
  damage_list = new_damages(damages)
  # loop through the list to find the worst hit
  for i in range(len(damage_list)):
    if "D" in str(damage_list[i]):
      continue
    elif temp < damage_list[i]:
      temp = damage_list[i]
      name = names[i]
  return {name: temp}






# write your catgeorize by damage function here:
def damage_scale():
  keys = [0, 1, 2, 3, 4, 5]
  zero = []; one = []; two = []; three = []; four = []; five = []
  for i in range(len(deaths)):
    if deaths[i] == 0:
      zero.append(names[i])
    elif deaths[i] <= 100000000 and deaths[i] > 0:
      one.append(names[i])
    elif deaths[i] <= 1000000000 and deaths[i] > 100000000:
      two.append(names[i])
    elif deaths[i] <= 10000000000 and deaths[i] > 1000000000:
      three.append(names[i])
    elif deaths[i] <= 50000000000 and deaths[i] > 10000000000:
      four.append(names[i])
    elif deaths[i] > 50000000000:
      five.append(names[i])
  listy = [i for i in [zero, one, two, three, four, five]]
  death_scl = dict(zip(keys, listy))
  return death_scl




#print(frequency())

print(damage_scale())
