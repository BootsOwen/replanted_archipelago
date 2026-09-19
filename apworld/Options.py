from dataclasses import dataclass
from Options import Choice, Range, Toggle, PerGameCommonOptions, DeathLink, OptionCounter, OptionGroup, OptionSet, StartInventoryPool

class AdventureModeProgression(Choice):
    """
    Determines the way in which you will progress through Adventure Mode.
    This setting only affects levels within Adventure Mode and has no impact on the other modes.

    - linear: Adventure Mode levels will be unlocked by clearing the previous level, just like in the vanilla game. Clearing an area will unlock the next one.
    - area_unlock_items: Locks each unique area (Night, Pool, Fog and Roof) of Adventure Mode behind a different item. You can swap between unlocked areas whenever you like, but the levels within each area must be cleared in order. (e.g. You must clear 5-1 before you can play 5-2)
    - open_area_unlock_items: After receiving an area unlock item, all levels within that area are instantly unlocked. (e.g. After unlocking Fog Access, you can instantly play 4-2 without playing 4-1)
    - level_items: You will start with the first five levels unlocked. Other levels are individually unlocked as separate items. If this option is enabled without enabling enough additional locations to place these items in, you will not be able to generate a world.
    """
    display_name = "Adventure Mode Progression"
    option_linear = 0
    option_area_unlock_items = 1
    option_open_area_unlock_items = 2
    option_level_items = 3
    default = 1    

class HugeWaveLocations(Toggle):
    """
    Include locations for defeating Huge Waves prior to each level's Final Wave.
    """
    display_name = "Huge Wave Locations"
    default = True

class WavesanityLocations(Range):
    """
    Include additional locations for small waves.
    This may add a lot of filler items. Make sure to consider any other players in your MultiWorld before increasing this number.

    This number will be automatically increased if there aren't enough locations available to place all of your items.
    This number will be automatically decreased if there aren't enough levels enabled.
    """
    display_name = "Wavesanity Locations"
    range_start = 0
    range_end = 2272
    default = 0    

class ZombieRandomisation(Toggle):
    """
    Randomises the zombie types included in each level.
    """
    display_name = "Zombie Randomisation"
    default = False

class RandomisedZombies(OptionCounter):
    """
    Determines which zombie types will be included in randomisation.
    If zombie_randomisation is set to false, this option will be ignored and no Zombies will be randomised.

    Any Zombie type set to 1 will be included in randomisation and can appear in randomly selected levels.
    Any Zombie type set to 0 will stay in its usual level(s) and will not be randomised to any others.

    *Trash Can Zombie is forced to 0 if goty_compatability_mode is enabled.
    """
    display_name = "Randomised Zombies"
    min = 0
    max = 1
    valid_keys = ["Conehead", "Polevaulter", "Buckethead", "Newspaper", "ScreenDoor", "Football", "Dancer", "Snorkel", "Zomboni", "DolphinRider", "JackInTheBox", "Balloon", "Digger", "Pogo", "Bungee", "Ladder", "Catapult", "Gargantuar", "PeaHead", "WallnutHead", "JalapenoHead", "GatlingHead", "SquashHead", "TallnutHead", "GigaGargantuar", "TrashCan", "Imp"]
    default = {
        "Conehead": 1,
        "Polevaulter": 1,
        "Buckethead": 1,
        "Newspaper": 1,
        "ScreenDoor": 1,
        "Football": 1,
        "Dancer": 1,
        "Snorkel": 1,
        "Zomboni": 1,
        "DolphinRider": 1,
        "JackInTheBox": 1,
        "Balloon": 1,
        "Digger": 1,
        "Pogo": 1,
        "Bungee": 1,
        "Ladder": 1,
        "Catapult": 1,
        "Gargantuar": 1,
        "PeaHead": 0,
        "WallnutHead": 0,
        "JalapenoHead": 0,
        "GatlingHead": 0,
        "SquashHead": 0,
        "TallnutHead": 0,
        "GigaGargantuar": 0,
        "TrashCan": 0,
        "Imp": 0
    }

class ZombieRandomisedModes(OptionCounter):
    """
    Determines which levels will have their zombie types randomised.
    If zombie_randomisation is set to false, this option will be ignored and no zombies will be randomised.

    Any mode set to 1 will feature levels with randomised selection of zombies.
    Any mode set to 0 will contain its usual zombies from the original game.

    *Survival, Cloudy Day, Bonus Levels and China will all be forced to 0 if goty_compatability_mode is enabled.
    """
    display_name = "Zombie Randomised Modes"
    min = 0
    max = 1
    valid_keys = ["Adventure", "Mini-games", "Survival", "Cloudy Day", "Bonus Levels", "China", "Vasebreaker"]
    default = {
        "Adventure": 1,
        "Mini-games": 1,
        "Survival": 1,
        "Cloudy Day": 0,
        "Bonus Levels": 1,
        "China": 0,
        "Vasebreaker": 0
    }

class ConveyorRandomisation(Toggle):
    """
    Randomises the seed packet types present in Conveyor Belt levels.
    """
    display_name = "Conveyor Randomisation"
    default = False

