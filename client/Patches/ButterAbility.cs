using HarmonyLib;
using Il2CppReloaded.Gameplay;
using Il2CppSource.Controllers;
using System;
using UnityEngine;

namespace ReplantedArchipelago.Patches
{
    public class ButterAbility
    {
        public static int butterCooldownLength = 2000;
        public static GameObject butter;
        public static GameObject disabledButter;
        public static GameObject butterTimer;

        public static void CreateButterUI()
        {
            GameObject uiObject = GameObject.Find("Panels/P_Gameplay_MainHUD/Canvas/Layout/Center");
            if (uiObject != null)
            {
                GameObject conveyorSeedBank = uiObject.transform.Find("ConveyorSeedBank").gameObject;
                if (conveyorSeedBank == null || !conveyorSeedBank.activeSelf)
                {
                    butter = uiObject.transform.Find("TopLeftLayout/ButterContainer/Butter").gameObject;
                }
                else
                {
                    butter = uiObject.transform.Find("ConveyorSeedBank/Butter").gameObject;
                }

                if (butter != null)
                {
                    GameObject butterDisplay = butter.transform.Find("ControllerVisblity/Butter").gameObject;
                    UnityEngine.UI.Button button = butter.AddComponent<UnityEngine.UI.Button>();
                    button.onClick.AddListener(((Action)ButterClicked));
                    butter.SetActive(ButterAllowed());

                    disabledButter = GameObject.Instantiate(butterDisplay, butterDisplay.transform.parent);
                    disabledButter.name = "DisabledButter";
                    UnityEngine.UI.Image butterImage = disabledButter.GetComponent<UnityEngine.UI.Image>();
                    butterImage.color = new UnityEngine.Color(0f, 0f, 0f, 0.7f);
                    disabledButter.SetActive(false);

                    butterTimer = GameObject.Instantiate(disabledButter, disabledButter.transform.parent);
                    butterTimer.name = "ButterTimer";
                    UnityEngine.UI.Image butterTimerImage = butterTimer.GetComponent<UnityEngine.UI.Image>();
                    butterTimerImage.type = UnityEngine.UI.Image.Type.Filled;
                    butterTimerImage.fillMethod = UnityEngine.UI.Image.FillMethod.Vertical;
                    butterTimerImage.fillOrigin = (int)UnityEngine.UI.Image.OriginVertical.Top;
                    butterTimer.SetActive(false);

                    GameObject.Destroy(butter.transform.Find("ControllerVisblity/PlayerNumber").gameObject);
                }
            }
        }

        public static void ButterClicked()
        {
            if (Main.cachedGameplayActivity.m_board.mCursorObject.mCursorType == CursorType.Normal)
            {
                if (Main.cachedGameplayActivity.m_board.mPottedPlantsCollected > 1)
                {
                    Main.cachedGameplayActivity.m_audioService.PlaySample(Il2CppReloaded.Constants.Sound.SOUND_BUZZER);
                }
                else
                {
                    Main.cachedGameplayActivity.m_board.PickUpTool(ReloadedObjectType.Phonograph);
                    Main.cachedGameplayActivity.m_board.mCursorObject.mCursorType = CursorType.TreeFood;
                    GameObject.Find("GridOffset/Cursor(Clone)/Render/Sprite").GetComponent<SpriteRenderer>().sprite = Graphics.GetGraphic("SPR_Butter");
                    GameObject.Find("GridOffset/Cursor(Clone)/Render/Sprite").GetComponent<SpriteRenderer>().transform.localScale = new Vector3(1.5f, 1.5f, 1f);
                    ToggleCustomButterObjects(true);
                }
            }
        }

        public static void ToggleCustomButterObjects(bool visible)
        {
            if (visible && butter != null)
            {
                GameObject disabledControllerPrompt = GameObject.Find("Panels/P_Gameplay_MainHUD/Canvas/Layout/Center/TopLeftLayout/ButterContainer/Butter/ControllerVisblity/DisabledButter/P_ControllerPrompt_Butter");
                if (disabledControllerPrompt != null)
                {
                    GameObject.Destroy(disabledControllerPrompt);
                }

                GameObject timerControllerPrompt = GameObject.Find("Panels/P_Gameplay_MainHUD/Canvas/Layout/Center/TopLeftLayout/ButterContainer/Butter/ControllerVisblity/ButterTimer/P_ControllerPrompt_Butter");
                if (timerControllerPrompt != null)
                {
                    GameObject.Destroy(timerControllerPrompt);
                }

                GameObject disabledControllerPromptConveyor = GameObject.Find("Panels/P_Gameplay_MainHUD/Canvas/Layout/Center/ConveyorSeedBank/Butter/ControllerVisblity/DisabledButter/P_ControllerPrompt_Butter");
                if (disabledControllerPromptConveyor != null)
                {
                    GameObject.Destroy(disabledControllerPromptConveyor);
                }

                GameObject timerControllerPromptConveyor = GameObject.Find("Panels/P_Gameplay_MainHUD/Canvas/Layout/Center/ConveyorSeedBank/Butter/ControllerVisblity/ButterTimer/P_ControllerPrompt_Butter");
                if (timerControllerPromptConveyor != null)
                {
                    GameObject.Destroy(timerControllerPromptConveyor);
                }
            }
            if (disabledButter != null)
            {
                disabledButter.SetActive(visible);
            }
            if (butterTimer != null)
            {
                butterTimer.SetActive(visible);
            }
        }

