# Regions are areas in your game that you travel to.
from typing import Dict, Set

from BaseClasses import Entrance, MultiWorld, Region
from . import Locations


def add_location(player: int, loc_name: str, id: int, region: Region) -> None:
    location = Locations.NoitaLocation(player, loc_name, id, region)
    region.locations.append(location)


def add_locations(multiworld: MultiWorld, player: int, region: Region) -> None:
    locations = Locations.location_region_mapping.get(region.name, {})
    for location_name, location_data in locations.items():
        location_type = location_data.ltype
        flag = location_data.flag

        opt_orbs = multiworld.orbs_as_checks[player].value
        opt_bosses = multiworld.bosses_as_checks[player].value
        opt_paths = multiworld.path_option[player].value
        opt_num_chests = multiworld.hidden_chests[player].value
        opt_num_pedestals = multiworld.pedestal_checks[player].value

        is_orb_allowed = location_type == "orb" and flag <= opt_orbs
        is_boss_allowed = location_type == "boss" and flag <= opt_bosses
        if flag == Locations.LocationFlag.none or is_orb_allowed or is_boss_allowed:
            add_location(player, location_name, location_data.id, region)
        elif location_type == "chest" and flag <= opt_paths:
            for i in range(opt_num_chests):
                add_location(player, f"{location_name} {i+1}", location_data.id + i, region)
        elif location_type == "pedestal" and flag <= opt_paths:
            for i in range(opt_num_pedestals):
                add_location(player, f"{location_name} {i+1}", location_data.id + i, region)


# Creates a new Region with the locations found in `location_region_mapping` and adds them to the world.
def create_region(multiworld: MultiWorld, player: int, region_name: str) -> Region:
    new_region = Region(region_name, player, multiworld)
    add_locations(multiworld, player, new_region)
    return new_region


def create_regions(multiworld: MultiWorld, player: int) -> Dict[str, Region]:
    return {name: create_region(multiworld, player, name) for name in noita_regions}


# An "Entrance" is really just a connection between two regions
def create_entrance(player: int, source: str, destination: str, regions: Dict[str, Region]):
    entrance = Entrance(player, f"From {source} To {destination}", regions[source])
    entrance.connect(regions[destination])
    return entrance


# Creates connections based on our access mapping in `noita_connections`.
def create_connections(player: int, regions: Dict[str, Region]) -> None:
    for source, destinations in noita_connections.items():
        new_entrances = [create_entrance(player, source, destination, regions) for destination in destinations]
        regions[source].exits = new_entrances


# Creates all regions and connections. Called from NoitaWorld.
def create_all_regions_and_connections(multiworld: MultiWorld, player: int) -> None:
    created_regions = create_regions(multiworld, player)
    create_connections(player, created_regions)

    multiworld.regions += created_regions.values()


