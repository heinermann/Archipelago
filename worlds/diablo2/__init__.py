from BaseClasses import Item, Tutorial
from worlds.AutoWorld import WebWorld, World
from . import Events, Items, Locations, Options, Regions, Rules


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
    option_definitions = Options.diablo2_options

    item_name_to_id = Items.item_name_to_id
    location_name_to_id = Locations.location_name_to_id

    item_name_groups = Items.item_name_groups
    location_name_groups = Locations.location_name_groups
    data_version = 2

    web = Diablo2Web()

    # Returned items will be sent over to the client
    def fill_slot_data(self):
        return {name: getattr(self.multiworld, name)[self.player].value for name in self.option_definitions}

    def create_regions(self) -> None:
        Regions.create_all_regions_and_connections(self.multiworld, self.player)
        Events.create_all_events(self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        return Items.create_item(self.player, name)

    def create_items(self) -> None:
        Items.create_all_items(self.multiworld, self.player)

    def set_rules(self) -> None:
        Rules.create_all_rules(self.multiworld, self.player)

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(Items.filler_items)
