using HarmonyLib;
using Il2CppReloaded.Data;
using Il2CppReloaded.Gameplay;
using System;
using System.Collections.Generic;
using System.Linq;

namespace ReplantedArchipelago.Patches
{
    public class PlantStatRando
    {
        public class PlantStats
        {
            public int Cost { get; set; }
            public int Refresh { get; set; }
            public int Rate { get; set; }
            public int Health { get; set; }
            public List<string> Projectiles { get; set; }
            public int EasyUpgradeCost { get; set; }
            public string StatsString { get; set; }
            public string ConveyorStatsString { get; set; }
            public PlantStats OldStats { get; private set; }
            public void BackupStats() //Save old stats to restore during I, Zombie etc.
            {
                if (OldStats == null)
                {
                    OldStats = new PlantStats();
                    OldStats.Cost = this.Cost;
                    OldStats.Refresh = this.Refresh;
                    OldStats.Rate = this.Rate;
                    OldStats.Health = this.Health;
                    if (Projectiles != null)
                    {
                        OldStats.Projectiles = new List<string>(Projectiles);
                    }
                    OldStats.EasyUpgradeCost = this.EasyUpgradeCost;
                }
            }
        }

        public static Dictionary<SeedType, PlantStats> plantStats = new Dictionary<SeedType, PlantStats>
        {
            [SeedType.Peashooter] = new PlantStats { Cost = 100, Refresh = 750, Rate = 150, Health = 300, Projectiles = new List<string> { "Pea" } },
            [SeedType.Sunflower] = new PlantStats { Cost = 50, Refresh = 750, Rate = 2500, Health = 300 },
            [SeedType.Cherrybomb] = new PlantStats { Cost = 150, Refresh = 5000, Health = 300 },
            [SeedType.Wallnut] = new PlantStats { Cost = 50, Refresh = 3000, Health = 4000 },
            [SeedType.Potatomine] = new PlantStats { Cost = 25, Refresh = 3000, Health = 300 },
            [SeedType.Snowpea] = new PlantStats { Cost = 175, Refresh = 750, Rate = 150, Health = 300, Projectiles = new List<string> { "Frozen Pea" } },
            [SeedType.Chomper] = new PlantStats { Cost = 150, Refresh = 750, Health = 300 },
            [SeedType.Repeater] = new PlantStats { Cost = 200, Refresh = 750, Rate = 150, Health = 300, Projectiles = new List<string> { "Pea" } },
            [SeedType.Puffshroom] = new PlantStats { Cost = 0, Refresh = 750, Rate = 150, Health = 300, Projectiles = new List<string> { "Spore" } },
            [SeedType.Sunshroom] = new PlantStats { Cost = 25, Refresh = 750, Rate = 2500, Health = 300 },
            [SeedType.Fumeshroom] = new PlantStats { Cost = 75, Refresh = 750, Rate = 150, Health = 300 },
            [SeedType.Gravebuster] = new PlantStats { Cost = 75, Refresh = 750, Health = 300 },
            [SeedType.Hypnoshroom] = new PlantStats { Cost = 75, Refresh = 3000, Health = 300 },
            [SeedType.Scaredyshroom] = new PlantStats { Cost = 25, Refresh = 750, Rate = 150, Health = 300, Projectiles = new List<string> { "Spore" } },
            [SeedType.Iceshroom] = new PlantStats { Cost = 75, Refresh = 5000, Health = 300 },
            [SeedType.Doomshroom] = new PlantStats { Cost = 125, Refresh = 5000, Health = 300 },
            [SeedType.Lilypad] = new PlantStats { Cost = 25, Refresh = 750, Health = 300 },
            [SeedType.Squash] = new PlantStats { Cost = 50, Refresh = 3000, Health = 300 },
            [SeedType.Threepeater] = new PlantStats { Cost = 325, Refresh = 750, Rate = 150, Health = 300, Projectiles = new List<string> { "Pea" } },
            [SeedType.Tanglekelp] = new PlantStats { Cost = 25, Refresh = 3000, Health = 300 },
            [SeedType.Jalapeno] = new PlantStats { Cost = 125, Refresh = 5000, Health = 300 },
            [SeedType.Spikeweed] = new PlantStats { Cost = 100, Refresh = 750 },
            [SeedType.Torchwood] = new PlantStats { Cost = 175, Refresh = 750, Health = 300 },
            [SeedType.Tallnut] = new PlantStats { Cost = 125, Refresh = 3000, Health = 8000 },
            [SeedType.Seashroom] = new PlantStats { Cost = 0, Refresh = 3000, Rate = 150, Health = 300, Projectiles = new List<string> { "Spore" } },
            [SeedType.Plantern] = new PlantStats { Cost = 25, Refresh = 3000, Health = 300 },
            [SeedType.Cactus] = new PlantStats { Cost = 125, Refresh = 750, Rate = 150, Health = 300, Projectiles = new List<string> { "Spike" } },
            [SeedType.Blover] = new PlantStats { Cost = 100, Refresh = 750, Health = 300 },
            [SeedType.Splitpea] = new PlantStats { Cost = 125, Refresh = 750, Rate = 150, Health = 300, Projectiles = new List<string> { "Pea" } },
            [SeedType.Starfruit] = new PlantStats { Cost = 125, Refresh = 750, Rate = 150, Health = 300, Projectiles = new List<string> { "Star" } },
            [SeedType.Pumpkinshell] = new PlantStats { Cost = 125, Refresh = 3000, Health = 4000 },
            [SeedType.Magnetshroom] = new PlantStats { Cost = 100, Refresh = 750, Health = 300 },
            [SeedType.Cabbagepult] = new PlantStats { Cost = 100, Refresh = 750, Rate = 300, Health = 300, Projectiles = new List<string> { "Cabbage" } },
            [SeedType.Flowerpot] = new PlantStats { Cost = 25, Refresh = 750, Health = 300 },
            [SeedType.Kernelpult] = new PlantStats { Cost = 100, Refresh = 750, Rate = 300, Health = 300, Projectiles = new List<string> { "Kernel", "Butter" } },
            [SeedType.InstantCoffee] = new PlantStats { Cost = 75, Refresh = 750, Health = 300 },
            [SeedType.Garlic] = new PlantStats { Cost = 50, Refresh = 750, Health = 400 },
            [SeedType.Umbrella] = new PlantStats { Cost = 100, Refresh = 750, Health = 300 },
            [SeedType.Marigold] = new PlantStats { Cost = 50, Refresh = 3000, Rate = 2500, Health = 300 },
            [SeedType.Melonpult] = new PlantStats { Cost = 300, Refresh = 750, Rate = 300, Health = 300, Projectiles = new List<string> { "Melon" } },
            [SeedType.Gatlingpea] = new PlantStats { Cost = 250, Refresh = 5000, Rate = 150, Health = 300, Projectiles = new List<string> { "Pea" }, EasyUpgradeCost = 450 },
            [SeedType.Twinsunflower] = new PlantStats { Cost = 150, Refresh = 5000, Rate = 2500, Health = 300, EasyUpgradeCost = 200 },
            [SeedType.Gloomshroom] = new PlantStats { Cost = 150, Refresh = 5000, Rate = 200, Health = 300, EasyUpgradeCost = 225 },
            [SeedType.Cattail] = new PlantStats { Cost = 225, Refresh = 5000, Rate = 150, Health = 300, Projectiles = new List<string> { "Spike" }, EasyUpgradeCost = 250 },
            [SeedType.Wintermelon] = new PlantStats { Cost = 200, Refresh = 5000, Rate = 300, Health = 300, Projectiles = new List<string> { "Frozen Melon" }, EasyUpgradeCost = 500 },
            [SeedType.GoldMagnet] = new PlantStats { Cost = 50, Refresh = 5000, Health = 300, EasyUpgradeCost = 150 },
            [SeedType.Spikerock] = new PlantStats { Cost = 125, Refresh = 5000, EasyUpgradeCost = 225 },
            [SeedType.Cobcannon] = new PlantStats { Cost = 500, Refresh = 5000, Health = 300, EasyUpgradeCost = 700 }
        };