class VasebreakerRandomisation(Toggle):
    """
    Randomises the seed packet types present in Vasebreaker levels.
    """
    display_name = "Vasebreaker Randomisation"
    default = False

class PlantStatRandomisation(Toggle):
    """
    Randomises the stats of each Plant in the game. 
    This affects Sun Cost, Packet Refresh Time, Toughness, Firing Rate and Projectile Damage.
    Plants should remain relatively balanced while still providing variety.

    While this affects the majority of levels in the game, it doesn't affect certain Mini-game and Puzzle levels.
    It only affects Conveyor Belt levels if conveyor_randomisation is set to true.
    It only affects Vasebreaker levels if vasebreaker_randomisation is set to true.
    """
    display_name = "Plant Stat Randomisation"
    default = False  

class MaintainVanillaProjectileStrength(Toggle):
    """
    Prevents Plant Stat Randomisation from affecting the damage of projectiles.
    If this option is enabled, then projectiles will maintain their original damage values.
    This will result in plants that play much more similarly to their standard versions.

    This option only matters if plant_stat_randomisation is set to true.
    If plant_stat_randomisation is set to false then projectiles will provide their usual damage and this option is irrelevant.
    """
    display_name = "Maintain Vanilla Projectile Strength"
    default = False  

class PlantStatRandomisationBlacklist(OptionSet):
    """
    Plants named here will avoid being affected by plant stat randomisation.
    For example, you may add "Sunflower" to ensure that Sunflower uses its default stats.

    This option only matters if plant_stat_randomisation is set to true.
    If plant_stat_randomisation is set to false then no plant stat randomisation will happen.
 
    Valid plant names are: "Peashooter", "Sunflower", "Cherry Bomb", "Wall-nut", "Potato Mine", "Snow Pea", "Chomper", "Repeater", "Puff-shroom", "Sun-shroom", "Fume-shroom", "Grave Buster", "Hypno-shroom", "Scaredy-shroom", "Ice-shroom", "Doom-shroom", "Lily Pad", "Squash", "Threepeater", "Tangle Kelp", "Jalapeno", "Spikeweed", "Torchwood", "Tall-nut", "Sea-shroom", "Plantern", "Cactus", "Blover", "Split Pea", "Starfruit", "Pumpkin", "Magnet-shroom", "Cabbage-pult", "Flower Pot", "Kernel-pult", "Coffee Bean", "Garlic", "Umbrella Leaf", "Marigold", "Melon-pult", "Gatling Pea", "Twin Sunflower", "Gloom-shroom", "Cattail", "Winter Melon", "Gold Magnet", "Spikerock", "Cob Cannon"
    """
    display_name = "Plant Stat Randomisation Blacklist"
    valid_keys = ["Peashooter", "Sunflower", "Cherry Bomb", "Wall-nut", "Potato Mine", "Snow Pea", "Chomper", "Repeater", "Puff-shroom", "Sun-shroom", "Fume-shroom", "Grave Buster", "Hypno-shroom", "Scaredy-shroom", "Ice-shroom", "Doom-shroom", "Lily Pad", "Squash", "Threepeater", "Tangle Kelp", "Jalapeno", "Spikeweed", "Torchwood", "Tall-nut", "Sea-shroom", "Plantern", "Cactus", "Blover", "Split Pea", "Starfruit", "Pumpkin", "Magnet-shroom", "Cabbage-pult", "Flower Pot", "Kernel-pult", "Coffee Bean", "Garlic", "Umbrella Leaf", "Marigold", "Melon-pult", "Gatling Pea", "Twin Sunflower", "Gloom-shroom", "Cattail", "Winter Melon", "Gold Magnet", "Spikerock", "Cob Cannon"]

class MinigameLevels(Choice):
    """
    Determines how Mini-game levels will be incorporated into the game.

    - off: Mini-game levels will not be included.
    - vanilla: After obtaining the "Mini-games" item, the first three Mini-game levels will be available to play. Clearing any Mini-game level will unlock a new one, in order.
    - randomised_order: After obtaining the "Mini-games" item, three random Mini-game levels will be available to play. Clearing any Mini-game level will unlock a new one, in a randomised order.
    - open: After obtaining the "Mini-games" item, you have instant access to all Mini-game levels.
    - level_items: Every individual Mini-game level is a separate item.
    """
    display_name = "Mini-game Levels"
    option_off = 0
    option_vanilla = 1
    option_randomised_order = 2
    option_open = 3
    option_level_items = 4
    default = 2

class PuzzleLevels(Choice):
    """
    Determines how Puzzle levels will be incorporated into the game.

    - off: Puzzle levels will not be included.
    - vanilla: After obtaining the "Puzzle Mode" item, the first Vasebreaker level and the first I, Zombie level will be available to play. Clearing a Puzzle level will unlock the next one in its category, in order.
    - randomised_order: After obtaining the "Puzzle Mode" item, one random Vasebreaker level and one random I, Zombie level will be available to play. Clearing any Puzzle level will unlock the next one in its category, in a randomised order.
    - open: After obtaining the "Puzzle Mode" item, you have instant access to all Puzzle levels.
    - level_items: Every individual Puzzle level is a separate item.
    """
    display_name = "Puzzle Levels"
    option_off = 0
    option_vanilla = 1
    option_randomised_order = 2
    option_open = 3
    option_level_items = 4
    default = 2

