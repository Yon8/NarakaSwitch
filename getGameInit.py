import os
import shutil

import requests

from newVersion import get_new_version

# 拼接最新版本GameInit文件地址
GameInit_fetch_url = "https://d90.gdl.netease.com/publish/" + get_new_version() + "/program/NarakaBladepoint_Data" \
                                                                                  "/StreamingAssets/GameInit "




def get_netease_Gameinit():
    if not os.path.exists("file"):
        os.makedirs("file")

    response = requests.get(GameInit_fetch_url, stream=True)

    if response.status_code == 200:
        # 将下载流写入文件
        with open("file/GameInit_Netease", "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print("GameInit_Netease文件下载成功")
    else:
        print("GameInit_Netease文件下载失败")


def get_steam_GameInit(netease_path):
    GameInit_path = "program\\NarakaBladepoint_Data\\StreamingAssets\\GameInit"
    # 拼接完整路径
    local_GameInit_path = os.path.join(netease_path, GameInit_path)
    # 判断路径是否存在
    if os.path.exists(local_GameInit_path):
        if not os.path.exists("file"):
            os.makedirs("file")
        # 复制文件
        shutil.copy(local_GameInit_path, "file\\GameInit_Steam")
