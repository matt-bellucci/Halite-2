
import hlt
import logging
import utils
game = hlt.Game("Destructorv4")
logging.info("Starting DESTRUCTOR")
while True:

	game_map = game.update_map()
	command_queue = []
	planet_target_list = []
	for ship in game_map.get_me().all_ships():
		if ship.docking_status == ship.DockingStatus.UNDOCKED:
			planet = utils.find_closest_planet(ship, game_map,isOwned=True,isFriendly=True)
					
			if not utils.isMapFullyOwned(game_map):
				target = utils.find_closest_planet(ship,game_map, target_list=planet_target_list)
				if target != None:
					planet_target_list.append(target)
			       # NAVIGATION ou DOCKING VERS PLANETE
					if ship.can_dock(target):
						command_queue.append(ship.dock(target))
					else:
						nav_command = ship.navigate(
							ship.closest_point_to(target),
							game_map,
							speed=int(hlt.constants.MAX_SPEED),
							avoid_obstacles=True)
						if nav_command:
							command_queue.append(nav_command)
					continue
				else:
					target = utils.find_closest_planet(ship,game_map)
					if ship.can_dock(target):
						command_queue.append(ship.dock(target))
					else:
						nav_command = ship.navigate(
							ship.closest_point_to(target),
							game_map,
							speed=int(hlt.constants.MAX_SPEED),
							avoid_obstacles=True)
						if nav_command:
							command_queue.append(nav_command)
				continue			
			else:
				planet = utils.find_largest_planet(game_map)
				enemy = utils.detectEnemies(game_map,planet,5)
				if enemy != []:
					target = enemy[0]
					nav_command = ship.navigate(
							ship.closest_point_to(target),
							game_map,
							speed=int(hlt.constants.MAX_SPEED),
							avoid_obstacles=True)
					if nav_command:
						command_queue.append(nav_command)

				else:
					target = utils.findDefenselessPlanet(game_map)[0]
					logging.info("Planete a attaquer")
					logging.info(planet.id)
					enemy = utils.detectEnemies(game_map,target,3)
					nav_command = ship.navigate(
							ship.closest_point_to(enemy[0]),
							game_map,
							speed=int(hlt.constants.MAX_SPEED),
							avoid_obstacles=True)
					if nav_command:
						command_queue.append(nav_command)

	game.send_command_queue(command_queue)