class SurvivalLevels(Choice):
    """
    Determines how Survival levels will be incorporated into the game.

    - off: Survival levels will not be included.
    - vanilla: After obtaining the "Survival Mode" item, the first three Survival levels will be available to play. Clearing any Survival level will unlock a new one, in order.
    - randomised_order: After obtaining the "Survival Mode" item, three random Survival levels will be available to play. Clearing any Survival level will unlock a new one, in a randomised order.
    - open: After obtaining the "Survival Mode" item, you have instant access to all Survival levels.
    - level_items: Every individual Survival level is a separate item.
    """
    display_name = "Survival Levels"
    option_off = 0
    option_vanilla = 1
    option_randomised_order = 2
    option_open = 3
    option_level_items = 4
    default = 2

class CloudyDayLevels(Choice):
    """
    Determines how Cloudy Day levels will be incorporated into the game.
    These can be particularly challenging compared to the rest of the game.

    - off: Cloudy Day levels will not be included.
    - vanilla: After obtaining the "Cloudy Day" item, the first Cloudy Day level will be available to play. Clearing a Cloudy Day level will unlock the next one, in order.
    - randomised_order: After obtaining the "Cloudy Day" item, one random Cloudy Day level will be available to play. Clearing a Cloudy Day level will unlock a new one, in a randomised order.
    - open: After obtaining the "Cloudy Day" item, you have instant access to all Cloudy Day levels.
    - level_items: Every individual Cloudy Day level is a separate item.

    *This option is forced to "off" if goty_compatability_mode is enabled.
    """
    display_name = "Cloudy Day Levels"
    option_off = 0
    option_vanilla = 1
    option_randomised_order = 2
    option_open = 3
    option_level_items = 4
    default = 0

class BonusLevels(Choice):
    """
    Determines how Bonus Levels (also known as Limbo Levels) will be incorporated into the game.

    - off: Bonus Levels will not be included.
    - vanilla: After obtaining the "Bonus Levels" item, you have instant access to all Bonus Levels.
    - level_items: Every individual Bonus Level is a separate item.

    *This option is forced to "off" if goty_compatability_mode is enabled.
    """
    display_name = "Bonus Levels"
    option_off = 0
    option_vanilla = 1
    option_level_items = 2
    default = 0

class ChinaLevel(Choice):
    """
    Determines how the China level ("The Great Wall") will be incorporated into the game.

    - off: The China level will not be included.
    - vanilla: The China level will be instantly accessible.
    - item: The China level will be locked behind an item.

    *This option is forced to "off" if goty_compatability_mode is enabled.
    """
    display_name = "China Level"
    option_off = 0
    option_vanilla = 1
    option_item = 2
    default = 0    

class AdventureLevelsGoal(Range):
    """
    Determines how many unique levels of Adventure Mode (if any) must be cleared before you can play the final battle with Dr. Zomboss in Roof: Level 5-10.
    """
    display_name = "Adventure Levels Goal"
    range_start = 0
    range_end = 49
    default = 49

class AdventureAreasGoal(Range):
    """
    Determines how many unique areas of Adventure Mode (if any) must be fully cleared before you can play the final battle with Dr. Zomboss in Roof: Level 5-10.
    """
    display_name = "Adventure Areas Goal"
    range_start = 0
    range_end = 5
    default = 0

class MinigameLevelsGoal(Range):
    """
    Determines how many unique Mini-game levels (if any) must be cleared before you can play the final battle with Dr. Zomboss in Roof: Level 5-10.
    Mini-games must be enabled in order for this setting to have any effect.
    """
    display_name = "Mini-game Levels Goal"
    range_start = 0
    range_end = 20
    default = 0

class PuzzleLevelsGoal(Range):
    """
    Determines how many unique Puzzle levels (if any) must be cleared before you can play the final battle with Dr. Zomboss in Roof: Level 5-10.
    Puzzle Levels must be enabled in order for this setting to have any effect.
    """
    display_name = "Puzzle Levels Goal"
    range_start = 0
    range_end = 18
    default = 0

class SurvivalLevelsGoal(Range):
    """
    Determines how many unique Survival levels (if any) must be cleared before you can play the final battle with Dr. Zomboss in Roof: Level 5-10.
    Survival Levels must be enabled in order for this setting to have any effect.
    """
    display_name = "Survival Levels Goal"
    range_start = 0
    range_end = 10
    default = 0

class CloudyDayLevelsGoal(Range):
    """
    Determines how many unique Cloudy Day levels (if any) must be cleared before you can play the final battle with Dr. Zomboss in Roof: Level 5-10.
    Cloudy Day Levels must be enabled in order for this setting to have any effect.

    *This option is forced to 0 if goty_compatability_mode is enabled.
    """
    display_name = "Cloudy Day Levels Goal"
    range_start = 0
    range_end = 12
    default = 0

