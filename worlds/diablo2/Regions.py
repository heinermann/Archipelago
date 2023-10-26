# Regions are areas in your game that you travel to.
from typing import Dict, Set

from BaseClasses import Entrance, MultiWorld, Region
from . import Events, Locations


def add_locations(world: "Diablo2World", region: Region) -> None:
    locations = Locations.location_region_mapping.get(region.name, {})
    for location_name, location_data in locations.items():
        location_type = location_data.ltype

        match location_type:
            case Locations.LocType.waypoint:
                if not world.options.waypoints_as_checks: continue
            case Locations.LocType.goldenchest:
                if not world.options.goldenchests_as_checks: continue
            case Locations.LocType.superunique:
                if not world.options.superuniques_as_checks: continue

        if not world.options.is_expansion and location_data.group == "Act 5":
            continue

        region.add_locations({location_name: location_data.id})


# Creates a new Region with the locations found in `location_region_mapping` and adds them to the world.
def create_region(world: "Diablo2World", region_name: str) -> Region:
    new_region = Region(region_name, world.player, world.multiworld)
    add_locations(world, new_region)
    return new_region


def get_connection_data(world: "Diablo2World") -> Dict[str, Set[str]]:
    if world.options.is_expansion:
        return d2_expansion_connections
    return d2_connections


def get_region_data(world: "Diablo2World") -> Set[str]:
    if world.options.is_expansion:
        return d2_expansion_regions
    return d2_regions


def create_regions(world: "Diablo2World") -> Dict[str, Region]:
    return {name: create_region(world, name) for name in get_region_data(world)}


# An "Entrance" is really just a connection between two regions
def create_entrance(player: int, source: str, destination: str, regions: Dict[str, Region]):
    entrance = Entrance(player, f"From {source} To {destination}", regions[source])
    entrance.connect(regions[destination])
    return entrance


# Creates connections based on our access mapping in `d2_connections`.
def create_connections(world: "Diablo2World", regions: Dict[str, Region]) -> None:
    for source, destinations in get_connection_data(world).items():
        new_entrances = [create_entrance(world.player, source, destination, regions) for destination in destinations]
        regions[source].exits = new_entrances


# Creates all regions and connections. Called from Diablo2World.
def create_all_regions_and_connections(world: "Diablo2World") -> None:
    created_regions = create_regions(world)
    create_connections(world, created_regions)
    Events.create_all_events(world, created_regions)

    world.multiworld.regions += created_regions.values()


d2_connections: Dict[str, Set[str]] = {
    # Act 1
    "Menu": {"Rogue Encampment"},
    "Rogue Encampment": {"Blood Moor", "Lut Gholein", "Secret Cow Level"},
    "Blood Moor": {"Cold Plains", "Den of Evil"},
    "Cold Plains": {"Burial Grounds", "Stony Field", "The Cave"},
    "Burial Grounds": {"The Mausoleum", "The Crypt"},
    "Stony Field": {"Underground Passage", "Tristram"},
    "Underground Passage": {"Dark Wood"},
    "Dark Wood": {"Black Marsh"},
    "Black Marsh": {"Tamoe Highland", "The Forgotten Tower", "The Hole"},
    "Tamoe Highland": {"The Pit", "Monestary Gate"},
    "Monestary Gate": {"Outer Cloister"},
    "Outer Cloister": {"Barracks"},
    "Barracks": {"Jail"},
    "Jail": {"Inner Cloister"},
    "Inner Cloister": {"Cathedral"},
    "Cathedral": {"Catacombs"},

    # Act 2
    "Lut Gholein": {"Lut Gholein Sewers", "Rocky Waste", "Harem", "Kurast Docks"},
    "Rocky Waste": {"The Stony Tomb", "Dry Hills"},
    "Dry Hills": {"Halls of the Dead", "Far Oasis"},
    "Far Oasis": {"Maggot Lair", "Lost City"},
    "Lost City": {"The Ancient Tunnels", "The Valley of Snakes"},
    "The Valley of Snakes": {"Claw Viper Temple"},
    "Harem": {"Palace Cellar"},
    "Palace Cellar": {"Arcane Sanctuary"},
    "Arcane Sanctuary": {"Canyon of the Magi"},
    "Canyon of the Magi": {"Tal Rasha's Tomb"},
    "Tal Rasha's Tomb": {"Tal Rasha's Chamber"},

    # Act 3
    "Kurast Docks": {"Spider Forest"},
    "Spider Forest": {"Spider Cavern", "Arachnid Lair", "Great Marsh", "Flayer Jungle"},
    "Great Marsh": {"Flayer Jungle"},
    "Flayer Jungle": {"Great Marsh", "Flayer Dungeon", "Swampy Pit", "Lower Kurast"},
    "Lower Kurast": {"Kurast Bazaar"},
    "Kurast Bazaar": {"Ruined Temple", "Disused Fane", "Kurast Sewers", "Upper Kurast"},
    "Upper Kurast": {"Kurast Sewers", "Forgotten Temple", "Forgotten Reliquary", "Kurast Causeway"},
    "Kurast Causeway": {"Disused Reliquary", "Ruined Fane", "Travincal"},
    "Travincal": {"Durance of Hate"},
    "Durance of Hate": {"Pandemonium Fortress"},

    # Act 4
    "Pandemonium Fortress": {"Harrogath", "Outer Steppes"},
    "Outer Steppes": {"Plains of Despair"},
    "Plains of Despair": {"City of the Damned"},
    "City of the Damned": {"River of Flame"},
    "River of Flame": {"Chaos Sanctuary"},
}

d2_expansion_connections: Dict[str, Set[str]] = {**d2_connections,
    # Act 4
    "Pandemonium Fortress": {"Harrogath", "Outer Steppes"},

    # Act 5
    "Harrogath": {"Bloody Foothills", "Nihlathak's Temple"},
    "Nihlathak's Temple": {"Halls of Anguish"},
    "Halls of Anguish": {"Halls of Pain"},
    "Halls of Pain": {"Halls of Vaught"},
    "Bloody Foothills": {"Frigid Highlands"},
    "Frigid Highlands": {"Abaddon", "Arreat Plateau"},
    "Arreat Plateau": {"Pit of Acheron", "Crystalline Passage"},
    "Crystalline Passage": {"Frozen River", "Glacial Trail"},
    "Glacial Trail": {"Drifter Cavern", "Frozen Tundra"},
    "Frozen Tundra": {"Infernal Pit", "The Ancients' Way"},
    "The Ancients' Way": {"Icy Cellar", "Arreat Summit"},
    "Arreat Summit": {"Worldstone Keep"},
    "Worldstone Keep": {"Throne of Destruction"},
    "Throne of Destruction": {"Worldstone Chamber"},
}

d2_regions: Set[str] = set(d2_connections.keys()).union(*d2_connections.values())
d2_expansion_regions: Set[str] = set(d2_expansion_connections.keys()).union(*d2_expansion_connections.values())