        [HarmonyPatch(typeof(GamepadCursorController), nameof(GamepadCursorController._updateTertiaryAction))]
        public static class GamepadCursorControllerUpdateTertiaryActionPatch
        {
            private static bool Prefix(GamepadCursorController __instance)
            {
                __instance.m_canButter = false;
                if (__instance.m_tertiaryAction.WasPressedThisFrame() && ButterAbility.CanButterRightNow(__instance.Board))
                {
                    __instance.m_cursor.mBoard.MouseDownButterUpZombie(__instance.m_obj.mApp.m_widgetManager.LastMouseX[__instance.m_playerIndex], __instance.m_obj.mApp.m_widgetManager.LastMouseY[__instance.m_playerIndex]);
                    return false;
                }
                return true;
            }
        }

        [HarmonyPatch(typeof(Board), nameof(Board.MouseDownButterUpZombie))]
        public static class MouseDownButterUpZombiePatch
        {
            private static bool Prefix(Board __instance)
            {
                return CanButterRightNow(__instance);
            }

            private static void Postfix(Board __instance, ref Zombie __result)
            {
                if (__result != null && !__result.mMindControlled)
                {
                    __instance.mPottedPlantsCollected = butterCooldownLength; //Begin buttering cooldown
                    __result.mButteredCounter = 900;
                    ToggleCustomButterObjects(true);
                }
            }
        }

        [HarmonyPatch(typeof(Board), nameof(Board.MouseDownWithTool))]
        public static class MouseDownWithToolPatch
        {
            private static void Prefix(Board __instance, ref int x, ref int y, ref int theClickCount, ref CursorType theCursorType, ref int playerIndex)
            {
                if (theCursorType == CursorType.TreeFood)
                {
                    __instance.MouseDownButterUpZombie(x, y);
                }
            }
        }

        public static void UpdateButterCooldown(Board board)
        {
            if (board.mPottedPlantsCollected > 0)
            {
                board.mPottedPlantsCollected -= 1;
                if (board.mPottedPlantsCollected <= 1)
                {
                    ToggleCustomButterObjects(false);
                }
                else
                {
                    if (butterTimer != null)
                    {
                        butterTimer.GetComponent<UnityEngine.UI.Image>().fillAmount = board.mPottedPlantsCollected / (float)butterCooldownLength;
                    }
                }
            }
        }

        [HarmonyPatch(typeof(Board), nameof(Board.ClearCursor))]
        public static class ClearCursorPatch
        {
            private static void Postfix(Board __instance)
            {
                if (CanButterRightNow(__instance))
                {
                    ToggleCustomButterObjects(false);
                }
            }
        }

        public static bool ButterAllowed()
        {
            return APClient.receivedItems.Contains(2004) && !(Main.cachedGameplayActivity == null || Main.cachedGameplayActivity.IsSlotMachineLevel() || Main.cachedGameplayActivity.IsWhackAZombieLevel() || Main.cachedGameplayActivity.GameMode == GameMode.ChallengeBeghouled || Main.cachedGameplayActivity.GameMode == GameMode.ChallengeBeghouledTwist || Main.cachedGameplayActivity.IsIZombieLevel() || Main.cachedGameplayActivity.GameMode == GameMode.ChallengeZombiquarium || Main.cachedGameplayActivity.GameMode == GameMode.ChallengeZenGarden || Main.cachedGameplayActivity.GameMode == GameMode.TreeOfWisdom || Main.cachedGameplayActivity.IsScaryPotterLevel());
        }

        public static bool CanButterRightNow(Board board)
        {
            return butter != null && ButterAllowed() && board.mPottedPlantsCollected <= 1;
        }
    }
}
