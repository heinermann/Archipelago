from typing import Dict

from BaseClasses import Item, ItemClassification, Location, Region
from .Items import D2Item
from .Locations import D2Location
from . import Diablo2World


def create_event(player: int, name: str) -> Item:
    return D2Item(name, ItemClassification.progression, None, player)


def create_location(player: int, name: str, region: Region) -> Location:
    return D2Location(player, name, None, region)


def create_locked_location_event(player: int, region: Region, item: str) -> Location:
    new_location = create_location(player, item, region)
    new_location.place_locked_item(create_event(player, item))

    region.locations.append(new_location)
    return new_location


def create_all_events(world: Diablo2World, regions: Dict[str, Region]) -> None:
    for region_name, event in event_locks.items():
        region = regions[region_name]
        create_locked_location_event(world.player, region, event)

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)


# Maps region names to event names
event_locks: tuple[str, str] = {
    ("Worldstone Chamber", "Victory"),
    ("Rogue Encampment", "Go East"),
    ("Lut Gholein", "Invited to Palace"),
    ("Tal Rasha's Tomb", "Place Horadric Staff on Orifice"),
    ("Lut Gholein", "Sail East"),
    ("Travincal", "Smash the Compelling Orb"),
    ("Durance of Hate", "Portal to Pandemonium Fortress"),
    ("Pandemonium Fortress", "Portal to Harrogath"),
    ("Arreat Summit", "Defeat the Ancients"),
}
