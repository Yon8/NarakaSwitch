import os
import sys

import toml

tmol_name = "config.toml"


# 读取TOML配置文件
def load_config():
    if not os.path.exists(tmol_name):
        # 文件不存在，创建一个默认的TOML文件
        default_config = "[config]\n# 如E:\\\\Naraka 双反斜杠\nnetease_path = \"\"\n# 0.未初始化 1.steam 2.netease\nplatform = 0"
        with open(tmol_name, "w", encoding="utf-8") as f:
            f.write(default_config)
        print("默认配置文件不存在，创建配置文件,请修改配置文件后再次运行程序！")
        sys.exit()
    with open(tmol_name, "r", encoding="utf-8") as f:
        config = toml.load(f)
    return config


# 写入TOML文件
def write_toml(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        toml.dump(data, f)


# 修改TOML文件中的属性
def modify_toml(section, key, new_value):
    config = load_config()
    config[section][key] = new_value
    write_toml(config, tmol_name)
