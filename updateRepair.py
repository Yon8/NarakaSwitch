import os

import requests

from newVersion import get_new_version

repair_file = ['NtUniSDKResources.dll','NtUniSdkBase.dll', 'NtUniSdkMpay.dll','mpay.dll'
               ,'NtUniSdkGMBridge.dll','NtUniSdkNgWebview.dll','unisdk_dll_load_whitelist','webview_support_helper.dll']
fetch_base_url = "https://d90.gdl.netease.com/publish/" + get_new_version() + "/program/"

def update_repair(netease_path):
    for file in repair_file:
        print("修补" + file)
        fetch_url = fetch_base_url + file
        response = requests.get(fetch_url, stream=True)

        if response.status_code == 200:
            # 将下载流写入文件
            file_path = os.path.join(netease_path, "program", file)
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        else:
            print(file + "文件下载失败")