class BonusLevelsGoal(Range):
    """
    Determines how many unique Bonus Levels (if any) must be cleared before you can play the final battle with Dr. Zomboss in Roof: Level 5-10.
    Bonus Levels must be enabled in order for this setting to have any effect.

    *This option is forced to 0 if goty_compatability_mode is enabled.
    """
    display_name = "Bonus Levels Goal"
    range_start = 0
    range_end = 10
    default = 0

class TotalLevelsGoal(Range):
    """
    Determines how many unique levels (if any) must be cleared across all modes combined before you can play the final battle with Dr. Zomboss in Roof: Level 5-10.
    If this option is assigned a number higher than the number of available levels then it will be automatically reduced.

    *This option is limited to 97 if goty_compatability_mode is enabled.
    """
    display_name = "Total Levels Goal"
    range_start = 0
    range_end = 120
    default = 0

class TacoHuntItems(Range):
    """
    Determines the total number of Taco items to be included in the item pool.
    """
    display_name = "Taco Hunt Items"
    range_start = 0
    range_end = 30
    default = 0

class TacoHuntPercentage(Range):
    """
    Determines what percentage of Taco items must be obtained before you can play the final battle with Dr. Zomboss in Roof: Level 5-10.

    *This option requires that taco_hunt_items be set to a number higher than 0.
    """
    display_name = "Taco Hunt Percentage"
    range_start = 1
    range_end = 100
    default = 100

class FastGoal(Toggle):
    """
    If this option is enabled, you can instantly fight Dr. Zomboss in Roof: Level 5-10 as soon as your custom goal requirements are met.
    If this option is disabled, your custom goal requirements will be needed in addition to how your chosen adventure_mode_progression setting would typically lead to 5-10. (i.e. "linear" requires 5-9 to be completed; "area_unlock_items" requires Roof Access and 5-9 to be completed; "open_area_unlock_items" requires Roof Access)

    This option is forced on if adventure_mode_progression is set to "level_items".
    If you are playing with adventure_mode_progression set to "level_items", make sure you set at least one goal.
    If you have adventure_mode_progression set to "level_items" with all goals set to 0, you will be able to complete the game immediately!
    """
    display_name = "Fast Goal"
    default = False

class ShopBehaviour(Choice):
    """
    Determines how access is granted to Crazy Dave's shop.

    - off: Crazy Dave's shop will not be included.
    - normal: Finding the "Crazy Dave's Car Key" item will grant access to Crazy Dave's shop. "Twiddydinkies Restock" items will unlock new pages.
    - progressive: The first "Progressive Twiddydinkies" item you find will grant access to Crazy Dave's shop. Additional "Progressive Twiddydinkies" items will unlock new pages.
    """
    display_name = "Shop Behaviour"
    option_off = 0
    option_normal = 1
    option_progressive = 2
    default = 1

class ShopItems(Range):
    """
    How many items to include in Crazy Dave's shop.

    Each page contains eight items.
    A value of 96 has twelve pages.
    """
    display_name = "Shop Items"
    range_start = 1
    range_end = 96
    default = 16

class StartingPlants(Range):
    """
    How many unique plants to begin the game with.
    """
    display_name = "Starting Plants"
    range_start = 1
    range_end = 49
    default = 1    

class StartingSeedSlots(Range):
    """
    How many seed slots to begin the game with.
    You will be able to unlock additional seed slots as items.
    """
    display_name = "Starting Seed Slots"
    range_start = 1
    range_end = 10
    default = 6

class EarlySunflower(Toggle):
    """
    Attempts to place Sunflower, Sun-shroom and Coffee Bean in the first sphere, making for a more beginner-friendly game.
    """
    display_name = "Early Sunflower"
    default = False

class EarlyShovel(Toggle):
    """
    Attempts to place the Shovel in the first sphere.
    """
    display_name = "Early Shovel"
    default = False    

class EarlyZenGarden(Toggle):
    """
    Attempts to place Zen Garden in the first sphere.
    """
    display_name = "Early Zen Garden"
    default = False

class ZenGardenItems(Toggle):
    """
    Determines whether to include Zen Garden items.

    Enabling Zen Garden items adds the following useful items to your game: Zen Garden, Phonograph, Gardening Glove, Wheelbarrow, Stinky and Gold Watering Can.
    It also adds the following filler items: Fertilizer, Bug Spray, Chocolate and Tree Food.
    Fertilizer, Bug Spray and Tree Food will be infinitely repurchaseable in Crazy Dave's shop.
    
    There are no AP locations related to Zen Garden, but growing your Tree of Wisdom can provide item hints.
    """
    display_name = "Zen Garden Items"
    default = True

class ShuffleButterAbility(Toggle):
    """
    Adds a useful "Butter Ability" item to the game.
    This item permanently grants you the power to butter any zombie of your choice. A cooldown applies after each use.

    *This option is forced to "false" if goty_compatability_mode is enabled.
    """
    display_name = "Shuffle Butter Ability"
    default = False

class RakeFiller(Toggle):
    """
    Determines whether to include "Rake" filler items.
    This item places a rake on the lawn, taking out the first zombie that steps on it.
    """
    display_name = "Rake Filler"
    default = False

