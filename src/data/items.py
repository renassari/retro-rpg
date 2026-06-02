"""Item, magic spell, and level-up icon definitions."""

ITEM_NAMES = ["small Mana potion", "small Health potion", "Chug Chug"]
QUEST_ITEM_NAMES = ["Key Shard", "Castle Key"]

INITIAL_INVENTORY = {
    "small Mana potion": 5,
    "small Health potion": 5,
    "Chug Chug": 1,
}

ITEM_TEXTURE_PATHS = {
    "small Mana potion": "assets/images/items/SmallManaPotion.png",
    "small Health potion": "assets/images/items/SmallHealPotion.png",
    "Chug Chug": "assets/images/items/mix.png",
    "Key Share": "assets/images/items/mix.png",
    "castle key": "assets/images/items/mix.png",
}


MAGIC_NAMES = ["Fire Spell", "Ice Spell", "Rakukaja", "Copper", "Nature Spell"]

MAGIC_BP_COST = {
    "Fire Spell": 3,
    "Ice Spell": 6,
    "Rakukaja": 4,
    "Copper": 5,
    "Nature Spell": 7,
}

MAGIC_TEXTURE_PATHS = {
    "Fire Spell": "assets/images/level_up_symbols/Fire.png",
    "Ice Spell": "assets/images/level_up_symbols/Ice.png",
    "Rakukaja": "assets/images/level_up_symbols/Fire.png",
    "Copper": "assets/images/level_up_symbols/copper.png",
    "Nature Spell": "assets/images/level_up_symbols/heart.png",
}


LEVEL_UP_OPTIONS = ["Health points", "Mana"]

LEVEL_UP_TEXTURE_PATHS = {
    "Health points": "assets/images/level_up_symbols/heart.png",
    "Mana": "assets/images/level_up_symbols/ManaSymbol.png",
}


BATTLE_MENU = ["Punch", "Magic", "Item", "Escape"]
