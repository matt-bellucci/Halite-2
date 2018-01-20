
import hlt
import logging

game = hlt.Game("Bot_Matt")
logging.info("Pret a enculer Coco")

#Game start
while True:

    game_map = game.update_map()
    me = game_map.get_me()
    enemies = game_map.all_players()
    command_queue = []
    planet_targetted = []
    #pour chaque ship que je controle
    for ship in game_map.get_me().all_ships():
        logging.info(ship)
        if ship.docking_status != ship.DockingStatus.UNDOCKED:
            continue
        else:




        #RECHERCHE PLANETES
            entities_by_distance = game_map.nearby_entities_by_distance(ship)
            nearest_planet = None
            for distance in sorted(entities_by_distance):
                nearest_planet = next((nearest_entity for nearest_entity in entities_by_distance[distance] if (isinstance(nearest_entity, hlt.entity.Planet) and not nearest_entity.is_owned() and (not nearest_entity in planet_targetted))), None)
                if nearest_planet:
                    logging.info("Planete trouvee")
                    planet_targetted.append(nearest_planet)
                    break

        # FIN RECHERCHE    
            if nearest_planet != None:
            # NAVIGATION ou DOCKING VERS PLANETE
                if ship.can_dock(nearest_planet):
                    command_queue.append(ship.dock(nearest_planet))
                    


                else:
                    nav_command = ship.navigate(
                        ship.closest_point_to(nearest_planet),
                        game_map,
                        speed=int(hlt.constants.MAX_SPEED),
                        avoid_obstacles=True)
                    if nav_command:
                        command_queue.append(nav_command)
                continue
            else:
                logging.info("Ordre attaque")
                entities_by_distance = game_map.nearby_entities_by_distance(ship)
                nearest_enemy = None
                for distance in sorted(entities_by_distance):
                    nearest_enemy = next((nearest_entity for nearest_entity in entities_by_distance[distance] if (isinstance(nearest_entity, hlt.entity.Ship))), None)
                    if nearest_enemy:
                        logging.info("Ennemi trouve")
                        break
                if nearest_enemy != None:    
                    attack_command = ship.navigate(
                    ship.closest_point_to(nearest_enemy),
                    game_map,
                    speed=int(hlt.constants.MAX_SPEED),
                    avoid_obstacles=True)
                    if attack_command:
                        command_queue.append(attack_command)
                else:
                    logging.info("Pas de target")
                    default_command=ship.navigate(
                        entities_by_distance[0],
                        game_map,
                        speed=0)
                    command_queue.append(default_command)
                continue 
                    








        #logging.info(nearest_planet)
    logging.info("Sending commands")
    game.send_command_queue(command_queue)  