        public static Dictionary<ProjectileType, int> defaultProjectileDamages = new Dictionary<ProjectileType, int>
        {
            [ProjectileType.Pea] = 20,
            [ProjectileType.Snowpea] = 20,
            [ProjectileType.Cabbage] = 40,
            [ProjectileType.Melon] = 80,
            [ProjectileType.Puff] = 20,
            [ProjectileType.Wintermelon] = 80,
            [ProjectileType.Star] = 20,
            [ProjectileType.Spike] = 20,
            [ProjectileType.Kernel] = 20,
            [ProjectileType.Butter] = 40,
            [ProjectileType.Fireball] = 40,
            [ProjectileType.PeashooterPea] = 20,
            [ProjectileType.PeashooterFireball] = 40
        };

        public static void ResetPlantStats()
        {
            var plantDefinitions = UnityEngine.Resources.FindObjectsOfTypeAll<PlantDefinition>();
            foreach (PlantDefinition plantDefinition in plantDefinitions)
            {
                if (plantStats.ContainsKey(plantDefinition.m_seedType))
                {
                    PlantStats theStats = plantStats[plantDefinition.m_seedType].OldStats;
                    plantDefinition.m_launchRate = theStats.Rate;
                    plantDefinition.m_seedCost = theStats.Cost;
                    plantDefinition.m_refreshTime = theStats.Refresh;
                    Main.Log($"{plantDefinition.m_seedType} {plantDefinition.m_launchRate}");
                }
            }
            Main.Log("Reset randomised plant stats.");

            var projectileDefinitions = UnityEngine.Resources.FindObjectsOfTypeAll<ProjectileDefinition>();
            foreach (ProjectileDefinition projectileDefinition in projectileDefinitions)
            {
                if (defaultProjectileDamages.ContainsKey(projectileDefinition.m_projectileType))
                {
                    projectileDefinition.m_damage = defaultProjectileDamages[projectileDefinition.m_projectileType];
                }
            }
            Main.Log("Reset randomised projectile stats.");
        }

