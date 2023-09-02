# -*- coding: UTF-8 -*-

import re
import os
import sys

import platform
from enum import Enum
from funchelper import funchelper

# 配置模块
class ConfigModule:
    class AppType(Enum):
        ALIST_TYPE = 0x011
        ARIA2_TYPE = 0x012

    def __init__(self, root_path):
        self.root_path = root_path
    
        self.run_path = os.path.join(self.root_path, "run")
        self.data_path = os.path.join(self.root_path, "data")

        self.bin_path = os.path.join(self.run_path, "bin")
        self.etc_path = os.path.join(self.run_path, "etc")
        self.usr_path = os.path.join(self.run_path, "usr")
        self.var_path = os.path.join(self.run_path, "var")

        self.system_type = platform.system()
        self.lock_file = os.path.join(self.run_path, "lock_file.lock")

    def init_env(self):
        os.makedirs(self.run_path, exist_ok=True)
        os.makedirs(self.data_path, exist_ok=True)

        os.makedirs(self.bin_path, exist_ok=True)
        os.makedirs(self.etc_path, exist_ok=True)
        os.makedirs(self.usr_path, exist_ok=True)
        os.makedirs(self.var_path, exist_ok=True)

    def check_run_instance(self):
        try:
            if os.path.exists(self.lock_file):
                run_pid = ""
                with open(self.lock_file, 'r') as fp:
                    content = fp.read()
                    pid = re.search(r'.*=(\d+)', content)
                    if pid:
                        run_pid = pid.group(1)

                if funchelper.check_process_running(self.system_type, run_pid):
                    sys.exit(1)
            else:   
                with open(self.lock_file, 'w') as fp:
                    fp.write('lock pid={}\n'.format(os.getpid()))

        except SystemExit as e:    
            exit_code = e.code
            print("程序退出，退出码为:", exit_code)

    def remove_run_instance(self):
        if os.path.exists(self.lock_file):
            os.remove(self.lock_file)