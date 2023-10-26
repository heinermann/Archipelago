from Options import AssembleOptions, DeathLink, DefaultOnToggle, PerGameCommonOptions, Toggle
from dataclasses import dataclass


class Traps(Toggle):
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


class IsLordOfDestruction(DefaultOnToggle):
    """Includes the Diablo II: Lord of Destruction expansion content."""
    display_name = "Is Expansion"


@dataclass
class Diablo2Options(PerGameCommonOptions):
    death_link: DeathLink
    traps: Traps
    waypoints_as_checks: WaypointsAsChecks
    superuniques_as_checks: SuperuniquesAsChecks
    goldenchests_as_checks: GoldenChestsAsChecks
    is_expansion: IsLordOfDestruction