# Oh, what a tangled web we weave
# Notes to create artificial spheres:
# - Shaft is excluded to disconnect Mines from the Snowy Depths
# - Lukki Lair is disconnected from The Vault
# - Overgrown Cavern is connected to the Underground Jungle instead of the Desert due to similar difficulty
# - Powerplant is disconnected from the Sandcave due to difficulty and sphere creation
# - Snow Chasm is disconnected from the Snowy Wasteland
# - Pyramid is connected to the Hiisi Base instead of the Desert due to similar difficulty
# - Frozen Vault is connected to the Vault instead of the Snowy Wasteland due to similar difficulty
# - Lake is connected to The Laboratory, since the boss is hard without specific set-ups (which means late game)
# - Snowy Depths connects to Lava Lake orb since you need digging for it, so fairly early is acceptable
# - Ancient Laboratory is connected to the Coal Pits, so that Ylialkemisti isn't sphere 1
noita_connections: Dict[str, Set[str]] = {
    # Act 1
    "Menu": {"Rogue Encampment"},
    "Rogue Encampment": {"Blood Moor", "Lut Gholein", "Secret Cow Level"},
        "Secret Cow Level": {"Rogue Encampment"},
    "Blood Moor": {"Rogue Encampment", "Cold Plains", "Den of Evil"},
        "Den of Evil": {"Blood Moor"},
    "Cold Plains": {"Blood Moor", "Burial Grounds", "Stony Field", "The Cave"},
        "The Cave": {"Cold Plains"},
    "Burial Grounds": {"Cold Plains", "The Mausoleum", "The Crypt"},
        "The Mausoleum": {"Burial Grounds"},
        "The Crypt": {"Burial Grounds"},
    "Stony Field": {"Cold Plains", "Underground Passage"},
    "Underground Passage": {"Stony Field", "Dark Wood"},
    "Dark Wood": {"Underground Passage", "Black Marsh"},
    "Black Marsh": {"Dark Wood", "Tamoe Highland", "The Forgotten Tower", "The Hole"},
        "The Hole": {"Black Marsh"},
        "The Forgotten Tower": {"Black Marsh"},
    "Tamoe Highland": {"Black Marsh", "The Pit", "Monestary Gate"},
        "The Pit": {"Tamoe Highland"},
    "Monestary Gate": {"Tamoe Highland", "Outer Cloister"},
    "Outer Cloister": {"Monestary Gate", "Barracks"},
    "Barracks": {"Outer Cloister", "Jail"},
    "Jail": {"Barracks", "Inner Cloister"},
    "Inner Cloister": {"Jail", "Cathedral"},
    "Cathedral": {"Inner Cloister", "Catacombs"},
    "Catacombs": {"Cathedral"},

    # Act 2
    "Lut Gholein": {"Lut Gholein Sewers", "Rocky Waste", "Harem", "Rogue Encampment", "Kurast Docks"},
    "Lut Gholein Sewers": {"Lut Gholein"},
    "Rocky Waste": {"Lut Gholein", "The Stony Tomb", "Dry Hills"},
        "The Stony Tomb": {"Rocky Waste"},
    "Dry Hills": {"Rocky Waste", "Halls of the Dead", "Far Oasis"},
        "Halls of the Dead": {"Dry Hills"},
    "Far Oasis": {"Dry Hills", "Maggot Lair", "Lost City"},
        "Maggot Lair": {"Far Oasis"},
    "Lost City": {"Far Oasis", "The Ancient Tunnels", "The Valley of Snakes"},
        "The Ancient Tunnels": {"Lost City"},
    "The Valley of Snakes": {"Lost City", "Claw Viper Temple"},
        "Claw Viper Temple": {"The Valley of Snakes"},
    "Harem": {"Lut Gholein", "Palace Cellar"},
    "Palace Cellar": {"Harem", "Arcane Sanctuary"},
    "Arcane Sanctuary": {"Palace Cellar", "Canyon of the Magi"},
    "Canyon of the Magi": {"Tal Rasha's Tomb"},
    "Tal Rasha's Tomb": {"Canyon of the Magi", "Tal Rasha's Chamber"},
    "Tal Rasha's Chamber": {"Lut Gholein"},

    # Act 3
    "Kurast Docks": {"Lut Gholein", "Spider Forest"},
    "Spider Forest": {"Kurast Docks", "Spider Cavern", "Arachnid Lair", "Great Marsh", "Flayer Jungle"},
        "Spider Cavern": {"Spider Forest"},
        "Arachnid Lair": {"Spider Forest"},
    "Great Marsh": {"Spider Forest", "Flayer Jungle"},
    "Flayer Jungle": {"Spider Forest", "Great Marsh", "Flayer Dungeon", "Swampy Pit", "Lower Kurast"},
        "Flayer Dungeon": {"Flayer Jungle"},
        "Swampy Pit": {"Flayer Jungle"},
    "Lower Kurast": {"Flayer Jungle", "Kurast Bazaar"},
    "Kurast Bazaar": {"Lower Kurast", "Ruined Temple", "Disused Fane", "Kurast Sewers", "Upper Kurast"},
        "Ruined Temple": {"Kurast Bazaar"},
        "Disused Fane": {"Kurast Bazaar"},
        "Kurast Sewers": {"Kurast Bazaar", "Upper Kurast"},
    "Upper Kurast": {"Kurast Bazaar", "Kurast Sewers", "Forgotten Temple", "Forgotten Reliquary", "Kurast Causeway"},
        "Forgotten Temple": {"Upper Kurast"},
        "Forgotten Reliquary": {"Upper Kurast"},
    "Kurast Causeway": {"Upper Kurast", "Disused Reliquary", "Ruined Fane", "Travincal"},
        "Disused Reliquary": {"Kurast Causeway"},
        "Ruined Fane": {"Kurast Causeway"},
    "Travincal": {"Kurast Causeway", "Durance of Hate"},
    "Durance of Hate": {"Travincal", "Pandemonium Fortress"},

    # Act 4
    "Pandemonium Fortress": {"Harrogath", "Outer Steppes"},
    "Outer Steppes": {"Pandemonium Fortress", "Plains of Despair"},
    "Plains of Despair": {"Outer Steppes", "City of the Damned"},
    "City of the Damned": {"Plains of Despair", "River of Flame"},
    "River of Flame": {"City of the Damned", "Chaos Sanctuary"},
    "Chaos Sanctuary": {"River of Flame"},

    # Act 5
    "Harrogath": {"Bloody Foothills", "Nihlathak's Temple"},
        "Nihlathak's Temple": {"Harrogath", "Halls of Anguish"},
        "Halls of Anguish": {"Nihlathak's Temple", "Halls of Pain"},
        "Halls of Pain": {"Halls of Anguish", "Halls of Vaught"},
        "Halls of Vaught": {"Halls of Pain"},
    "Bloody Foothills": {"Harrogath", "Frigid Highlands"},
    "Frigid Highlands": {"Bloody Foothills", "Abaddon", "Arreat Plateau"},
        "Abaddon": {"Frigid Highlands"},
    "Arreat Plateau": {"Frigid Highlands", "Pit of Acheron", "Crystalline Passage"},
        "Pit of Acheron": {"Arreat Plateau"},
    "Crystalline Passage": {"Arreat Plateau", "Frozen River", "Glacial Trail"},
        "Frozen River": {"Crystalline Passage"},
    "Glacial Trail": {"Crystalline Passage", "Drifter Cavern", "Frozen Tundra"},
        "Drifter Cavern": {"Glacial Trail"},
    "Frozen Tundra": {"Glacial Trail", "Infernal Pit", "The Ancients' Way"},
        "Infernal Pit": {"Frozen Tundra"},
    "The Ancients' Way": {"Icy Cellar", "Arreat Summit"},
        "Icy Cellar": {"The Ancients' Way"},
    "Arreat Summit": {"Worldstone Keep"},
    "Worldstone Keep": {"Arreat Summit", "Throne of Destruction"},
    "Throne of Destruction": {"Worldstone Keep", "Worldstone Chamber"},
    "Worldstone Chamber": {},
}

noita_regions: Set[str] = set(noita_connections.keys()).union(*noita_connections.values())
