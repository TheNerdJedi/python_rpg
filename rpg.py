import math
import random

class Character:
	"""Create Character Class"""
	name = ""
	def __init__(self):
		pass

	def basic_attack(self, defender):
		#calculate damage
		damage = self.atk - defender.dfs
		# calculate hit chance
		spd_diff = self.spd - defender.spd
		hit_chance = 75
		hit_chance = hit_chance + spd_diff
		hit_prob = random.randrange(self.luck, hit_chance)
		# on hit fail
		if hit_prob < 15:
			print("{}'s attack missed!".format(self.name))
			return
		# on hit success
		else:
			# output no damage
			if damage <= 0:
				print("The attack has no effect.")
				damage = 0
			else:
				# calculate crit chance and damage
				crit = random.randrange(self.luck, 100, 5)
				if(crit > 85):
					damage = int(damage * 1.5)
					print("Critical Hit!")
				# calculate defender hp
				defender.hp = defender.hp - damage
				print("{} did {} damage!".format(self.name, damage))

	def magic_attack(self, defender):
		damage = self.magic_atk - defender.dfs
		crit = random.randrange(self.luck, 100, 5)
		if damage <= 0:
			print("The attack has no effect.")
			damage = 0
		else:
			if(crit > 85):
				damage = damage * 1.5
				print("Critical Hit!")
			defender.hp = defender.hp - damage
			print("{} did {} damage!".format(self.name, damage))

	def defend(self):
		pass


class Player(Character):
	"""Create Player Class"""
	# initialize player at level 1 with 0 experience
	exp = 0
	lvl = 1
	def __init__(self):
		pass

	#define stats from base stats of subclass
	def stats_init(self):
		self.hp = self.stats['BASE_HP']
		self.mp = self.stats['BASE_MP']
		self.atk = self.stats['BASE_ATK']
		self.dfs = self.stats['BASE_DFS']
		self.magic_atk = self.stats['BASE_MAGIC_ATK']
		self.spd = self.stats['BASE_SPD']
		self.luck = self.stats['BASE_LUCK']

	# loop through base stats dict and add level up modifiers
	def level_up(self):
		print()
		print("*--- {} LEVELED UP! ---*".format(self.name))
		for stat, value in self.stats.items():
			print("{}: {} + {} -->".format(stat, value, self.modifiers[stat]), end="")
			self.stats[stat] = value + self.modifiers[stat]
			print(self.stats[stat])
		self.lvl += 1
		print("*----------------------------------*")
		print()
		self.stats_init()

	# check level requirements and call level up on self if met
	def check_level_up(self):
		self.levels = [100, 250, 500, 1200]
		for value in self.levels:
			if self.exp >= value:
				self.level_up()
				self.levels.remove(value)
				break

	# take in enemies defeated from battle and add exp to total player controlled character
	def calculate_experience(self, enemies):
		exp_gain = 0
		for enemy in enemies:
			self.exp = self.exp + enemy.exp
			exp_gain = exp_gain + enemy.exp
		print("{} gained {} exp!".format(self.name, exp_gain))
		print("{}'s total exp: {}".format(self.name, self.exp))

	def check_inventory(self):
		if len(self.inventory) > 0:
			for idx, item in enumerate(self.inventory):
				print("{}. {}".format(idx, item.name))

			valid_item = False
			while not valid_item:
				item = input("Pick an item: ")
				try:
					item = int(item)
					valid_item = 0 <= item <= idx
				except ValueError:
					pass
				if not valid_item:
					print("Invalid Target")
			else:
				self.inventory[item].use_potion(self)
		else:
			raise Exception("You have no items")


	# create different class types
class Fighter(Player):
	"""Defines Fighter Class"""
	def __init__(self, name):
		self.name = name
		self.class_type = "Fighter"
		self.weapon = "sword"
		self.inventory = []
		self.stats = {'BASE_HP': 12, 'BASE_MP': 2, 'BASE_ATK': 10, 'BASE_DFS': 5, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 4, 'BASE_LUCK': 6}
		self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1, 'BASE_LUCK': 1}
		self.stats_init()

