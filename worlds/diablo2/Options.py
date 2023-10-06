from typing import Dict
from Options import AssembleOptions, DeathLink, DefaultOnToggle, Toggle


class Traps(DefaultOnToggle):
    """Whether negative effects that can hinder your character are added to the item pool."""
    display_name = "Traps"


class WaypointsAsChecks(Toggle):
    """Discovering a waypoint will also unlock an Archipelago item."""
    display_name = "Waypoints as Checks"


class SuperuniquesAsChecks(Toggle):
    """Killing more obscure superuniques will unlock an Archipelago item."""
    display_name = "Superuniques as Checks"


class GoldenChestsAsChecks(Toggle):
    """Opening golden chests will unlock an Archipelago item."""
    display_name = "Golden Chests as Checks"


diablo2_options: Dict[str, AssembleOptions] = {
    "death_link": DeathLink,
    "traps": Traps,
    "waypoints_as_checks": WaypointsAsChecks,
    "superuniques_as_checks": SuperuniquesAsChecks,
    "goldenchests_as_checks": GoldenChestsAsChecks,
}