class RandomSeedFiller(Toggle):
    """
    Determines whether to include "Random Seed Packet" filler items.
    This item drops a random seed packet onto the lawn which can be freely picked up and planted, just like the ones you see in Vasebreaker.
    """
    display_name = "Random Seed Packet Filler"
    default = False

class ZombieFreezeFiller(Toggle):
    """
    Determines whether to include "Instant Zombie Freeze" filler items.
    This item instantly freezes all zombies on the lawn.
    """
    display_name = "Zombie Freeze Filler"
    default = False

class ZombieHypnosisFiller(Toggle):
    """
    Determines whether to include "Instant Zombie Hypnosis" filler items.
    This item instantly hypnotises all zombies on the lawn.
    """
    display_name = "Zombie Hypnosis Filler"
    default = False    

class SunBurstFiller(Toggle):
    """
    Determines whether to include "Sun Burst" filler items.
    This item causes a burst of 75-150 sun to appear.
    """
    display_name = "Sun Burst Filler"
    default = False

class EasyUpgradePlants(Toggle):
    """
    Allows you to place upgrade plants without requiring their base form.
    For example, Gatling Pea could be placed straight onto the lawn without requiring a Repeater first.
    Enabling this option increases the Sun prices of upgrade plants accordingly.
    """
    display_name = "Easy Upgrade Plants"
    default = False

class LockConveyorPlants(Toggle):
    """
    If this option is enabled, then conveyor levels will be unable to serve you plants that you haven't yet unlocked.
    """
    display_name = "Lock Conveyor Plants"
    default = False

class LockVasebreakerPlants(Toggle):
    """
    If this option is enabled, then Vasebreaker will be unable to serve you plants that you haven't yet unlocked.
    """
    display_name = "Lock Vasebreaker Plants"
    default = False    

class LockIZombieZombies(Toggle):
    """
    If this option is enabled, each zombie type in "I, Zombie" will be locked behind individual unlock items.
    """
    display_name = "Lock I, Zombie Zombies"
    default = False

class ImitaterBehaviour(Choice):
    """
    Determines which seeds can be copied by Imitater.

    - normal: Imitater can copy the seeds of plants you have already unlocked.
    - open: Imitater can copy any seed in the game - even the seeds of plants you haven't unlocked yet.
    """
    display_name = "Imitater Behaviour"
    option_normal = 0
    option_open = 1
    default = 0

class StartingSunUpgrades(Choice):
    """
    Adds "Additional Starting Sun" items to the item pool.
    Obtaining an "Additional Starting Sun" item increases the amount of sun you will start a level with.
    
    - off: No "Additional Starting Sun" items will be generated.
    - 5_sun_each: Each "Additional Starting Sun" item you obtain will give you 5 additional sun at the beginning of each level.
    - 25_sun_each: Each "Additional Starting Sun" item you obtain will give you 25 additional sun at the beginning of each level.
    - 50_sun_each: Each "Additional Starting Sun" item you obtain will give you 50 additional sun at the beginning of each level.
    """
    display_name = "Starting Sun Upgrades"
    option_off = 0
    option_5_sun_each = 1
    option_25_sun_each = 2
    option_50_sun_each = 3
    default = 0

class MaximumSunUpgrades(Range):
    """
    Determines the maximum amount of additional sun that "Additional Starting Sun" items can provide.
    Increasing this number results in more "Additional Starting Sun" items being generated.    
    """
    display_name = "Maximum Sun Upgrades"
    range_start = 50
    range_end = 150
    default = 50

class MowerRewardUpgrades(Range):
    """
    Determines the number of "Mower Reward Upgrade" items to include in the item pool.
    Obtaining an "Mower Reward Upgrade" item increases the number of Gold Coins you receive for each remaining Lawn Mower at the end of a level.
    """
    display_name = "Mower Reward Upgrades"
    range_start = 0
    range_end = 5
    default = 0

class ProgressiveLootRateItems(Range):
    """
    Determines the number of "Progressive Loot Rate" items to include in the item pool.
    Each "Progressive Loot Rate" item adds a +10% chance for zombies to drop loot.
    """
    display_name = "Progressive Loot Rate Items"
    range_start = 0
    range_end = 10
    default = 0    

class MusicShuffle(Choice):
    """
    Randomises the music played during levels.
    """
    display_name = "Music Shuffle"
    option_disabled = 0
    option_by_type = 1
    option_by_level = 2
    default = 0

class DisableStormFlashes(Toggle):
    """
    Disables the storm flashes in "Fog: Level 4-10" and "Bonus Levels: Dark Stormy Night".
    """
    display_name = "Disable Storm Flashes"
    default = False

class TrapPercentage(Range):
    """
    Determines the percentage of filler items that will be replaced with trap items.
    """
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 0   