class Mage(Player):
	"""Defines Mage Class"""
	def __init__(self, name):
		self.name = name
		self.class_type = "Mage"
		self.weapon = "wand"
		self.inventory = []
		self.stats = {'BASE_HP': 10, 'BASE_MP': 8, 'BASE_ATK': 5, 'BASE_DFS': 4, 'BASE_MAGIC_ATK': 12, 'BASE_SPD': 7, 'BASE_LUCK': 5}
		self.modifiers = {'BASE_HP': 2, 'BASE_MP': 4, 'BASE_ATK': 1, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 3, 'BASE_SPD': 2, 'BASE_LUCK': 1}
		self.stats_init()
		
class Rogue(Player):
	"""Defines Rogue Class"""
	def __init__(self, name):
		self.name = name
		self.class_type = "Rogue"
		self.weapon = "dagger"
		self.inventory = []
		self.stats = {'BASE_HP': 10, 'BASE_MP': 4, 'BASE_ATK': 7, 'BASE_DFS': 4, 'BASE_MAGIC_ATK': 7, 'BASE_SPD': 10, 'BASE_LUCK': 10}
		self.modifiers = {'BASE_HP': 2, 'BASE_MP': 2, 'BASE_ATK': 2, 'BASE_DFS': 1, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 3, 'BASE_LUCK': 3}
		self.stats_init()

class Enemy(Character):
	"""Create Enemy"""
	def __init__(self):
		pass
class Slime(Enemy):
	"""Create Beast Enemy"""
	def __init__(self):
		self.name = "Slime"
		self.hp = 10
		self.mp = 0
		self.atk = 7
		self.dfs = 4
		self.spd = 4
		self.luck = 1
		self.exp = 10

class Item():
	"""Define item class"""
	name = ""
	def __init__(self):
		pass

class Weapon(Item):
	"""Define Weapon Item"""
	def __init__(self):
		self.type = "Weapon"

class Potion(Item):
	def __init__(self):
		self.name = "Healing potion"
		self.type = "Aid"
		self.short_desc = "Heals 5 HP"
		self.hp = 5

	def use_potion(self, user):
		print("{} used a potion!".format(user.name))
		if user.hp + self.hp < user.stats['BASE_HP']:
			user.hp = user.hp + self.hp
		else:
			user.hp = user.stats['BASE_HP']

def character_create():
	name = input("Hello brave adventurer, what is your name? : ")
	print()
	print("1. Fighter\n2. Mage\n3. Rogue")
	print()

	chosen = False
	while not chosen:
		class_choice = input("Please choose a class: ")
		print()
		if class_choice == "1":
			return Fighter(name)
			chosen = True
		elif class_choice == "2":
			return Mage(name)
			chosen = True
		elif class_choice == "3":
			return Rogue(name)
			chosen = True
		else:
			print("Invalid input. Please pick 1, 2, 3")
			continue

def turn_order(combatants):
	speed_order = sorted(combatants, key=lambda character: character.spd, reverse=True)

	return speed_order

def check_health(party):

	for person in party:
		if(person.hp > 0):
			return True

	return False

def pick_target(enemies):

	print("Which enemy do you target?")
	print()

	for idx, enemy in enumerate(enemies):
		print("{}. {} HP: {}".format(idx, enemy.name, enemy.hp))

	valid_target = False

	while not valid_target:
		target = input("Pick Target: ")
		try:
			target = int(target)
			valid_target = 0 <= target <= idx
		except ValueError:
			pass
		if not valid_target:
			print("Invalid Target")
	else:
		return target

	def main():

	player = character_create()
	potion = Potion()
	player.inventory.append(potion)
	friend = Mage("Dude")

	print("You are {}, the {}".format(player.name, player.class_type))
	print()
	print("As you travel throught the forest you encounter a fork in the road.\nWhich way do you go?")
	print("1. Left\n2. Right")
	print()
	direction = input("Pick a path: ")
	print()
	if direction == "1":
		back = False
		while not back:
			slime = Slime()
			slime2 = Slime()

			print("Enemies Appear!")
			battle([player, friend, slime, slime2], [player, friend], [slime, slime2])
			if player.hp > 0:
				print("Behind the beast was a dead end. Do you want to turn back?")
				print("1. Yes\n2. No")
				print()
				go_back = input("Go back? : ")
				if go_back == "1":
					print("As you head back you see another adventurer walking away from the other path with boundless treasure, too bad you didn't go that way.")
					back = True
				elif go_back == "2":
					continue
			else:
				break
	elif direction == "2":
		print("You discover boundless treasure and will never have to work another day of you life!")

	print("Game over.")

if __name__ == '__main__':
	main()