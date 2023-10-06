from typing import Dict

from BaseClasses import Item, ItemClassification, Location, MultiWorld, Region
from . import Items, Locations


def create_event(player: int, name: str) -> Item:
    return Items.D2Item(name, ItemClassification.progression, None, player)


def create_location(player: int, name: str, region: Region) -> Location:
    return Locations.D2Location(player, name, None, region)


def create_locked_location_event(multiworld: MultiWorld, player: int, region_name: str, item: str) -> Location:
    region = multiworld.get_region(region_name, player)

    new_location = create_location(player, item, region)
    new_location.place_locked_item(create_event(player, item))

    region.locations.append(new_location)
    return new_location


def create_all_events(multiworld: MultiWorld, player: int) -> None:
    for region, event in event_locks.items():
        create_locked_location_event(multiworld, player, region, event)

    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)


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
