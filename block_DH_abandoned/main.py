import sys
import clr
# clr.FindAssembly('PyConnDH')
clr.AddReference('PyConnDH')
from PyConnDH import *

# 计算模块
def calc():
    csvOutPath = sys.executable.split("python.exe")[0] + "PyComDH\\out"  # 获取csv所在文件夹路径的方法,DLL里是自动获取了Application的路径，所以py调用时就是在python.exe的那个目录
    csvInPath = sys.executable.split("python.exe")[0] + "PyComDH\\in"

    calcInfo = calcDH.doCal()  # 开始计算
    if calcInfo.split(",")[0] == 'false':  # 计算异常
        print("调用计算失败：" + calcInfo.split(",")[1])  # 控制台输出异常问题
    else:
        print("调用计算成功")


if __name__ == '__main__':
    calc()
