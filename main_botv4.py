
import hlt
import logging
import utils
game = hlt.Game("Destructorv4")
logging.info("Starting DESTRUCTOR")
map_isfull = False
while True:

	game_map = game.update_map()
	command_queue = []
	planet_target_list = []



	for ship in game_map.get_me().all_ships():
		if ship.docking_status == ship.DockingStatus.UNDOCKED:
					
			if not utils.isMapFullyOwned(game_map):
				target = utils.find_closest_planet(ship,game_map, target_list=planet_target_list)
				if target != None:
					if not map_isfull:
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

			elif len(utils.detectEnemies(game_map,ship,100))==0 and not utils.find_closest_planet(ship,game_map,isOwned=True,isFriendly=True).is_full():
				map_isfull = True
				target = utils.find_closest_planet(ship,game_map,isOwned=True,isFriendly=True)
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
			else:
				map_isfull = True
				target = utils.find_closest_ship(ship,game_map)
				nav_command = ship.navigate(
						ship.closest_point_to(target),
						game_map,
						speed=int(hlt.constants.MAX_SPEED),
						avoid_obstacles=True)
				if nav_command:
					command_queue.append(nav_command)

	game.send_command_queue(command_queue)




