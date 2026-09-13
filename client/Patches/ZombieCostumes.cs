using HarmonyLib;
using Il2CppReloaded.Gameplay;
using Il2CppReloaded.Services;
using Il2CppReloaded.TreeStateActivities;
using System.Collections.Generic;

namespace ReplantedArchipelago.Patches
{
    public class ZombieCostumes
    {
        public static bool forceRetro = false;
        public static bool forceChina = false;
        public static bool forcePlatform = false;

        [HarmonyPatch(typeof(GameplayActivity), nameof(GameplayActivity.CreateZombieController))]
        public static class CreateZombieControllerPatch
        {
            private static void Prefix(ref ZombieType type, ref Zombie zombie, ref bool forceDecember)
            {
                if (APClient.costumeChances.Count > 0)
                {
                    List<string> possibleSkins = new List<string>();
                    if (type == ZombieType.Normal)
                    {
                        if (APClient.costumeChances.ContainsKey("Zombie (China)") && Data.random.Next(10000) < (int)APClient.costumeChances["Zombie (China)"] && (!((zombie.mRow == 2 || zombie.mRow == 3) && (zombie.mBoard.mBackground == BackgroundType.Pool || zombie.mBoard.mBackground == BackgroundType.Fog))))
                        {
                            possibleSkins.Add("China");
                        }
                        if (APClient.costumeChances.ContainsKey("Zombie (Retro)") && Data.random.Next(10000) < (int)APClient.costumeChances["Zombie (Retro)"])
                        {
                            possibleSkins.Add("Retro");
                        }
                        if (APClient.costumeChances.ContainsKey("Zombie (Winter)") && Data.random.Next(10000) < (int)APClient.costumeChances["Zombie (Winter)"])
                        {
                            possibleSkins.Add("Winter");
                        }
                    }
                    else if (type == ZombieType.TrafficCone)
                    {
                        if (APClient.costumeChances.ContainsKey("Conehead (China)") && Data.random.Next(10000) < (int)APClient.costumeChances["Conehead (China)"] && (!((zombie.mRow == 2 || zombie.mRow == 3) && (zombie.mBoard.mBackground == BackgroundType.Pool || zombie.mBoard.mBackground == BackgroundType.Fog))))
                        {
                            possibleSkins.Add("China");
                        }
                        if (APClient.costumeChances.ContainsKey("Conehead (Winter)") && Data.random.Next(10000) < (int)APClient.costumeChances["Conehead (Winter)"])
                        {
                            possibleSkins.Add("Winter");
                        }
                        if (APClient.costumeChances.ContainsKey("Conehead (Headcrab)") && Data.random.Next(10000) < (int)APClient.costumeChances["Conehead (Headcrab)"])
                        {
                            possibleSkins.Add("Platform");
                        }
                    }
                    else if ((type == ZombieType.Flag && APClient.costumeChances.ContainsKey("Flag (China)") && (Data.random.Next(10000) < (int)APClient.costumeChances["Flag (China)"]) && (!((zombie.mRow == 2 || zombie.mRow == 3) && (zombie.mBoard.mBackground == BackgroundType.Pool || zombie.mBoard.mBackground == BackgroundType.Fog)))) ||
                        (type == ZombieType.Pail && APClient.costumeChances.ContainsKey("Buckethead (China)") && (Data.random.Next(10000) < (int)APClient.costumeChances["Buckethead (China)"]) && (!((zombie.mRow == 2 || zombie.mRow == 3) && (zombie.mBoard.mBackground == BackgroundType.Pool || zombie.mBoard.mBackground == BackgroundType.Fog)))) ||
                        (type == ZombieType.Polevaulter && APClient.costumeChances.ContainsKey("Polevaulter (China)") && (Data.random.Next(10000) < (int)APClient.costumeChances["Polevaulter (China)"])) ||
                        (type == ZombieType.Football && APClient.costumeChances.ContainsKey("Football (China)") && (Data.random.Next(10000) < (int)APClient.costumeChances["Football (China)"])) ||
                        (type == ZombieType.Bungee && APClient.costumeChances.ContainsKey("Bungee (China)") && (Data.random.Next(10000) < (int)APClient.costumeChances["Bungee (China)"])))
                    {
                        possibleSkins.Add("China");
                    }

                    if (possibleSkins.Count > 0)
                    {
                        string chosenSkin = possibleSkins[Data.random.Next(possibleSkins.Count)];
                        if (chosenSkin == "China")
                        {
                            forceChina = true;
                        }
                        else if (chosenSkin == "Winter")
                        {
                            forceDecember = true;
                        }
                        else if (chosenSkin == "Retro")
                        {
                            forceRetro = true;
                            zombie.mIsRetro = true;
                        }
                        else if (chosenSkin == "Platform")
                        {
                            forcePlatform = true;
                        }
                    }
                }
            }
        }

        [HarmonyPatch(typeof(GameplayService), "get_ChinaModeActive")]
        public static class ChinaModePatch
        {
            private static bool Prefix(GameplayService __instance, ref bool __result)
            {
                if (__instance.m_currentLevelData.m_gameArea != GameArea.China)
                {
                    __result = forceChina;
                    forceChina = false;
                    return false;
                }
                return true;
            }
        }

        [HarmonyPatch(typeof(GameplayService), "get_RetroContentActive")]
        public static class RetroContentPatch
        {
            private static bool Prefix(GameplayService __instance, ref bool __result)
            {
                __result = forceRetro;
                forceRetro = false;
                return false;
            }
        }

        [HarmonyPatch(typeof(GameplayService), "get_PlatformContentActive")]
        public static class PlatformContentPatch
        {
            private static bool Prefix(GameplayService __instance, ref bool __result)
            {
                __result = forcePlatform;
                forceRetro = false;
                return false;
            }
        }

        [HarmonyPatch(typeof(GameplayActivity), nameof(GameplayActivity.CreatePlantController))]
        public static class CreatePlantControllerPatch
        {
            private static void Prefix(GameplayActivity __instance, ref SeedType type, ref bool forceDecemberContent, ref bool forceRetroContent)
            {
                if (type == SeedType.Wallnut && APClient.costumeChances.ContainsKey("Wall-nut (Winter)") && Data.random.Next(10000) < (int)APClient.costumeChances["Wall-nut (Winter)"])
                {
                    forceDecemberContent = true;
                }
                else if (type == SeedType.Peashooter)
                {
                    bool selectedWinter = false;
                    bool selectedRetro = false;

                    if (APClient.costumeChances.ContainsKey("Peashooter (Winter)"))
                    {
                        selectedWinter = Data.random.Next(10000) < (int)APClient.costumeChances["Peashooter (Winter)"];
                    }
                    if (APClient.costumeChances.ContainsKey("Peashooter (Retro)"))
                    {
                        selectedRetro = Data.random.Next(10000) < (int)APClient.costumeChances["Peashooter (Retro)"];
                    }

                    if (selectedRetro)
                    {
                        Il2CppOOI.Platforms.Platform platform = UnityEngine.Object.FindObjectOfType<Il2CppOOI.Platforms.Platform>();
                        selectedRetro = platform.HasPreOrder; //Can't use Retro Peashooter if you didn't pre-order
                    }

                    if (selectedWinter && selectedRetro)
                    {
                        selectedWinter = Data.random.Next(2) == 1;
                        selectedRetro = !selectedWinter;
                    }

                    if (selectedWinter)
                    {
                        forceDecemberContent = true;
                    }
                    else if (selectedRetro)
                    {
                        forceRetroContent = true;
                    }
                }
            }
        }
    }
}
