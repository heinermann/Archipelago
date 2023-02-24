from BaseClasses import Item, ItemClassification, MultiWorld
from typing import Dict, NamedTuple


class ONIItem(Item):
    game: str = "Oxygen Not Included"


class ItemData(NamedTuple):
    code: int
    classification: ItemClassification = ItemClassification.filler
    count: int = 1

def create_all_items(world: MultiWorld, player: int) -> None:
    # TODO
    print("TODO")


oni_base_id: int = 57000

vanilla_research: Dict[str, ItemData] = {
    "Basic Farming": ItemData(oni_base_id + 0, ItemClassification.progression),
    "Meal Preparation": ItemData(oni_base_id + 1, ItemClassification.progression),
    "Agriculture": ItemData(oni_base_id + 2, ItemClassification.progression),
    "Food Repurposing": ItemData(oni_base_id + 3, ItemClassification.progression),
    "Ranching": ItemData(oni_base_id + 4, ItemClassification.progression),
    "Animal Control": ItemData(oni_base_id + 5, ItemClassification.progression),
    "Gourmet Meal Preparation": ItemData(oni_base_id + 6, ItemClassification.progression),
    "Power Regulation": ItemData(oni_base_id + 7, ItemClassification.progression),
    "Internal Combustion": ItemData(oni_base_id + 8, ItemClassification.progression),
    "Fossil Fuels": ItemData(oni_base_id + 9, ItemClassification.progression),
    "Plastic Manufacturing": ItemData(oni_base_id + 10, ItemClassification.progression),
    "Valve Miniaturization": ItemData(oni_base_id + 11, ItemClassification.progression),
    "Sound Amplifiers": ItemData(oni_base_id + 12, ItemClassification.progression),
    "Advanced Power Regulation": ItemData(oni_base_id + 13, ItemClassification.progression),
    "Low-Resistance Conductors": ItemData(oni_base_id + 14, ItemClassification.progression),
    "Renewable Energy": ItemData(oni_base_id + 15, ItemClassification.progression),
    "Employment": ItemData(oni_base_id + 16, ItemClassification.progression),
    "Brute-Force Refinement": ItemData(oni_base_id + 17, ItemClassification.progression),
    "Smart Storage": ItemData(oni_base_id + 18, ItemClassification.progression),
    "Solid Transport": ItemData(oni_base_id + 19, ItemClassification.progression),
    "Solid Control": ItemData(oni_base_id + 20, ItemClassification.progression),
    "Solid Management": ItemData(oni_base_id + 21, ItemClassification.progression),
    "Refined Renovations": ItemData(oni_base_id + 22, ItemClassification.progression),
    "Smelting": ItemData(oni_base_id + 23, ItemClassification.progression),
    "Superheated Forging": ItemData(oni_base_id + 24, ItemClassification.progression),
    "Advanced Research": ItemData(oni_base_id + 25, ItemClassification.progression),
    "Artificial Friends": ItemData(oni_base_id + 26, ItemClassification.progression),
    "Robotic Tools": ItemData(oni_base_id + 27, ItemClassification.progression),
    "Notification Systems": ItemData(oni_base_id + 28, ItemClassification.progression),
    "Pharmacology": ItemData(oni_base_id + 29, ItemClassification.progression),
    "Medical Equipment": ItemData(oni_base_id + 30, ItemClassification.progression),
    "Pathogen Diagnostics": ItemData(oni_base_id + 31, ItemClassification.progression),
    "Micro-Targeted Medicine": ItemData(oni_base_id + 32, ItemClassification.progression),
    "Plumbing": ItemData(oni_base_id + 33, ItemClassification.progression),
    "Air Systems": ItemData(oni_base_id + 34, ItemClassification.progression),
    "Liquid-Based Refinement Processes": ItemData(oni_base_id + 35, ItemClassification.progression),
    "Sanitation": ItemData(oni_base_id + 36, ItemClassification.progression),
    "Flow Redirection": ItemData(oni_base_id + 37, ItemClassification.progression),
    "Filtration": ItemData(oni_base_id + 38, ItemClassification.progression),
    "Distillation": ItemData(oni_base_id + 39, ItemClassification.progression),
    "Improved Plumbing": ItemData(oni_base_id + 40, ItemClassification.progression),
    "Liquid Tuning": ItemData(oni_base_id + 41, ItemClassification.progression),
    "Advanced Caffeination": ItemData(oni_base_id + 42, ItemClassification.progression),
    "Ventilation": ItemData(oni_base_id + 43, ItemClassification.progression),
    "Pressure Management": ItemData(oni_base_id + 44, ItemClassification.progression),
    "Temperature Modulation": ItemData(oni_base_id + 45, ItemClassification.progression),
    "HVAC": ItemData(oni_base_id + 46, ItemClassification.progression),
    "Catalytics": ItemData(oni_base_id + 47, ItemClassification.progression),
    "Decontamination": ItemData(oni_base_id + 48, ItemClassification.progression),
    "Portable Gasses": ItemData(oni_base_id + 49, ItemClassification.progression),
    "Improved Ventilation": ItemData(oni_base_id + 50, ItemClassification.progression),
    "Hazard Protection": ItemData(oni_base_id + 51, ItemClassification.progression),
    "Transit Tubes": ItemData(oni_base_id + 52, ItemClassification.progression),
    "Jetpacks": ItemData(oni_base_id + 53, ItemClassification.progression),
    "Interior Decor": ItemData(oni_base_id + 54, ItemClassification.progression),
    "Artistic Expression": ItemData(oni_base_id + 55, ItemClassification.progression),
    "Textile Production": ItemData(oni_base_id + 56, ItemClassification.progression),
    "Home Luxuries": ItemData(oni_base_id + 57, ItemClassification.progression),
    "Glass Blowing": ItemData(oni_base_id + 58, ItemClassification.progression),
    "Environmental Appreciation": ItemData(oni_base_id + 59, ItemClassification.progression),
    "Fine Art": ItemData(oni_base_id + 60, ItemClassification.progression),
    "High Culture": ItemData(oni_base_id + 61, ItemClassification.progression),
    "Renaissance Art": ItemData(oni_base_id + 62, ItemClassification.progression),
    "New Media": ItemData(oni_base_id + 63, ItemClassification.progression),
    "Monuments": ItemData(oni_base_id + 64, ItemClassification.progression),
    "Smart Home": ItemData(oni_base_id + 65, ItemClassification.progression),
    "Generic Sensors": ItemData(oni_base_id + 66, ItemClassification.progression),
    "Parallel Automation": ItemData(oni_base_id + 67, ItemClassification.progression),
    "Advanced Automation": ItemData(oni_base_id + 68, ItemClassification.progression),
    "Computing": ItemData(oni_base_id + 69, ItemClassification.progression),
    "Multiplexing": ItemData(oni_base_id + 70, ItemClassification.progression),
    "Celestial Detection": ItemData(oni_base_id + 71, ItemClassification.progression),
    "Introductory Rocketry": ItemData(oni_base_id + 72, ItemClassification.progression),
    "Solid Fuel Combustion": ItemData(oni_base_id + 73, ItemClassification.progression),
    "Hydrocarbon Combustion": ItemData(oni_base_id + 74, ItemClassification.progression),
    "CryoFuel Combustion": ItemData(oni_base_id + 75, ItemClassification.progression),
    "Solid Cargo": ItemData(oni_base_id + 76, ItemClassification.progression),
    "Liquid and Gas Cargo": ItemData(oni_base_id + 77, ItemClassification.progression),
    "Unique Cargo": ItemData(oni_base_id + 78, ItemClassification.progression)
}


