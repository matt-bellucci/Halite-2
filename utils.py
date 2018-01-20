import hlt
import logging

def find_closest_planet(ship,game_map,isOwned=False, isFriendly=False):
	# par défaut, renvoie la planete non occupee la plus proche, sinon renvoie la planete la plus proche en fonction de son proprietaire
	me = game_map.get_me()
	entities_by_distance = game_map.nearby_entities_by_distance(ship)
	nearest_planet = None
	for distance in sorted(entities_by_distance):
		nearest_planet = next((nearest_entity for nearest_entity in entities_by_distance[distance] if (isinstance(nearest_entity, hlt.entity.Planet) and (nearest_entity.is_owned() == isOwned) and ((nearest_entity.owner==me)==isFriendly))),None)
		if nearest_planet:
			break
	if nearest_planet==None:
		logging.info("Planete non trouvee")

	else:
		logging.info("Planete trouvee")
		logging.info(nearest_planet.id)
	return nearest_planet

def detectEnemies(map, planet, radius):
	result = []
	for player in map.all_players():
		if player.id != map.get_me().id:
			for ship in player.all_ships():
				if planet.calculate_distance_between(ship) < radius:
					result.append(ship)
	return result

def find_closest_ship(ship,game_map, isFriendly=False):
	# par défaut, renvoie la planete non occupee la plus proche, sinon renvoie la planete la plus proche en fonction de son proprietaire
	me = game_map.get_me()
	entities_by_distance = game_map.nearby_entities_by_distance(ship)
	nearest_ship = None
	for distance in sorted(entities_by_distance):
		nearest_ship = next((nearest_entity for nearest_entity in entities_by_distance[distance] if (isinstance(nearest_entity, hlt.entity.Ship) and ((nearest_entity.owner==me)==isFriendly))),None)
		if nearest_ship:
			break
	if nearest_ship==None:
		logging.info("Planete non trouvee")

	else:
		logging.info("Planete trouvee")
		logging.info(nearest_ship.id)
	return nearest_ship

def isMapFullyOwned(map):
	result = True;
	for planet in map.all_planets():
		if not planet.is_owned():
			result = False
			break
	return result

def find_largest_planet(game_map,isOwned=True,isFriendly=True):
	me = game_map.get_me()
	planet_list = game_map.all_planets()
	planet=None
	k = 1
	sorted_planet_list = sorted(planet_list, key = lambda x : x.radius, reverse=True)
	for planet in sorted_planet_list:
		if (planet.is_owned()==isOwned and (planet.owner==me)==isFriendly):
			result = planet
			break
	return result



