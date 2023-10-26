import itertools
from collections import Counter
from typing import Dict, List, NamedTuple, Set

from BaseClasses import Item, ItemClassification
from . import Diablo2World


class ItemData(NamedTuple):
    code: int
    act: int
    group: str
    classification: ItemClassification = ItemClassification.progression
    required_num: int = 0


class D2Item(Item):
    game: str = "Diablo II"


def create_item(player: int, name: str) -> Item:
    item_data = item_table[name]
    return D2Item(name, item_data.classification, item_data.code, player)


def create_fixed_item_pool() -> List[str]:
    required_items: Dict[str, int] = {name: data.required_num for name, data in item_table.items()}
    return list(Counter(required_items).elements())


def create_random_items(world: Diablo2World, random_count: int) -> List[str]:
    filler_pool = filler_weights.copy()
    if world.options.traps.value == 0:
        del filler_pool["Trap"]

    return world.random.choices(
        population=list(filler_pool.keys()),
        weights=list(filler_pool.values()),
        k=random_count
    )


def create_all_items(world: Diablo2World) -> None:
    sum_locations = len(world.multiworld.get_unfilled_locations(world.player))

    itempool = create_fixed_item_pool()

    random_count = sum_locations - len(itempool)
    itempool += create_random_items(world, random_count)

    world.multiworld.itempool += [world.create_item(name) for name in itempool]


# Total: 33
# 120000 - 120041
item_table: Dict[str, ItemData] = {
    "Trap":                                 ItemData(120000, 0, "Traps", ItemClassification.trap),

    # Act 1
    # 8
    "Act 1 Merc Unlock":                    ItemData(120001, 1, "Mercenary", ItemClassification.useful, 1),
    "Scroll of Inifuss":                    ItemData(120002, 1, "Quest", ItemClassification.progression, 1),
    "Wirt's Leg":                           ItemData(120003, 1, "Quest", ItemClassification.useful, 1),
    "Horadric Malus":                       ItemData(120004, 1, "Quest", ItemClassification.useful, 1),
    "Skill Reset (Akara)":                  ItemData(120005, 1, "Reward", ItemClassification.useful, 1),
    "Free Item Identification (Cain)":      ItemData(120006, 1, "Reward", ItemClassification.useful, 1),
    "Item Imbuement (Charsi)":              ItemData(120007, 1, "Reward", ItemClassification.useful, 1),
    "One Skill Point (Akara)":              ItemData(120008, 1, "Reward", ItemClassification.useful, 1),

    # Act 2
    # 8
    "Act 2 Merc Unlock":                    ItemData(120009, 2, "Mercenary", ItemClassification.useful, 1),
    "Book of Skill":                        ItemData(120010, 2, "Reward", ItemClassification.useful, 1),
    "Lower Vendor Prices":                  ItemData(120011, 2, "Reward", ItemClassification.useful, 1),
    "Horadric Cube":                        ItemData(120012, 2, "Quest", ItemClassification.progression, 1),
    "Staff of Kings":                       ItemData(120013, 2, "Quest", ItemClassification.progression, 1),
    "Amulet of the Viper":                  ItemData(120014, 2, "Quest", ItemClassification.progression, 1),
    "Dispell Darkness":                     ItemData(120015, 2, "Quest", ItemClassification.useful, 1),
    "True Symbol of Tal Rasha's Tomb":      ItemData(120016, 2, "Quest", ItemClassification.progression, 1),

    # Act 3
    # 9
    "Act 3 Merc Unlock":                    ItemData(120017, 3, "Mercenary", ItemClassification.useful, 1),
    "The Golden Bird":                      ItemData(120018, 3, "Quest", ItemClassification.useful, 1),
    "The Gidbinn":                          ItemData(120019, 3, "Quest", ItemClassification.useful, 1),
    "Lam Esen's Tome":                      ItemData(120020, 3, "Quest", ItemClassification.useful, 1),
    "Khalim's Eye":                         ItemData(120021, 3, "Quest", ItemClassification.progression, 1),
    "Khalim's Brain":                       ItemData(120022, 3, "Quest", ItemClassification.progression, 1),
    "Khalim's Heart":                       ItemData(120023, 3, "Quest", ItemClassification.progression, 1),
    "Khalim's Flail":                       ItemData(120024, 3, "Quest", ItemClassification.progression, 1),
    "Mephisto's Soulstone":                 ItemData(120025, 3, "Quest", ItemClassification.useful, 1),

    # Act 4
    # 2
    "Hellforge Hammer":                     ItemData(120026, 4, "Quest", ItemClassification.useful, 1),
    "Two Skill Points (Tyrael)":            ItemData(120027, 4, "Reward", ItemClassification.useful, 1),

    # Act 5
    # 6
    "Act 5 Merc Unlock":                    ItemData(120028, 5, "Mercenary", ItemClassification.useful, 1),
    "Malah's Potion":                       ItemData(120029, 5, "Quest", ItemClassification.useful, 1),
    "Item Socketing (Larzuk)":              ItemData(120030, 5, "Reward", ItemClassification.useful, 1),
    "Scroll of Resistance":                 ItemData(120031, 5, "Reward", ItemClassification.useful, 1),
    "Item Inscription (Anya)":              ItemData(120032, 5, "Reward", ItemClassification.useful, 1),
    "One Level Up (Ancients)":              ItemData(120033, 5, "Reward", ItemClassification.useful, 1),

    # Filler Items
    "Skill Point":                          ItemData(120034, 0, "Stuff", ItemClassification.useful),
    "5 Stat Points":                        ItemData(120035, 0, "Stuff", ItemClassification.useful),
    "Gold (250)":                           ItemData(120036, 0, "Stuff", ItemClassification.filler),
    "Gold (1000)":                          ItemData(120037, 0, "Stuff", ItemClassification.filler),
    "Random Rune":                          ItemData(120038, 0, "Stuff", ItemClassification.filler),
    "Random Gem":                           ItemData(120039, 0, "Stuff", ItemClassification.filler),
    "Rare Ring":                            ItemData(120040, 0, "Stuff", ItemClassification.filler),
    "Rare Amulet":                          ItemData(120041, 0, "Stuff", ItemClassification.filler),
}

filler_weights: Dict[str, int] = {
    "Trap":             15,
    "Skill Point":      4,
    "5 Stat Points":    4,
    "Gold (250)":       20,
    "Gold (1000)":      10,
    "Random Rune":      8,
    "Random Gem":       8,
    "Rare Ring":        6,
    "Rare Amulet":      5,
}


# These helper functions make the comprehensions below more readable
def get_item_group(item_name: str) -> str:
    return item_table[item_name].group


def item_is_filler(item_name: str) -> bool:
    return item_table[item_name].classification == ItemClassification.filler


filler_items: List[str] = list(filter(item_is_filler, item_table.keys()))
item_name_to_id: Dict[str, int] = {name: data.code for name, data in item_table.items()}

item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in itertools.groupby(item_table, get_item_group)
}