vanilla_care_packages: Dict[str, ItemData] = {
    "500kg Algae": ItemData(oni_base_id + 200),
    "1 Arbor Acorn": ItemData(oni_base_id + 201),
    "2 Blossom Seed": ItemData(oni_base_id + 202),
    "3 Briar Seed": ItemData(oni_base_id + 203),
    "2000kg Brine": ItemData(oni_base_id + 204),
    "3000kg Coal": ItemData(oni_base_id + 205),
    "3kg Curative Tablet": ItemData(oni_base_id + 206),
    "500kg Dirt": ItemData(oni_base_id + 207),
    "3000kg Fertilizer": ItemData(oni_base_id + 208),
    "1 Fungal Spore": ItemData(oni_base_id + 209),
    "1 Hatchling": ItemData(oni_base_id + 210),
    "3 Hatchling Egg": ItemData(oni_base_id + 211),
    "3 Joya Seed": ItemData(oni_base_id + 212),
    "3 Mirth leaf Seed": ItemData(oni_base_id + 213),
    "6kg Muckroot": ItemData(oni_base_id + 214),
    "5kg Nutrient Bar": ItemData(oni_base_id + 215),
    "1 Oxyfern Seed": ItemData(oni_base_id + 216),
    "100kg Oxylite": ItemData(oni_base_id + 217),
    "2 Pip Egg": ItemData(oni_base_id + 218),
    "1 Pipsqueak": ItemData(oni_base_id + 219),
    "1 Pokeshell Spawn": ItemData(oni_base_id + 220),
    "1 Puftlet": ItemData(oni_base_id + 221),
    "3 Puftlet Egg": ItemData(oni_base_id + 222),
    "1000kg Rust": ItemData(oni_base_id + 223),
    "2000kg Salt Water": ItemData(oni_base_id + 224),
    "3000kg Sand": ItemData(oni_base_id + 225),
    "1000kg Sandstone": ItemData(oni_base_id + 226),
    "1 Shine Nymph": ItemData(oni_base_id + 227),
    "3 Shine Nymph Egg": ItemData(oni_base_id + 228),
    "1 Snazzy Suit": ItemData(oni_base_id + 229),
    "2000kg Water": ItemData(oni_base_id + 230),
    "3kg Omelette": ItemData(oni_base_id + 231),
    "3kg Bristle Berry": ItemData(oni_base_id + 232),
    "4000kg Ice": ItemData(oni_base_id + 233),
    "3 Larva Egg": ItemData(oni_base_id + 234),
    "1 Balm Lily Seed": ItemData(oni_base_id + 235),
    "1 Drecklet": ItemData(oni_base_id + 236),
    "3 Drecklet Egg": ItemData(oni_base_id + 237),
    "3kg Fried Mushroom": ItemData(oni_base_id + 238),
    "8 Pacu": ItemData(oni_base_id + 239),
    "1 Pincha Pepper Seed": ItemData(oni_base_id + 240),
    "3 Shove Vole Egg": ItemData(oni_base_id + 241),
    "3 Thimble Reed Seed": ItemData(oni_base_id + 242),
    "1 Wort Seed": ItemData(oni_base_id + 243),
    "3kg Barbeque": ItemData(oni_base_id + 244),
    "1 Slickster Larva": ItemData(oni_base_id + 245),
    "3kg Spicy Tofu": ItemData(oni_base_id + 246),
    "1 Vole Pup": ItemData(oni_base_id + 247),
    "2000kg Copper Ore": ItemData(oni_base_id + 248),
    "2000kg Gold Amalgam": ItemData(oni_base_id + 249),
    "400kg Copper": ItemData(oni_base_id + 250),
    "400kg Iron": ItemData(oni_base_id + 251),
    "100kg Aluminum Ore": ItemData(oni_base_id + 252),
    "100kg Ethanol": ItemData(oni_base_id + 253),
    "200kg Glass": ItemData(oni_base_id + 254),
    "150kg Lime": ItemData(oni_base_id + 255),
    "500kg Plastic": ItemData(oni_base_id + 256),
    "100kg Steel": ItemData(oni_base_id + 257),
}


item_table: Dict[str, ItemData] = {
    **vanilla_research,
    **vanilla_care_packages,
    "Care Package Trap": ItemData(oni_base_id - 1, ItemClassification.trap),
    "Colony Trap": ItemData(oni_base_id - 2, ItemClassification.trap)
}


filler_items: List[str] = list(vanilla_care_packages.keys())
item_name_to_id: Dict[str, int] = { item_name: data.code for item_name, data in item_table.items() }
