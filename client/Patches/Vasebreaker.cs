using HarmonyLib;
using Il2CppBest.HTTP.Shared.Extensions;
using Il2CppReloaded.Gameplay;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;

namespace ReplantedArchipelago.Patches
{
    public class Vasebreaker
    {
        [HarmonyPatch(typeof(Challenge), nameof(Challenge.ScaryPotterPopulate))]
        public static class ScaryPotterPopulatePatch
        {
            private static void Postfix(Challenge __instance)
            {
                String levelId = Data.GetLevelIdFromGameplayActivity(__instance.mApp).ToString();

                //Random Plants
                if (APClient.vasebreakerPlantMap.ContainsKey(levelId))
                {
                    JObject plants = (JObject)APClient.vasebreakerPlantMap[levelId][__instance.mSurvivalStage];
                    List<SeedType> seedTypes = new List<SeedType>();

                    foreach (var property in plants.Properties())
                    {
                        SeedType theSeedType;
                        if (property.Name.ToInt32() == 107)
                        {
                            theSeedType = SeedType.Leftpeater;
                        }
                        else
                        {
                            theSeedType = Data.seedTypes[property.Name.ToInt32()];
                        }
                        seedTypes.AddRange(Enumerable.Repeat(theSeedType, (int)property.Value));
                    }

                    for (int gridItemIndex = 0; gridItemIndex < __instance.mBoard.m_gridItems.Count; gridItemIndex++)
                    {
                        if (__instance.mBoard.m_gridItems[gridItemIndex].mGridItemType == GridItemType.ScaryPot && __instance.mBoard.m_gridItems[gridItemIndex].mSeedType != SeedType.None)
                        {
                            int seedIndex = UnityEngine.Random.Range(0, seedTypes.Count());
                            SeedType seedToUse = seedTypes[seedIndex];
                            __instance.mBoard.m_gridItems[gridItemIndex].mSeedType = seedToUse;
                            seedTypes.RemoveAt(seedIndex);
                        }
                    }
                }

                //Random Zombies
                if (APClient.vasebreakerZombieMap.ContainsKey(levelId))
                {
                    JObject zombies = (JObject)APClient.vasebreakerZombieMap[levelId][__instance.mSurvivalStage];
                    List<ZombieType> zombieTypes = new List<ZombieType>();

                    foreach (var property in zombies.Properties())
                    {
                        ZombieType theZombieType = Data.zombieTypes[property.Name.ToInt32()];
                        zombieTypes.AddRange(Enumerable.Repeat(theZombieType, (int)property.Value));
                    }

                    for (int gridItemIndex = 0; gridItemIndex < __instance.mBoard.m_gridItems.Count; gridItemIndex++)
                    {
                        if (__instance.mBoard.m_gridItems[gridItemIndex].mGridItemType == GridItemType.ScaryPot && __instance.mBoard.m_gridItems[gridItemIndex].mSeedType == SeedType.None)
                        {
                            int zombieIndex = UnityEngine.Random.Range(0, zombieTypes.Count());
                            ZombieType zombieToUse = zombieTypes[zombieIndex];
                            __instance.mBoard.m_gridItems[gridItemIndex].mZombieType = zombieToUse;
                            zombieTypes.RemoveAt(zombieIndex);
                        }
                    }
                }

            }
        }
    }
}
