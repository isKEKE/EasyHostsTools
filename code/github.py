# _*_ coding: utf-8 _*_
import sys
from updateHosts import UpdateHosts
if __name__ == "__main__":
    command = sys.argv
    print('''Github更新IP小脚本...''')
    try:
        if command[1] == "update":
            if UpdateHosts.go() != 0:
                print("更新失败.")
            else:
                print("更新成功.")
    except IndexError:
        pass
    UpdateHosts.pause()