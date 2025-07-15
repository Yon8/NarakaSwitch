import os
import shutil

import requests

from newVersion import get_new_version

# 需要获取的DLL文件名列表
dll_files = ["NtUniSDKResources.dll", "NtUniSdkBase.dll",'NtUniSdkGMBridge.dll','NtUniSdkNgWebview.dll','unisdk_dll_load_whitelist','webview_support_helper.dll']

# 拼接最新版本DLL文件地址
def get_dll_fetch_url(dll_name):
    return f"https://d90.gdl.netease.com/publish/{get_new_version()}/program/{dll_name}"


def get_netease_dll():
    """从网易CDN获取DLL文件"""
    if not os.path.exists("file"):
        os.makedirs("file")

    for dll_name in dll_files:
        dll_url = get_dll_fetch_url(dll_name)
        print(f"正在下载 {dll_name}...")
        
        response = requests.get(dll_url, stream=True)

        if response.status_code == 200:
            # 将下载流写入文件
            with open(f"file/{dll_name}_Netease", "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"{dll_name}_Netease文件下载成功")
        else:
            print(f"{dll_name}_Netease文件下载失败，状态码：{response.status_code}")


def get_steam_dll(netease_path):
    """从Steam本地路径获取DLL文件"""
    if not os.path.exists("file"):
        os.makedirs("file")

    for dll_name in dll_files:
        dll_path = f"program\\{dll_name}"
        # 拼接完整路径
        local_dll_path = os.path.join(netease_path, dll_path)
        
        # 判断路径是否存在
        if os.path.exists(local_dll_path):
            # 复制文件
            shutil.copy(local_dll_path, f"file\\{dll_name}_Steam")
            print(f"{dll_name}_Steam文件复制成功")
        else:
            print(f"{dll_name}_Steam文件路径不存在：{local_dll_path}")


    