class MowerDeployTrapWeight(Range):
    """
    This trap instantly activates all lawn mowers on the lawn.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "Mower Deploy Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class SeedPacketCooldownTrapWeight(Range):
    """
    This trap instantly puts all seed packets on cooldown.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "Seed Packet Cooldown Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class ZombieAmbushTrapWeight(Range):
    """
    This trap instantly causes an ambush of zombies.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "Zombie Ambush Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class ZombieShuffleTrapWeight(Range):
    """
    This trap causes zombies to change lanes.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "Zombie Shuffle Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class ZombieCaffeineTrapWeight(Range):
    """
    This trap gives a speed boost to all zombies on the lawn.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "Zombie Caffeine Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class RVTrapWeight(Range):
    """
    This trap causes an RV to be thrown at your lawn, crushing some of your plants.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "RV Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class CraterTrapWeight(Range):
    """
    This trap adds three random craters to your lawn.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "Crater Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class LawnFlipTrapWeight(Range):
    """
    This trap flips your lawn - whatever was at the back, is now at the front, and vice versa.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "Lawn Flip Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class LawnRandomiserTrapWeight(Range):
    """
    This trap randomises your lawn - every active plant is transformed into a completely random one. If you're lucky, this could turn out to be a positive thing!
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "Lawn Randomiser Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class InvisighoulTrapWeight(Range):
    """
    This trap causes all zombies on the lawn to turn invisible.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "Invisighoul Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class SeedBankRandomiserTrapWeight(Range):
    """
    This trap randomises the plants available in your seed bank.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "Seed Bank Randomiser Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class ParanoiaTrapWeight(Range):
    """
    This trap plays the music associated with the Jack-in-the-Box zombie.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "Paranoia Trap Weight"
    range_start = 0
    range_end = 100
    default = 50

class LadderTrapWeight(Range):
    """
    This trap places a ladder on every plant on the lawn.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.
    """
    display_name = "Ladder Trap Weight"
    range_start = 0
    range_end = 100
    default = 50    

class ZombieGrowthSerumTrapWeight(Range):
    """
    This trap causes zombies to grow, increasing their toughness.
    A higher number means that you are more likely to see the given trap. A value of 0 means the trap will not appear.

    *This option is forced to 0 if goty_compatability_mode is enabled.
    """
    display_name = "Zombie Growth Serum Trap Weight"
    range_start = 0
    range_end = 100
    default = 50    

class CostumeChances(OptionCounter):
    """
    Determines the odds out of 10000 that an easter egg costume is used whenever a plant or zombie appears.
    Retro Peashooter is exclusive to pre-ordered versions of the game.
    Zombies will always use their Chinese variants when playing on The Great Wall.
    Due to limitations in the game, you may see the wrong heads and arms pop off defeated zombies when using this feature.

    *These are all set to 0 if goty_compatability_mode is enabled.
    """
    display_name = "Costume Chances"
    min = 0
    max = 10000
    valid_keys = ["Peashooter (Retro)", "Peashooter (Winter)", "Wall-nut (Winter)", "Cabbage-pult (PvZ2)", "Flower Pot (China)", "Zombie (China)", "Zombie (Retro)", "Zombie (Winter)", "Flag (China)", "Conehead (China)", "Conehead (Headcrab)", "Conehead (Winter)", "Buckethead (China)", "Polevaulter (China)", "Football (China)", "Bungee (China)", "Backup Dancer (Original)"]
    default = {
        "Peashooter (Retro)": 0,
        "Peashooter (Winter)": 0,
        "Wall-nut (Winter)": 0,
        "Cabbage-pult (PvZ2)": 65,
        "Flower Pot (China)": 0,
        "Zombie (China)": 0,
        "Zombie (Retro)": 0,
        "Zombie (Winter)": 0,
        "Flag (China)": 0, 
        "Conehead (China)": 0,
        "Conehead (Headcrab)": 0, 
        "Conehead (Winter)": 0, 
        "Buckethead (China)": 0, 
        "Polevaulter (China)": 0, 
        "Football (China)": 0, 
        "Bungee (China)": 0,
        "Backup Dancer (Original)": 300
    }
    
class GotyCompatabilityMode(Toggle):
    """
    This APWorld is primarily designed to be used with Plants vs. Zombies: Replanted.
    All features and options within this YAML are fully supported by Plants vs. Zombies: Replanted.

    If you wish to connect to this world using Victor Tran's GOTY client, you can - but there are certain limitations.
    The GOTY client is not 100% compatible with all options, and may not be up to date with the latest APWorld version.
    It's recommended you double check the latest APWorld version supported by the GOTY client before generating a game.
    Enabling this option will automatically disable any features exclusive to Plants vs. Zombies: Replanted.
    """
    display_name = "GOTY Compatability Mode"
    default = False

class EnergyLink(Toggle):
    """
    Adds an "Energy Link" button, allowing you to deposit and withdraw money via Energy Link.
    """
    display_name = "Energy Link"
    default = False

class RingLink(Toggle):
    """
    Enables Ring Link for Sun.
    """
    display_name = "Ring Link"
    default = False

class SeedLink(Toggle):
    """
    All Plants vs. Zombies players in your MultiWorld that have enabled Seed Link will be able to trigger each other's matching seed packet cooldowns when placing a plant.
    """
    display_name = "Seed Link"
    default = False    

class LawnLink(Toggle):
    """
    All Plants vs. Zombies players in your MultiWorld that have enabled Lawn Link will be able to interact with each other's lawns.
    """
    display_name = "Lawn Link"
    default = False    

