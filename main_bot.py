
import hlt
import logging
import utils
game = hlt.Game("Destructor")
logging.info("Starting DESTRUCTOR")

while True:
	game_map = game.update_map()
	command_queue = []
	for ship in game_map.get_me().all_ships():
		if ship.docking_status == ship.DockingStatus.UNDOCKED:
			if not utils.isMapFullyOwned(game_map):
				target = utils.find_closest_planet(ship,game_map)
				if target != None:
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
					target = utils.find_closest_ship(ship,game_map)
					nav_command = ship.navigate(
							ship.closest_point_to(target),
							game_map,
							speed=int(hlt.constants.MAX_SPEED),
							avoid_obstacles=True)
					if nav_command:
						command_queue.append(nav_command)

	game.send_command_queue(command_queue)



