# Attack another's active pokemon with a potion
def attacked(pokemon, potion):
  if pokemon.is_knocked_out == False:
    	pokemon.current_health - 50
    	print(f"{pokemon}'s current health is {pokemon.current_health}.")


# Fight function to calculate damage and reduce HP
def battle(attacker, defender):
  a = attacker
  d = defender
  if attacker.is_knocked_out == False:
    if (a._type == "Fire" and d._type == "Grass") or (a._type == "Grass" and d._type == "Water") or (a._type == "Water" and d._type == "Fire"):
      if a.level <= d.level:
            new_hp = d.current_health - 15
      elif a.level > d.level:
            new_hp = d.current_health - 20
      elif a.level > d.level * 2:
            new_hp = d.current_health - 40
    else:
    	if a.level <= d.level:
    	    new_hp = d.current_health - 5
    	elif a.level > d.level:
          new_hp = d.current_health - 10
      #elif a.level > d.level * 2:
          #new_hp = d.current_health - 15 
      
    return new_hp
    
# Function to regain HP based on potions(not real items, per the game) picked
def regain(pokemon, potion):
  if potion == "Berries":
    pokemon.current_health += 20
  elif potion == "Herb":
    pokemon.current_health += 30
  elif potion == "Orb":
    pokemon.current_health += 40
  if pokemon.current_health > pokemon.max_health:
    pokemon.current_health = pokemon.max_health
  pokemon.revive_poke()


# Trainers
class Trainer:
  def __init__(self, name, pokemons, potions, active_pokemon_index):
    self.name = name
    self.pokemons = pokemons
    self.potions = potions
    self.active_pokemon_index = active_pokemon_index
		
  def revive_pokemon(self, potion_index):
    active_pokemon = self.pokemons[self.active_pokemon_index]
    potion = self.potions[potion_index]
    regain(active_pokemon, potion)
    active_pokemon.regain_health()
		
  def attacking(self, other, active_pokemon, potion):
    attacked(other.pokemons[active_pokemon], self.potions.pop(potion))
		
  def swap(self, active_pokemon_index, swap_index):
    temp = self.pokemons[active_pokemon_index]
    if temp.is_knocked_out == False:
      self.pokemons[active_pokemon_index] = self.pokemons[swap_index]
      self.pokemons[swap_index] = temp
      print(f"{self.pokemon[active_pokemon_index]} is now active.")
		




# Pokemoms games
class Pokemon(Trainer):
    # Initializing The character
    def __init__(self, name, _type, level, max_health, current_health, is_knocked_out):
        self.name = name
        self._type = _type
        self.level = level
        self.max_health = max_health
        self.current_health = current_health
        self.is_knocked_out = is_knocked_out
    
    # Pokemon loses hp in a battle
    def lose_health(self, other):
    	other.current_health = battle(self, other)
    	print(f"{other.name}'s current HP is {other.current_health}.")
    	other.knock_out()
    	
    # Pokemon gains health from finding potions
    def regain_health(self):
    	print(f"{self.name}'s current HP is {self.current_health}.")
    
    # Knock out a Pokemon whose HP is now 0
    def knock_out(self):
    	if self.current_health <= 0:
    		self.is_knocked_out = True
    		print(f"{self.name} has been eliminated.")
    	
    # Revives pokemon
    def revive_poke(self):
    	self.is_knocked_out = False
    	print(f"{self.name} is back.")


A = Pokemon("Aa", "Fire", 4, 100, 100, False)
B = Pokemon("Bb", "Gress", 5, 100, 100, False)
C = Pokemon("Cc", "Water", 5, 100, 100, False)

okah = Trainer("Okah", [A, B, C], ["Berries", "Herb", "Orb"], 0)

X = Pokemon("Xx", "Fire", 10, 100, 100, False)
Y = Pokemon("Yy", "Gress", 3, 100, 100, False)
Z = Pokemon("Zz", "Water", 20, 100, 100, False)

john = Trainer("John", [X, Y, Z], ["Berries", "Herb", "Orb"], 0)

A.lose_health(X)

X.lose_health(A)
X.lose_health(A)

okah.revive_pokemon(2)
#print(okah.active_pokemon_index)
print(okah.potions)
