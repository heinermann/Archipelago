from typing import List, NamedTuple

# from worlds.generic import Rules as GenericRules
from . import Diablo2World


class EntranceLock(NamedTuple):
    source: str
    destination: str
    event: str


entrance_locks: List[EntranceLock] = [
    EntranceLock("Rogue Encampment", "Lut Gholein", "Go East"),
    EntranceLock("Lut Gholein", "Harem", "Invited to Palace"),
    EntranceLock("Tal Rasha's Tomb", "Tal Rasha's Chamber", "Place Horadric Staff on Orifice"),
    EntranceLock("Lut Gholein", "Kurast Docks", "Sail East"),
    EntranceLock("Travincal", "Durance of Hate", "Smash the Compelling Orb"),
    EntranceLock("Durance of Hate", "Pandemonium Fortress", "Portal to Pandemonium Fortress"),
]

entrance_locks_expansion: List[EntranceLock] = [
    EntranceLock("Pandemonium Fortress", "Harrogath", "Portal to Harrogath"),
    EntranceLock("Arreat Summit", "Worldstone Keep", "Defeat the Ancients"),
]


# ----------------
# Main Function
# ----------------


def create_all_rules(world: Diablo2World) -> None:
    "TODO"
