# Locations are specific points that you would obtain an item at.
from enum import IntEnum
from typing import Dict, NamedTuple, Optional, Set

from BaseClasses import Location


class D2Location(Location):
    game: str = "Diablo II"


class LocType(IntEnum):
    none = 0
    superunique = 1
    goldenchest = 2
    waypoint = 3


class LocationData(NamedTuple):
    id: int
    group: str
    ltype: LocType = LocType.none



# Mapping of items in each region.
# The superunique ltype is only used for the option to exclude them, so it makes sense to include a few
# superuniques you must kill anyway (or those that are genuinely unique and not just a reskin).
#
# goldenchest are just golden chest locations.
#
# waypoint for waypoints as checks.
#
# Always: 53
# Waypoints: 34
# Superuniques: 26 (additional)
# Golden Chests: 22
# Total: 135
# 120000 - 120135
location_region_mapping: Dict[str, Dict[str, LocationData]] = {
    # Act 1
    # Always: 12
    # Waypoints: 8
    # Superuniques: 7
    # Golden Chests: 6
    # Total: 33
    "Rogue Camp": {
        "Clear Den of Evil": LocationData(120000, "Act 1"),
        "Return Horadric Malus": LocationData(120001, "Act 1"),
    },
    "Den of Evil": {
        "Kill Corpsefire": LocationData(120002, "Act 1"),
    },
    "Cold Plains": {
        "Cold Plains Waypoint": LocationData(120003, "Act 1", LocType.waypoint),
        "Kill Bishibosh": LocationData(120004, "Act 1", LocType.superunique),
    },
    "The Cave": {
        "Kill Coldcrow": LocationData(120005, "Act 1", LocType.superunique),
        "Golden Chest (Cave)": LocationData(120006, "Act 1", LocType.goldenchest),
    },
    "Stony Field": {
        "Stony Field Waypoint": LocationData(120007, "Act 1", LocType.waypoint),
        "Read The Forgotten Tower Lectern": LocationData(120008, "Act 1"),
        "Kill Rakanishu": LocationData(120009, "Act 1", LocType.superunique),
    },
    "Dark Wood": {
        "Dark Wood Waypoint": LocationData(120010, "Act 1", LocType.waypoint),
        "Kill Treehead Woodfist": LocationData(120011, "Act 1", LocType.superunique),
        "Tree of Inifuss": LocationData(120012, "Act 1"),
    },
    "Black Marsh": {
        "Black Marsh Waypoint": LocationData(120013, "Act 1", LocType.waypoint),
    },
    "Tristram": {
        "Wirt's Body": LocationData(120014, "Act 1"),
        "Rescue Cain": LocationData(120015, "Act 1"),
        "Kill Griswold": LocationData(120016, "Act 1"),
    },
    "Burial Grounds": {
        "Kill Blood Raven": LocationData(120017, "Act 1"),
    },
    "The Forgotten Tower": {
        "Kill The Countess": LocationData(120018, "Act 1"),
    },
    "Outer Cloister": {
        "Outer Cloister Waypoint": LocationData(120019, "Act 1", LocType.waypoint),
    },
    "Barracks": {
        "Kill The Smith": LocationData(120020, "Act 1"),
    },
    "Jail": {
        "Jail Level 1 Waypoint": LocationData(120021, "Act 1", LocType.waypoint),
        "Kill Pitspawn Fouldog": LocationData(120022, "Act 1", LocType.superunique),
    },
    "Inner Cloister": {
        "Inner Cloister Waypoint": LocationData(120023, "Act 1", LocType.waypoint),
    },
    "Cathedral": {
        "Kill Bone Ash": LocationData(120024, "Act 1", LocType.superunique),
    },
    "Catacombs": {
        "Catacombs Level 2 Waypoint": LocationData(120025, "Act 1", LocType.waypoint),
        "Kill Andariel": LocationData(120026, "Act 1"),
    },
    "The Crypt": {
        "Kill Bonebreaker": LocationData(120027, "Act 1", LocType.superunique),
        "Golden Chest (Crypt)": LocationData(120028, "Act 1", LocType.goldenchest),
    },
    "The Mausoleum": {
        "Golden Chest (Mausoleum)": LocationData(120029, "Act 1", LocType.goldenchest),
    },
    "Underground Passage": {
        "Golden Chest (Underground Passage)": LocationData(120030, "Act 1", LocType.goldenchest),
    },
    "The Hole": {
        "Golden Chest (Hole)": LocationData(120031, "Act 1", LocType.goldenchest),
    },
    "The Pit": {
        "Golden Chest (Pit)": LocationData(120032, "Act 1", LocType.goldenchest),
    },

    # Act 2
    # Note: We will ignore the false tombs of Tal Rasha
    # Always: 6
    # Waypoint: 8
    # Superuniques: 6
    # Golden Chests: 5
    # Total: 25
    "Lut Gholein Sewers": {
        "Sewers Level 2 Waypoint": LocationData(120033, "Act 2", LocType.waypoint),
        "Kill Radament": LocationData(120034, "Act 2"),
        "Golden Chest (Lut Gholein Sewers)": LocationData(120035, "Act 2", LocType.goldenchest),
    },
    "Dry Hills": {
        "Dry Hills Waypoint": LocationData(120036, "Act 2", LocType.waypoint),
    },
    "Far Oasis": {
        "Far Oasis Waypoint": LocationData(120037, "Act 2", LocType.waypoint),
        "Kill Beetleburst": LocationData(120038, "Act 2", LocType.superunique),
    },
    "Claw Viper Temple": {
        "Smash Tainted Sun Altar": LocationData(120039, "Act 2"),
        "Kill Fangskin": LocationData(120040, "Act 2", LocType.superunique),
    },
    "Palace Cellar": {
        "Palace Cellar Level 1 Waypoint": LocationData(120041, "Act 2", LocType.waypoint),
        "Kill Fire Eye": LocationData(120042, "Act 2", LocType.superunique),
    },
    "Arcane Sanctuary": {
        "Arcane Sanctuary Waypoint": LocationData(120043, "Act 2", LocType.waypoint),
        "Read Horazon's Journal": LocationData(120044, "Act 2"),
        "Kill The Summoner": LocationData(120045, "Act 2"),
    },
    "Canyon of the Magi": {
        "Canyon of the Magi Waypoint": LocationData(120046, "Act 2", LocType.waypoint),
    },
    "Tal Rasha's Chamber": {
        "Kill Duriel": LocationData(120047, "Act 2"),
    },
    "Lost City": {
        "Lost City Waypoint": LocationData(120048, "Act 2", LocType.waypoint),
        "Kill Dark Elder": LocationData(120049, "Act 2", LocType.superunique),
    },
    "Halls of the Dead": {
        "Halls of the Dead Level 2 Waypoint": LocationData(120050, "Act 2", LocType.waypoint),
        "Golden Chest (Halls of the Dead)": LocationData(120051, "Act 2", LocType.goldenchest),
        "Kill Bloodwitch The Wild": LocationData(120052, "Act 2", LocType.superunique),
    },
    "Maggot Lair": {
        "Golden Chest (Maggot Lair)": LocationData(120053, "Act 2", LocType.goldenchest),
        "Kill Coldworm the Burrower": LocationData(120054, "Act 2"),
    },
    "The Stony Tomb": {
        "Kill Creeping Feature": LocationData(120055, "Act 2", LocType.superunique),
        "Golden Chest (Stony Tomb)": LocationData(120056, "Act 2", LocType.goldenchest),
    },
    "The Ancient Tunnels": {
        "Golden Chest (Ancient Tunnels)": LocationData(120057, "Act 2", LocType.goldenchest),
    },

    # Act 3 (TODO I think there are more golden chests in this act)
    # Always: 10
    # Waypoint: 8
    # Superuniques: 4
    # Golden Chests: 5
    # Total: 27
    "Kurast Docks": {
        "Give Jade Figurine to Meshif": LocationData(120058, "Act 3"),
    },
    "Spider Forest": {
        "Spider Forest Waypoint": LocationData(120059, "Act 3", LocType.waypoint),
    },
    "Great Marsh": {
        "Great Marsh Waypoint": LocationData(120060, "Act 3", LocType.waypoint),
    },
    "Flayer Jungle": {
        "Flayer Jungle Waypoint": LocationData(120061, "Act 3", LocType.waypoint),
        "Activate the Gidbinn": LocationData(120062, "Act 3"),
        "Kill Stormtree": LocationData(120063, "Act 3", LocType.superunique),
    },
    "Lower Kurast": {
        "Lower Kurast Waypoint": LocationData(120064, "Act 3", LocType.waypoint),
    },
    "Kurast Bazaar": {
        "Kurast Bazaar Waypoint": LocationData(120065, "Act 3", LocType.waypoint),
    },
    "Upper Kurast": {
        "Upper Kurast Waypoint": LocationData(120066, "Act 3", LocType.waypoint),
    },
    "Ruined Temple": {
        "Interact with Lam Esen's Lectern": LocationData(120067, "Act 3"),
        "Kill Battlemaid Sarina": LocationData(120068, "Act 3", LocType.superunique),
    },
    "Travincal": {
        "Travincal Waypoint": LocationData(120069, "Act 3", LocType.waypoint),
        "Kill Council Member Ismail Vilehand": LocationData(120070, "Act 3"),
        "Kill Council Member Geleb Flamefinger": LocationData(120071, "Act 3"),
        "Kill Council Member Toorc Icefist": LocationData(120072, "Act 3"),
    },
    "Durance of Hate": {
        "Durance of Hate Level 2 Waypoint": LocationData(120073, "Act 3", LocType.waypoint),
        "Kill Council Member Wyand Voidbringer": LocationData(120074, "Act 3"),
        "Kill Council Member Maffer Dragonhand": LocationData(120075, "Act 3"),
        "Kill Council Member Bremm Sparkfist": LocationData(120076, "Act 3"),
        "Kill Mephisto": LocationData(120077, "Act 3"),
    },
    "Spider Cavern": {
        "Golden Chest (Spider Cavern)": LocationData(120078, "Act 3", LocType.goldenchest),
        "Kill Sszark The Burning": LocationData(120079, "Act 3", LocType.superunique),
    },
    "Flayer Dungeon": {
        "Golden Chest (Flayer Dungeon)": LocationData(120080, "Act 3", LocType.goldenchest),
        "Kill Witch Doctor Endugu": LocationData(120081, "Act 3", LocType.superunique),
    },
    "Kurast Sewers": {
        "Golden Chest (Kurast Sewers)": LocationData(120082, "Act 3", LocType.goldenchest),
        "Kill Icehawk Riftwing": LocationData(120083, "Act 3", LocType.superunique),
    },
    "Arachnid Lair": {
        "Golden Chest (Arachnid Lair)": LocationData(120084, "Act 3", LocType.goldenchest),
    },
    "Swampy Pit": {
        "Golden Chest (Swampy Pit)": LocationData(120085, "Act 3", LocType.goldenchest),
    },

    # Act 4
    # Always: 12
    # Waypoint: 2
    # Superuniques: 0
    # Golden Chests: 0
    # Total: 14
    "Plains of Despair": {
        "Kill Izual": LocationData(120086, "Act 4"),
    },
    "City of the Damned": {
        "City of the Damned Waypoint": LocationData(120087, "Act 4", LocType.waypoint),
    },
    "River of Flame": {
        "River of Flame Waypoint": LocationData(120088, "Act 4", LocType.waypoint),
        "Kill Hephasto the Armorer": LocationData(120089, "Act 4"),
        "Destroy Mephisto's Soulstone": LocationData(120090, "Act 4"),
    },
    "Chaos Sanctuary": {
        "Kill Infector of Souls": LocationData(120091, "Act 4"),
        "Kill Grand Vizier of Chaos": LocationData(120092, "Act 4"),
        "Kill Lord De Seis": LocationData(120093, "Act 4"),
        "Break Diablo Seal 1": LocationData(120094, "Act 4"),
        "Break Diablo Seal 2": LocationData(120095, "Act 4"),
        "Break Diablo Seal 3": LocationData(120096, "Act 4"),
        "Break Diablo Seal 4": LocationData(120097, "Act 4"),
        "Break Diablo Seal 5": LocationData(120098, "Act 4"),
        "Kill Diablo": LocationData(120099, "Act 4"),
    },

    # Act 5
    # Always: 13
    # Waypoint: 8
    # Superuniques: 9
    # Golden Chests: 6
    # Total: 36
    "Harrogath": {
        "Free Barbarians": LocationData(120100, "Act 5"),
        "Free Anya": LocationData(120101, "Act 5"),
    },
    "Bloody Foothills": {
        "Kill Shenk the Overseer": LocationData(120102, "Act 5"),
        "Kill Dac Farren": LocationData(120103, "Act 5", LocType.superunique),
    },
    "Frigid Highlands": {
        "Frigid Highlands Waypoint": LocationData(120104, "Act 5", LocType.waypoint),
        "Kill Eldritch the Rectifier": LocationData(120105, "Act 5", LocType.superunique),
        "Kill Sharptooth Slayer": LocationData(120106, "Act 5", LocType.superunique),
        "Kill Eyeback the Unleashed": LocationData(120107, "Act 5", LocType.superunique),
    },
    "Arreat Plateau": {
        "Arreat Plateau Waypoint": LocationData(120108, "Act 5", LocType.waypoint),
        "Kill Thresh Socket": LocationData(120109, "Act 5", LocType.superunique),
    },
    "Crystalline Passage": {
        "Crystalline Passage Waypoint": LocationData(120110, "Act 5", LocType.waypoint),
    },
    "Frozen River": {
        "Kill Frozenstein": LocationData(120111, "Act 5", LocType.superunique),
    },
    "Glacial Trail": {
        "Glacial Trail Waypoint": LocationData(120112, "Act 5", LocType.waypoint),
        "Kill Bonesaw Breaker": LocationData(120113, "Act 5", LocType.superunique),
        "Golden Chest (Glacial Trail)": LocationData(120114, "Act 5", LocType.goldenchest),
    },
    "Nihlathak's Temple": {
        "Kill Pindleskin": LocationData(120115, "Act 5", LocType.superunique),
    },
    "Halls of Pain": {
        "Halls of Pain Waypoint": LocationData(120116, "Act 5", LocType.waypoint),
    },
    "Halls of Vaught": {
        "Kill Nihlathak": LocationData(120117, "Act 5"),
    },
    "Frozen Tundra": {
        "Frozen Tundra Waypoint": LocationData(120118, "Act 5", LocType.waypoint),
    },
    "The Ancients' Way": {
        "The Ancients' Way Waypoint": LocationData(120119, "Act 5", LocType.waypoint),
    },
    "Arreat Summit": {
        "Kill Talic": LocationData(120120, "Act 5"),
        "Kill Madawc": LocationData(120121, "Act 5"),
        "Kill Korlic": LocationData(120122, "Act 5"),
    },
    "Worldstone Keep": {
        "Worldstone Keep Level 2 Waypoint": LocationData(120123, "Act 5", LocType.waypoint),
    },
    "Throne of Destruction": {
        "Kill Colenzo The Annihilator": LocationData(120124, "Act 5"),
        "Kill Achmel The Cursed": LocationData(120125, "Act 5"),
        "Kill Bartuc The Bloody": LocationData(120126, "Act 5"),
        "Kill Ventar The Unholy": LocationData(120127, "Act 5"),
        "Kill Lister The Tormentor": LocationData(120128, "Act 5"),
    },
    "Worldstone Chamber": {
        "Kill Baal": LocationData(120129, "Act 5"),
    },
    "Abaddon": {
        "Golden Chest (Abaddon)": LocationData(120130, "Act 5", LocType.goldenchest),
    },
    "Pit of Acheron": {
        "Golden Chest (Pit of Acheron)": LocationData(120131, "Act 5", LocType.goldenchest),
    },
    "Drifter Cavern": {
        "Golden Chest (Drifter Cavern)": LocationData(120132, "Act 5", LocType.goldenchest),
    },
    "Icy Cellar": {
        "Kill Snapchip Shatter": LocationData(120133, "Act 5", LocType.superunique),
        "Golden Chest (Icy Cellar)": LocationData(120134, "Act 5", LocType.goldenchest),
    },
    "Infernal Pit": {
        "Golden Chest (Infernal Pit)": LocationData(120135, "Act 5", LocType.goldenchest),
    },
}


# Iterating the hidden chest and pedestal locations here to avoid clutter above
def generate_location_entries(locname: str, locinfo: LocationData) -> Dict[str, int]:
    return {locname: locinfo.id}


location_name_groups: Dict[str, Set[str]] = {
    "Act 1": set(), "Act 2": set(), "Act 3": set(), "Act 4": set(), "Act 5": set()
}
location_name_to_id: Dict[str, int] = {}


for location_group in location_region_mapping.values():
    for locname, locinfo in location_group.items():
        location_name_to_id.update(generate_location_entries(locname, locinfo))
        location_name_groups[locinfo.group].add(locname)