class LawnLinkChances(OptionCounter):
    """
    Determines the likelihoods of Lawn Link effects as percentages out of 100.

    - add_plant: The percentage chance that a plant placed by another player will appear on your lawn, if that tile is free.
    - overwrite_plant: The percentage chance that a plant placed by another player will appear on your lawn, if that tile is not free. This results in the plant that was there being replaced.
    - remove_plant: The percentage chance that a plant lost by another player will result in the loss of a plant on your lawn, if a plant exists on your lawn in the same tile.

    This setting requires Lawn Link to be enabled.
    """
    display_name = "Lawn Link Chances"
    min = 0
    max = 100
    valid_keys = ["add_plant", "overwrite_plant", "remove_plant"]
    default = {
        "add_plant": 15,
        "overwrite_plant": 5,
        "remove_plant": 15
    }

class ZombieWeightRandomisation(Choice):
    """
    Randomises the spawning weights for each zombie type. This affects how zombies are chosen to spawn in each level.
    As an extreme example, this could result in more Gargantuars spawning in a level than standard zombies.
    As such, this option is only recommended for somewhat experienced players.

    - off: Zombies will be spawned using their usual ratios.
    - randomise_once: One randomised set of weights will be generated and used across every level.
    - randomise_per_level: A different set of randomised weights will be generated for each level.
    """
    display_name = "Zombie Weight Randomisation"
    option_off = 0
    option_randomise_once = 1
    option_randomise_per_level = 2    
    default = 0

class ProgressiveSunCapacityItems(Toggle):
    """
    Restricts the amount of sun that can be held at once until enough "Progressive Sun Capacity" items are collected. 
    You will begin the game with the ability to hold a maximum of 150 sun at a time.
    Each "Progressive Sun Capacity" item you obtain doubles your current maximum.
    """
    display_name = "Progressive Sun Capacity Items"
    default = False

class IndividualTileUnlockItems(Choice):
    """
    Locks planting on each individual lawn tile behind receiving a corresponding item.
    You will start the game with a random assortment of tiles unlocked.

    This can make the game much more difficult, especially when combined with other forms of randomisation.
    You may be expected to exploit lawn mowers and zombie spawning patterns in order to progress.

    - off: Tiles will not be locked behind items.
    - light: You will start with 5-6 tiles per row. All other tiles must be unlocked.
    - maximum: You will start with 1-2 tiles per row. All other tiles must be unlocked.
    """
    display_name = "Individual Tile Unlock Items"
    option_off = 0
    option_light = 1
    option_maximum = 2
    default = 0

class HarderZombieSpawns(Toggle):
    """
    Makes various changes to the way zombies spawn in order to increase game difficulty.
    This includes reducing the initial grace period before zombies can spawn, as well as increasing the size and strength of waves.
    This affects all applicable levels in the game and is recommended for experienced players only.

    If you regret enabling this setting, you can toggle it via the title screen's "Options" menu.
    """
    display_name = "Harder Zombie Spawns"
    default = False

class RandomlyBannedPlantsPerLevel(Range):
    """
    Selects the given number of plants at random to be banned from each level.
    This may force you to spice up your strategy or unlock alternative plants in order to progress.
    """
    display_name = "Randomly Banned Plants Per Level"
    range_start = 0
    range_end = 30
    default = 0    

