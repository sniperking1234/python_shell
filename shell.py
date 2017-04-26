import os
import sys
import shlex
import getpass
import socket
import signal
import subprocess
import platform
from func import *

# 一张字典表，用于存储命令与函数的映射
built_in_cmds = {}


def register_command(name, func):
    """
    注册命令，使命令与相应的处理函数建立映射关系
    @param name: 命令名
    @param func: 函数名
    """
    built_in_cmds[name] = func


def init():
    """
    注册所有的命令
    """
    register_command("cd", cd)
    register_command("exit", exit)
    register_command("getenv", getenv)
    register_command("history", history)


def shell_loop():
    """
    shell 循环
    :return: 
    """
    status = SHELL_STATUS_RUN
    while status = SHELL_STATUS_RUN:
        # 打印命令提示符
        display_cmd_prompt()

        # 忽略Ctrl-Z 或者Ctrl-C
        ignore_signals()

        try:
            # 读取命令
            cmd = sys.stdin.readline()

            # 拆解命令
            cmd_tokens = tokenize(cmd)

            # 预处理
            #　将环境中的环境变量替换为真实值
            cmd_tokens = preprocess(cmd_tokens)

            status = execute(cmd_tokens)

        except:
            _, err, _ = sys.exec_info()
            print(err)

def main():
    init()
    shell_loop()

if __name__ == "__main__":
    main()