        public static void ApplyPlantStats()
        {
            var plantDefinitions = UnityEngine.Resources.FindObjectsOfTypeAll<PlantDefinition>();
            foreach (PlantDefinition plantDefinition in plantDefinitions)
            {
                if (plantStats.ContainsKey(plantDefinition.m_seedType))
                {
                    PlantStats theStats = plantStats[plantDefinition.m_seedType];
                    plantDefinition.m_launchRate = theStats.Rate;
                    plantDefinition.m_seedCost = theStats.Cost;
                    plantDefinition.m_refreshTime = theStats.Refresh;
                }
            }
            Main.Log("Applied randomised plant stats.");

            var projectileDefinitions = UnityEngine.Resources.FindObjectsOfTypeAll<ProjectileDefinition>();
            foreach (ProjectileDefinition projectileDefinition in projectileDefinitions)
            {
                if (Data.projectileTypes.Contains(projectileDefinition.m_projectileType))
                {
                    string projectileIndex = Array.FindIndex(Data.projectileTypes, projectileType => projectileType == projectileDefinition.m_projectileType).ToString();
                    if (APClient.projectileDamages.ContainsKey(projectileIndex))
                    {
                        projectileDefinition.m_damage = (int)APClient.projectileDamages[projectileIndex];
                    }
                    else if (projectileDefinition.m_projectileType == ProjectileType.PeashooterPea && APClient.projectileDamages.ContainsKey("0"))
                    {
                        projectileDefinition.m_damage = (int)APClient.projectileDamages["0"];
                    }
                    else if ((projectileDefinition.m_projectileType == ProjectileType.Fireball || projectileDefinition.m_projectileType == ProjectileType.PeashooterFireball) && APClient.projectileDamages.ContainsKey("0"))
                    {
                        projectileDefinition.m_damage = ((int)APClient.projectileDamages["0"]) * 2;
                    }
                }
            }
            Main.Log("Applied randomised projectile stats.");
        }

        public static string FormatPlantStatChanges(string label, double oldValue, double newValue, bool upIsGood)
        {
            double multiplier = newValue / oldValue;
            if (label == "Rate")
            {
                multiplier = 1 / multiplier; //Invert the firing rate multiplier for clarity
            }
            if (oldValue == newValue)
            {
                return "";
            }

            string textColor = "<color=black>◌ ";
            if (multiplier > 1)
            {
                if (upIsGood)
                {
                    textColor = "<color=#00B400>↑ ";
                }
                else
                {
                    textColor = "<color=#B40000>↑ ";
                }
            }
            else if (multiplier < 1)
            {
                if (upIsGood)
                {
                    textColor = "<color=#B40000>↓ ";
                }
                else
                {
                    textColor = "<color=#00B400>↓ ";
                }
            }

            return $"{textColor}{label} x{multiplier:F2}</color><br>";
        }

