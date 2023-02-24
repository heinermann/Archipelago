# More appropriate for DLC. We shouldn't need to worry about this very much.
from BaseClasses import Region, MultiWorld


# Creates all regions and connections. Called from NoitaWorld.
def create_all_regions_and_connections(world: MultiWorld, player: int) -> None:
    menu = Region("Menu", player, world)
    
    new_game = Entrance(player, "New Game", menu)
    menu.exits.append(new_game)

    asteroid = Region("Asteroid", player, world)
    new_game.connect(asteroid)

    world.regions += [menu, asteroid]
