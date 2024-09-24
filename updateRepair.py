import os

import requests

from newVersion import get_new_version

repair_file = ['NE_SamplingPlugin.dll','NE_NvNgxDlss.dll','NarakaBladepoint.exe','GameAssembly.dll',
               'NtUniSDKResources.dll','NeacSafe64.sys','NtUniSdkBase.dll','NeacClient.exe',
               'NtUniSdkMpay.dll','NeacInterface.dll','UnityCrashHandler64.exe','StartGame.exe',
               'UnityPlayer.dll','ffx_fsr2_api_dx11_x64.dll','ffx_backend_dx12_x64.dll','mpay.dll',
               'libxess.dll','unisdk_dll_load_whitelist','nvngx_dlss.dll']
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

