from BaseClasses import Item, Tutorial
from worlds.AutoWorld import WebWorld, World
from . import Items, Locations, Regions, Rules
from .Options import Diablo2Options


class Diablo2Web(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Diablo II integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Heinermann"]
    )]
    theme = "stone"
    bug_report_page = ""


# Keeping World slim so that it's easier to comprehend
class Diablo2World(World):
    """
    TODO
    """

    game = "Diablo II"
    options_dataclass = Diablo2Options
    options: Diablo2Options

    item_name_to_id = Items.item_name_to_id
    location_name_to_id = Locations.location_name_to_id

    item_name_groups = Items.item_name_groups
    location_name_groups = Locations.location_name_groups
    data_version = 1

    web = Diablo2Web()

    # Returned items will be sent over to the client
    def fill_slot_data(self):
        return self.options.as_dict("death_link", "waypoints_as_checks", "superuniques_as_checks",
                                    "goldenchests_as_checks")

    def create_regions(self) -> None:
        Regions.create_all_regions_and_connections(self)

    def create_item(self, name: str) -> Item:
        return Items.create_item(self.player, name)

    def create_items(self) -> None:
        Items.create_all_items(self)

    def set_rules(self) -> None:
        Rules.create_all_rules(self)

    def get_filler_item_name(self) -> str:
        return self.random.choice(Items.filler_items)
