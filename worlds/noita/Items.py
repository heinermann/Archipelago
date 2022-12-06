import itertools
from typing import Dict, NamedTuple, Optional, List, Set
from BaseClasses import Item, ItemClassification, MultiWorld


class ItemData(NamedTuple):
    code: Optional[int]
    group: str
    classification: ItemClassification = ItemClassification.progression
    required_num: int = 0


class NoitaItem(Item):
    game: str = "Noita"


def create_item(player: int, name: str) -> Item:
    item_data = item_table[name]
    return NoitaItem(name, item_data.classification, item_data.code, player)


def create_all_items(world: MultiWorld, player: int) -> None:
    pool_option = world.bad_effects[player].value
    total_locations = world.total_locations[player].value

    # Generate item pool
    itempool: List = []
    for item_name, count in required_items.items():
        itempool += [item_name] * count

    # Add other junk to the pool
    junk_pool = item_pool_weights[pool_option]
    for i in range(1, total_locations + 1):
        itempool += world.random.choices(list(junk_pool.keys()), weights=list(junk_pool.values()))

    # Convert itempool into real items
    world.itempool += [create_item(player, name) for name in itempool]


# 110000 - 110021
item_table: Dict[str, ItemData] = {
    "Bad":                                  ItemData(110000, "Traps", ItemClassification.trap),
    "Heart":                                ItemData(110001, "Pickups", ItemClassification.useful),
    "Refresh":                              ItemData(110002, "Pickups", ItemClassification.filler),
    "Potion":                               ItemData(110003, "Items", ItemClassification.filler),
    "Gold (10)":                            ItemData(110004, "Gold", ItemClassification.filler),
    "Gold (50)":                            ItemData(110005, "Gold", ItemClassification.filler),
    "Gold (200)":                           ItemData(110006, "Gold", ItemClassification.filler),
    "Gold (1000)":                          ItemData(110007, "Gold", ItemClassification.filler),
    "Wand (Tier 1)":                        ItemData(110008, "Wands", ItemClassification.useful),
    "Wand (Tier 2)":                        ItemData(110009, "Wands", ItemClassification.useful),
    "Wand (Tier 3)":                        ItemData(110010, "Wands", ItemClassification.useful),
    "Wand (Tier 4)":                        ItemData(110011, "Wands", ItemClassification.useful),
    "Wand (Tier 5)":                        ItemData(110012, "Wands", ItemClassification.useful),
    "Wand (Tier 6)":                        ItemData(110013, "Wands", ItemClassification.useful),
    "Perk (Fire Immunity)":                 ItemData(110014, "Perks", ItemClassification.progression, 1),
    "Perk (Toxic Immunity)":                ItemData(110015, "Perks", ItemClassification.progression, 1),
    "Perk (Explosion Immunity)":            ItemData(110016, "Perks", ItemClassification.progression, 1),
    "Perk (Melee Immunity)":                ItemData(110017, "Perks", ItemClassification.progression, 1),
    "Perk (Electricity Immunity)":          ItemData(110018, "Perks", ItemClassification.progression, 1),
    "Perk (Tinker With Wands Everywhere)":  ItemData(110019, "Perks", ItemClassification.progression, 1),
    "Perk (All-Seeing Eye)":                ItemData(110020, "Perks", ItemClassification.progression, 1),
    "Perk (Extra Life)":                    ItemData(110021, "Repeatable Perks", ItemClassification.useful),
}


default_weights: Dict[str, int] = {
    "Wand (Tier 1)":    10,
    "Potion":           35,
    "Refresh":          25,
    "Heart":            25,
    "Wand (Tier 2)":    9,
    "Wand (Tier 3)":    8,
    "Bad":              15,
    "Gold (200)":       15,
    "Wand (Tier 4)":    7,
    "Wand (Tier 5)":    6,
    "Gold (1000)":      5,
    "Wand (Tier 6)":    4,
    "Perk (Extra Life)": 4
}

no_bad_weights: Dict[str, int] = {
    "Wand (Tier 1)":    10,
    "Potion":           35,
    "Refresh":          25,
    "Heart":            25,
    "Wand (Tier 2)":    9,
    "Wand (Tier 3)":    8,
    "Bad":              0,
    "Gold (200)":       15,
    "Wand (Tier 4)":    7,
    "Wand (Tier 5)":    6,
    "Gold (1000)":      5,
    "Wand (Tier 6)":    4,
    "Perk (Extra Life)": 4
}

item_pool_weights: Dict[int, Dict[str, int]] = {
    0:      no_bad_weights,
    1:      default_weights
}


# These helper functions make the comprehensions below more readable
def get_item_group(item_name: str) -> str:
    return item_table[item_name].group


def item_is_filler(item_name: str) -> bool:
    return item_table[item_name].classification == ItemClassification.filler


filler_items: List[str] = list(filter(item_is_filler, item_table.keys()))
item_name_to_id: Dict[str, int] = {name: data.code for name, data in item_table.items()}

item_name_groups: Dict[set, Set[str]] = {
    group: set(item_names)
    for group, item_names in itertools.groupby(item_table, get_item_group)
}

required_items: Dict[str, int] = {
    name: data.required_num
    for name, data in item_table.items() if data.required_num > 0
}
