import os

version_path = "program\\version.txt"


def get_local_version(netease_path):
    # 拼接完整路径
    local_version_path = os.path.join(netease_path, version_path)
    local_version = open(local_version_path, "r").read()
    return local_version


def set_local_version(netease_path, new_version):
    # 拼接完整路径
    local_version_path = os.path.join(netease_path, version_path)
    open(local_version_path, "w").write(new_version)
