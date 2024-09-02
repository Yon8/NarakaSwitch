
import xml.etree.ElementTree as ET
import requests
# netease配置文件地址
x = requests.get("https://update.yjwujian.cn/publish/data.xml")
# xml文件处理
root = ET.fromstring(x.content)
# 获取版本信息
config = root.find("config")
version = config.find("TargetVersion").attrib["value"]


def get_new_version():
    return version