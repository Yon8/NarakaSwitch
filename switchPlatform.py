import os
import shutil
from getGameInit import get_netease_Gameinit
from tomlLoad import modify_toml


GameInit_path = "program\\NarakaBladepoint_Data\\StreamingAssets\\GameInit"


def switch_to_steam(netease_path):
    # 拼接完整路径
    local_GameInit_path = os.path.join(netease_path, GameInit_path)

    if not os.path.exists("file/GameInit_Steam"):
        print("找不到Steam GameInit文件")
        print("请Steam版Naraka更新至最新版本后 将config中的platform设置为0后再次运行执行初始化")
    else:
        shutil.copy("file/GameInit_Steam", local_GameInit_path)
        modify_toml("config", "platform", 1)
        print("切换Steam版本成功")


def switch_to_netease(netease_path):
    # 拼接完整路径
    local_GameInit_path = os.path.join(netease_path, GameInit_path)
    get_netease_Gameinit()
    if not os.path.exists("file/GameInit_Netease"):
        print("获取Netease_GameInit失败，请检查网络连接")
    else:
        shutil.copy("file/GameInit_Netease", local_GameInit_path)
        modify_toml("config", "platform", 2)
        print("切换Netease版本成功")
