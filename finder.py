
import hlt
import logging

def find_closest_planet(ship,game_map,is_owned=False, isFriendly=False):
	# par défaut, renvoie la planete non occupee la plus proche, sinon renvoie la planete la plus proche en fonction de son proprietaire
	me = game_map.get_me()
	entities_by_distance = game_map.nearby_entities_by_distance(ship)
	nearest_planet = None
	for distance in sorted(entities_by_distance):
                nearest_planet = next((nearest_entity for nearest_entity in entities_by_distance[distance] if (isinstance(nearest_entity, hlt.entity.Planet) and (nearest_entity.is_owned == is_owned) and ((nearest_entity.owner==me)==isFriendly))),None)
    if (nearest_planet==None):
    	logging.info("Planete non trouvee")
   	else:
   		logging.info("Planete trouvee")
    return nearest_planet

def find_closest_ship(ship,game_map,isFriendly=False):
	# retourne le vaisseau allie ou ennemi le plus proche de ship
	me = game_map.get_me()
	entities_by_distance = game_map.nearby_entities_by_distance(ship)
	nearest_ship = None
	for distance in sorted(entities_by_distance):
                nearest_ship = next((nearest_entity for nearest_entity in entities_by_distance[distance] if (isinstance(nearest_entity, hlt.entity.Ship) and ((nearest_entity.owner==me)==isFriendly))),None)
    if (nearest_ship==None):
    	logging.info("Vaisseau non trouve")
    else:
    	logging.info("Vaisseau trouve")
    return nearest_ship	