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