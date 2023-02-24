import typing

from Options import Choice, Option, Toggle, Range, DeathLink, DefaultOnToggle


class NumResearches(Range):
    """Number of research tree items."""
    display_name = "Total Locations"
    range_start = 50
    range_end = 400
    default = 100


class NumCarePackages(Range):
    """Number of location checks which are added to the playthrough."""
    display_name = "Total Locations"
    range_start = 75
    range_end = 500
    default = 100


class DLC(Choice):
    """DLC content to include."""
    display_name = "DLC"
    option_vanilla = 0
    option_spaced_out = 1
    default = 0


class DeathLinkDupe(DeathLink):
    """When a Duplicant in your colony dies, everyone else dies. Of course the reverse is true too."""


# TODO
#class TechTreeInformation(Choice):
#    """How much information should be displayed in the tech tree."""
#    display_name = "Technology Tree Information"
#    option_none = 0
#    option_advancement = 1
#    option_full = 2
#    default = 2


class Monument(Choice):
    """Ingredients to build a Great Monument."""
    display_name = "Great Monument"
    option_vanilla = 0
    option_randomize_recipe = 1
    default = 1


class Goal(Choice):
    """Goal required to complete the game."""
    display_name = "Goal"
    option_any = 0
    option_home_sweet_home = 1
    option_the_great_escape = 2
    option_all = 3
    default = 0


# Temporary notes (TODO not going to think about research separation right now beyond this):
# - Progressive Planter (Planter Box, Farm Tile, Hydroponic Farm)
# - Progressive Battery (Battery, Jumbo Battery, Smart Battery)
# - Progressive Wire (Wire, Heavi-Watt Wire, Conductive Wire, Heavi-Watt Conductive Wire)
# - Progressive Wire Bridge (Wire Bridge, Heavi-Watt Joint Plate, Conductive Wire Bridge)
# - Progressive Power Transformer (Power Transformer, Large Power Transformer)
# - Progressive Cooking Station (Microbe Musher, Electric Grill, Gas Range)
# - Progressive Research Station (Research Station, Super Computer, Materials Study Terminal, Virtual Planetarium)
# - Progressive Sink (Wash Basin, Sink)
# - Progressive Toilet (Outhouse, Lavatory, Wall Toilet)
# - Progressive Shower (Shower, Decontamination Shower)
# - Progressive Liquid Pipe (Liquid Pipe, Liquid Bridge/Liquid Vent, Insulated Liquid Pipe, Radiant Liquid Pipe)
# - Progressive Gas Pipe (Gas Pipe, Gas Bridge/Gas Vent, Insulated Gas Pipe, High Pressure Gas Vent)
# - Progressive Door (Pneumatic Door, Manual Airlock, Mechanized Airlock)
# - Progressive Tile (Tile, Airflow Tile/Mesh Tile, Insulated Tile) (Metal Tile, Bunker Tile) (Carpeted Tile, Plastic Tile, Window Tile)
# - Progressive Sculpting Block (Sculpting Block, Large Sculpting Block, Metal Block, Marble Block)
# - Progressive Monument (Monument Base, Monument Midsection, Monument Top)
# - Progressive Canvas (Blank Canvas, Landscape Canvas, Portrait Canvas)
# - Progressive Lighting (Lamp, Ceiling Light, Sun Lamp)
# - Progressive Flower Pot (Flower Pot, Wall Pot, Hanging Pot, Aero Pot)
# - Progressive Automation Wire (Automation Wire, Automation Wire Bridge, Automation Ribbon, Automation Ribbon Bridge)
# - Progressive Food Storage (Ration Box, Refrigerator)
# - Progressive Storage (Storage Bin, Smart Storage Bin)


#class ResearchType(Choice):
#    """Splits the unlockable buildings into separate items instead of research. If "Progressive" is chosen, merges some buildings such as pipes into multiple copies of "Progressive Pipe"."""
#    display_name = "Research Type"
#    option_vanilla = 0
#    option_progressive_vanilla = 1
#    option_split = 2
#    option_progressive_split = 3
#    default = 0


class StartingResearch(Choice):
    """Allows you to start with all the first tier research for faster early game progression."""
    display_name = "Starting Buildings"
    option_vanilla = 0
    option_basics = 1
    default = 0


class BuildingCostMultiplier(Range):
    """Modifies building cost (percentage)."""
    display_name = "Building Cost"
    range_start = 1
    range_end = 300
    default = 100


class ResearchCostMultiplier(Range):
    """Modifies research cost (percentage)."""
    display_name = "Research Cost"
    range_start = 1
    range_end = 300
    default = 100


class TechTreeLayout(Choice):
    """Selects how the tech tree nodes are interwoven."""
    display_name = "Technology Tree Layout"
    option_single = 0
    option_small_diamonds = 1
    option_medium_diamonds = 2
    option_large_diamonds = 3
    option_small_pyramids = 4
    option_medium_pyramids = 5
    option_large_pyramids = 6
    option_small_funnels = 7
    option_medium_funnels = 8
    option_large_funnels = 9
    option_trees = 10
    option_choices = 11
    default = 0


class CarePackages(DefaultOnToggle):
    """Shuffle care packages"""


class CarePackageTraps(Toggle):
    """Add traps that come from the Printing Pod (i.e. Morb)"""


class ColonyTraps(Toggle):
    """Add traps that get applied globally or to random Duplicants (i.e. random disease)"""


oni_options: typing.Dict[str, type(Option)] = {
    "dlc": DLC,
    #"tech_tree_information": TechTreeInformation,
    "monument": Monument,
    "goal": Goal,
    "tech_tree_layout": TechTreeLayout,
    "starting_research": StartingResearch,
    "building_cost": BuildingCostMultiplier,
    "research_cost": ResearchCostMultiplier,
    "death_link": DeathLinkDupe,
    "care_package_traps": CarePackageTraps,
    "colony_traps": ColonyTraps
}
