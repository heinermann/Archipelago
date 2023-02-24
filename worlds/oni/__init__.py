import string

from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld

from . import Options, Items, Locations, Regions, Rules, Events
from .Options import noita_options

# TODO: Gate holy mountain access behind an event that triggers when you visit the same holy mountain?


class ONIWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Oxygen Not Included integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Heinermann"]
    )]
    theme = "dirt"


# Keeping World slim so that it's easier to comprehend
class ONIWorld(World):
    """
    Oxygen Not Included is a space-colony simulation game that revolves around heavy resource management and strategic
    decision making tied to a unique physics engine. It prioritizes the procurement of food, oxygen, and water among
    handling game mechanics such as air pressure, temperature, germs, automation, and more.
    """
    game: str = "Oxygen Not Included"
    option_definitions = Options.oni_options
    topology_present = False

    item_name_to_id = Items.item_name_to_id
    # TODO location_name_to_id = Locations.location_name_to_id

    data_version = 1
    web = ONIWeb()

    def get_option(self, name):
        return getattr(self.multiworld, name)[self.player].value

    # Returned items will be sent over to the client
    # TODO return new AP tech tree from here
    def fill_slot_data(self):
        slot_data = {
            "seed": self.multiworld.seed_name,
        }

        for option_name in self.option_definitions:
            slot_data[option_name] = self.get_option(option_name)

        return slot_data

    def create_regions(self) -> None:
        Regions.create_all_regions_and_connections(self.multiworld, self.player)

    def create_items(self) -> None:
        Items.create_all_items(self.multiworld, self.player)

    def set_rules(self) -> None:
        Rules.create_all_rules(self.multiworld, self.player)

    # Generate victory conditions and other shenanigans
    def generate_basic(self) -> None:
        Events.create_all_events(self.multiworld, self.player)

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(Items.filler_items)
