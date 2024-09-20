import os
import sys

from newVersion import get_new_version
from localVersion import get_local_version, set_local_version
from tomlLoad import load_config, modify_toml
from getGameInit import get_steam_GameInit
from switchPlatform import switch_to_netease, switch_to_steam
from updateRepair import update_repair

config = load_config()
platform = config['config']['platform']
netease_path = config['config']['netease_path']

if not os.path.exists(os.path.join(netease_path, "program")):
    print("路径选择错误！")
    sys.exit()

local_version = get_local_version(netease_path)
new_version = get_new_version()
print("本地版本为" + local_version)
print("云端版本为" + new_version)


if local_version != new_version:
    print("请确认Steam更新至最新版本后再进行后续操作！")
    is_update = input("请输入对应选项 1.我速速去把Steam端更新至最新版 2.我已经更新到最新版了")
    if is_update == '1':
        sys.exit()
    elif is_update == '2':
        set_local_version(netease_path, new_version)
        local_version = new_version
        update_repair(netease_path)
        get_steam_GameInit(netease_path)
    else:
        sys.exit()
if local_version == new_version:
    if platform == 0:
        print("第一次运行,请确认当前游戏为Steam端，进行初始化操作！")
        print("1.不是Steam端，我去点击Steam游戏修复后再来 2.是Steam端，继续下一步")
        is_steam = input("请输入对应选项:")
        if is_steam == '1':
            sys.exit()
        elif is_steam == '2':
            get_steam_GameInit(netease_path)
            modify_toml("config", "platform", 1)
            platform = 1
        else:
            sys.exit()

    if platform == 1:
        print("当前平台为Steam,请选择要切换的平台 1.steam 2.netease")
    elif platform == 2:
        print("当前平台为Netease,请选择要切换的平台 1.steam 2.netease")
    else:
        print("请按照注释填写配置文件")
    switch_platform = input("请输入选项:")
    if switch_platform == '1':
        switch_to_steam(netease_path)
    elif switch_platform == '2':
        switch_to_netease(netease_path)
    else:
        print("输入选项错误")
        sys.exit()




