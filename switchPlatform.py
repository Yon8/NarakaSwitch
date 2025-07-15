import os
import shutil
from getGameInit import get_netease_Gameinit
from updateRepair import update_repair
from tomlLoad import modify_toml


GameInit_path = "program\\NarakaBladepoint_Data\\StreamingAssets\\GameInit"
Program_path = "program"

def switch_to_steam(netease_path):
    # 拼接完整路径
    local_GameInit_path = os.path.join(netease_path, GameInit_path)
    if not os.path.exists("file/GameInit_Steam"):
        print("找不到Steam GameInit文件")
        print("请Steam版Naraka更新至最新版本后 将config中的platform设置为0后再次运行执行初始化")
    else:
        shutil.copy("file/GameInit_Steam", local_GameInit_path)
        shutil.copy("file/NtUniSDKResources.dll_Steam", os.path.join(netease_path, Program_path,"NtUniSDKResources.dll"))
        shutil.copy("file/NtUniSdkBase.dll_Steam", os.path.join(netease_path, Program_path,"NtUniSdkBase.dll"))
        shutil.copy("file/NtUniSdkGMBridge.dll_Steam", os.path.join(netease_path, Program_path,"NtUniSdkGMBridge.dll"))
        shutil.copy("file/NtUniSdkNgWebview.dll_Steam", os.path.join(netease_path, Program_path,"NtUniSdkNgWebview.dll"))
        shutil.copy("file/unisdk_dll_load_whitelist_Steam", os.path.join(netease_path, Program_path,"unisdk_dll_load_whitelist"))
        shutil.copy("file/webview_support_helper.dll_Steam", os.path.join(netease_path, Program_path,"webview_support_helper.dll"))
        modify_toml("config", "platform", 1)
        print("切换Steam版本成功")


def switch_to_netease(netease_path):
    # 拼接完整路径
    local_GameInit_path = os.path.join(netease_path, GameInit_path)
    get_netease_Gameinit()
    update_repair(netease_path)
    if not os.path.exists("file/GameInit_Netease"):
        print("获取Netease_GameInit失败，请检查网络连接")
    else:
        shutil.copy("file/GameInit_Netease", local_GameInit_path)
        modify_toml("config", "platform", 2)
        print("切换Netease版本成功")