        [HarmonyPatch(typeof(Plant), nameof(Plant.PlantInitialize))]
        public static class PlantInitializePatch
        {
            private static void Postfix(Plant __instance)
            {
                if (APClient.plantHealths.Count > 0 && __instance.mBoard != null && __instance.mSeedType != null)
                {
                    int levelId = Data.GetLevelIdFromGameplayActivity(__instance.mApp);
                    if (__instance.mBoard.ChooseSeedsOnCurrentLevel() || APClient.conveyorMap.ContainsKey(levelId.ToString()))
                    {
                        SeedType theSeedType = __instance.mSeedType;
                        if (plantStats.ContainsKey(theSeedType))
                        {
                            PlantStats theStats = plantStats[theSeedType];
                            if (theStats.Health > 0)
                            {
                                __instance.mPlantMaxHealth = theStats.Health;
                                __instance.mPlantHealth = theStats.Health;
                            }
                        }
                    }
                }
            }
        }

        public static void SetupPlantStats()
        {
            //Set up plant stats
            foreach (var plant in plantStats)
            {
                SeedType theSeedType = plant.Key;
                PlantStats theStats = plant.Value;
                string plantIndex = Array.FindIndex(Data.seedTypes, seedType => seedType == theSeedType).ToString();
                string nonConveyorStats = "";
                string otherStats = "";
                theStats.BackupStats();
                if (APClient.sunPrices.ContainsKey(plantIndex))
                {
                    if (APClient.easyUpgradePlants && theStats.EasyUpgradeCost > theStats.Cost)
                    {
                        nonConveyorStats += FormatPlantStatChanges("Cost", theStats.OldStats.EasyUpgradeCost, (double)APClient.sunPrices[plantIndex], false);
                    }
                    else
                    {
                        nonConveyorStats += FormatPlantStatChanges("Cost", theStats.OldStats.Cost, (double)APClient.sunPrices[plantIndex], false);
                    }
                    theStats.Cost = (int)APClient.sunPrices[plantIndex];
                }
                if (APClient.rechargeTimes.ContainsKey(plantIndex))
                {
                    nonConveyorStats += FormatPlantStatChanges("Refresh", theStats.OldStats.Refresh, (double)APClient.rechargeTimes[plantIndex], false);
                    theStats.Refresh = (int)APClient.rechargeTimes[plantIndex];
                }
                if (APClient.plantHealths.ContainsKey(plantIndex))
                {
                    otherStats += FormatPlantStatChanges("Toughness", theStats.OldStats.Health, (double)APClient.plantHealths[plantIndex], true);
                    theStats.Health = (int)APClient.plantHealths[plantIndex];
                }
                if (APClient.firingRates.ContainsKey(plantIndex))
                {
                    otherStats += FormatPlantStatChanges("Rate", theStats.OldStats.Rate, (double)APClient.firingRates[plantIndex], true);
                    theStats.Rate = (int)APClient.firingRates[plantIndex];
                }
                if (theStats.Projectiles != null)
                {
                    foreach (string projectileName in theStats.Projectiles)
                    {
                        ProjectileType theProjectileType = Data.projectileNamesToTypes[projectileName];
                        int projectileDamage = defaultProjectileDamages[theProjectileType];
                        string projectileIndex = Array.FindIndex(Data.projectileTypes, projectileType => projectileType == theProjectileType).ToString();
                        if (APClient.projectileDamages.ContainsKey(projectileIndex))
                        {
                            string damageName = "Damage";
                            if (theStats.Projectiles.Count > 1)
                            {
                                damageName = $"{projectileName} Damage";
                            }
                            otherStats += FormatPlantStatChanges(damageName, projectileDamage, (double)APClient.projectileDamages[projectileIndex], true);
                        }
                    }
                }
                if (nonConveyorStats == "" && otherStats == "")
                {
                    otherStats = "◌ No Changes";
                }
                theStats.StatsString = nonConveyorStats + otherStats;
                theStats.ConveyorStatsString = otherStats;
            }
        }
    }
}