@dataclass
class PVZROptions(PerGameCommonOptions):
    goty_compatability_mode: GotyCompatabilityMode 
    death_link: DeathLink
    ring_link: RingLink
    energy_link: EnergyLink
    seed_link: SeedLink
    lawn_link: LawnLink
    lawn_link_chances: LawnLinkChances
    adventure_mode_progression: AdventureModeProgression
    minigame_levels: MinigameLevels
    puzzle_levels: PuzzleLevels
    survival_levels: SurvivalLevels
    cloudy_day_levels: CloudyDayLevels
    bonus_levels: BonusLevels
    china_level: ChinaLevel
    huge_wave_locations: HugeWaveLocations
    wavesanity_locations: WavesanityLocations
    shop_behaviour: ShopBehaviour
    shop_items: ShopItems
    adventure_levels_goal: AdventureLevelsGoal
    adventure_areas_goal: AdventureAreasGoal
    minigame_levels_goal: MinigameLevelsGoal
    puzzle_levels_goal: PuzzleLevelsGoal
    survival_levels_goal: SurvivalLevelsGoal
    cloudy_day_levels_goal: CloudyDayLevelsGoal
    bonus_levels_goal: BonusLevelsGoal
    total_levels_goal: TotalLevelsGoal
    taco_hunt_items: TacoHuntItems
    taco_hunt_percentage: TacoHuntPercentage
    fast_goal: FastGoal
    conveyor_randomisation: ConveyorRandomisation
    vasebreaker_randomisation: VasebreakerRandomisation
    zombie_randomisation: ZombieRandomisation
    randomised_zombies: RandomisedZombies
    zombie_randomised_modes: ZombieRandomisedModes
    zombie_weight_randomisation: ZombieWeightRandomisation
    plant_stat_randomisation: PlantStatRandomisation
    maintain_vanilla_projectile_strength: MaintainVanillaProjectileStrength
    plant_stat_randomisation_blacklist: PlantStatRandomisationBlacklist
    lock_conveyor_plants: LockConveyorPlants
    lock_vasebreaker_plants: LockVasebreakerPlants
    lock_izombie_zombies: LockIZombieZombies
    easy_upgrade_plants: EasyUpgradePlants
    randomly_banned_plants_per_level: RandomlyBannedPlantsPerLevel
    harder_zombie_spawns: HarderZombieSpawns
    imitater_behaviour: ImitaterBehaviour
    disable_storm_flashes: DisableStormFlashes
    music_shuffle: MusicShuffle
    costume_chances: CostumeChances
    zen_garden_items: ZenGardenItems
    starting_sun_upgrades: StartingSunUpgrades
    maximum_sun_upgrades: MaximumSunUpgrades
    mower_reward_upgrades: MowerRewardUpgrades
    shuffle_butter_ability: ShuffleButterAbility
    random_seed_filler: RandomSeedFiller
    zombie_freeze_filler: ZombieFreezeFiller
    zombie_hypnosis_filler: ZombieHypnosisFiller
    sun_burst_filler: SunBurstFiller
    rake_filler: RakeFiller
    starting_plants: StartingPlants
    starting_seed_slots: StartingSeedSlots
    early_sunflower: EarlySunflower
    early_shovel: EarlyShovel
    early_zen_garden: EarlyZenGarden
    progressive_sun_capacity_items: ProgressiveSunCapacityItems
    individual_tile_unlock_items: IndividualTileUnlockItems
    trap_percentage: TrapPercentage
    mower_deploy_trap_weight: MowerDeployTrapWeight
    seed_packet_cooldown_trap_weight: SeedPacketCooldownTrapWeight
    zombie_ambush_trap_weight: ZombieAmbushTrapWeight
    zombie_shuffle_trap_weight: ZombieShuffleTrapWeight
    zombie_caffeine_trap_weight: ZombieCaffeineTrapWeight
    zombie_growth_serum_trap_weight: ZombieGrowthSerumTrapWeight
    invisighoul_trap_weight: InvisighoulTrapWeight
    rv_trap_weight: RVTrapWeight
    crater_trap_weight: CraterTrapWeight
    ladder_trap_weight: LadderTrapWeight
    lawn_flip_trap_weight: LawnFlipTrapWeight
    lawn_randomiser_trap_weight: LawnRandomiserTrapWeight
    seed_bank_randomiser_trap_weight: SeedBankRandomiserTrapWeight
    paranoia_trap_weight: ParanoiaTrapWeight
    start_inventory_from_pool: StartInventoryPool

OPTION_GROUPS = [
    OptionGroup("AP Settings", [GotyCompatabilityMode, DeathLink, RingLink, EnergyLink, SeedLink, LawnLink, LawnLinkChances]),
    OptionGroup("Level Access", [AdventureModeProgression, MinigameLevels, PuzzleLevels, SurvivalLevels, CloudyDayLevels, BonusLevels, ChinaLevel]),    
    OptionGroup("Extra Locations", [HugeWaveLocations, WavesanityLocations, ShopBehaviour, ShopItems]),
    OptionGroup("Goal", [AdventureLevelsGoal, AdventureAreasGoal, MinigameLevelsGoal, PuzzleLevelsGoal, SurvivalLevelsGoal, CloudyDayLevelsGoal, BonusLevelsGoal, TotalLevelsGoal, TacoHuntItems, TacoHuntPercentage, FastGoal]),
    OptionGroup("Zombie & Plant Randomisation", [ConveyorRandomisation, VasebreakerRandomisation, ZombieRandomisation, RandomisedZombies, ZombieRandomisedModes, ZombieWeightRandomisation, PlantStatRandomisation, MaintainVanillaProjectileStrength, PlantStatRandomisationBlacklist]),
    OptionGroup("Game Tweaks", [LockConveyorPlants, LockVasebreakerPlants, LockIZombieZombies, EasyUpgradePlants, ImitaterBehaviour, RandomlyBannedPlantsPerLevel, HarderZombieSpawns, DisableStormFlashes, MusicShuffle, CostumeChances]),
    OptionGroup("Item Generation", [ZenGardenItems, StartingSunUpgrades, MaximumSunUpgrades, MowerRewardUpgrades, ShuffleButterAbility, RandomSeedFiller, ZombieFreezeFiller, ZombieHypnosisFiller, SunBurstFiller, RakeFiller, StartingPlants, StartingSeedSlots, EarlySunflower, EarlyShovel, EarlyZenGarden, ProgressiveSunCapacityItems, IndividualTileUnlockItems]),
    OptionGroup("Traps", [TrapPercentage, MowerDeployTrapWeight, SeedPacketCooldownTrapWeight, ZombieAmbushTrapWeight, ZombieShuffleTrapWeight, ZombieCaffeineTrapWeight, ZombieGrowthSerumTrapWeight, InvisighoulTrapWeight, RVTrapWeight, CraterTrapWeight, LawnFlipTrapWeight, LawnRandomiserTrapWeight, SeedBankRandomiserTrapWeight, ParanoiaTrapWeight, LadderTrapWeight]),
]