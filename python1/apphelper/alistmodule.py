# -*- coding: UTF-8 -*-
import os
import json
import secrets

from config import ConfigModule
from component import Component
from funchelper import funchelper

# alist模块
class AlistModule(Component):
    def __init__(self, config):
        self.config = config
        self.alist_name = "alist"
        self.alist_http_port = "8015"

        self.alist_usr_path = self.config.usr_path
        self.alist_bin_path = os.path.join(self.config.bin_path, self.alist_name)
        self.alist_etc_path = os.path.join(self.config.etc_path, self.alist_name)

        self.system_type = self.config.system_type.lower()
        self.alist_tag_url = "https://api.github.com/repos/alist-org/alist/releases/latest"

        self.alist_file_extension = f"{self.alist_name}{'.exe' if self.system_type == 'windows' else ''}"
        self.alist_filename_pattern = f"{self.alist_name}*.{'zip' if self.system_type == 'windows' else 'tar.gz'}"
        
        self.alist_cfg_file = os.path.join(self.alist_etc_path, "config.json")
        self.alist_admin_file = os.path.join(self.alist_bin_path, "admin_passwd.txt")
        
    def init(self):
        try:
            command = f"where {self.alist_file_extension}" if self.system_type == 'windows' else f"which {self.alist_file_extension}"
            returncode, stdout, stderr = funchelper.run_process_command(command)
            if returncode == 0 and stdout:
                self.alist_installed = True
                self.alist_bin_file = stdout
            else:
                self.alist_installed = False
                self.alist_bin_file = os.path.join(self.alist_bin_path, self.alist_file_extension)

            self.alist_server_command = f"{self.alist_bin_file}"  
            self.alist_server_command += f" server --data "  
            self.alist_server_command += f"{self.alist_etc_path} "  # &>/dev/null &

            self.alist_admin_command = f"{self.alist_bin_file}"
            self.alist_admin_command += f" admin --data "
            self.alist_admin_command += f"{self.alist_etc_path}"

            os.makedirs(self.alist_bin_path, exist_ok=True)
            os.makedirs(self.alist_etc_path, exist_ok=True)
        except Exception as e:
            print("An error occurred in AlistModule:", str(e))

    def get(self):
        if not self.alist_server_command:
            return None
        
        command_tuple = tuple(self.alist_server_command.split())
        return command_tuple

    def exec(self):
        try:
            if self.alist_installed:
                pass
            else:
                funchelper.copy_process_files(self.config.data_path, self.alist_usr_path, self.alist_name, self.alist_filename_pattern)
            
                if not os.path.exists(self.alist_bin_path) or os.path.exists(self.alist_bin_file):
                    return
                
                filepath = funchelper.find_latest_files(self.alist_usr_path, self.alist_filename_pattern)
                if not filepath:
                    self._downloadPackages()
                    
                if len(filepath) == 0:
                    return
                
                # 安装alist软件包
                self._installPackages(filepath)

                # 设置alist环境
                self._setalistenv() 
                
        except Exception as e:
            print("An error occurred in AlistModule:", str(e))

    def _downloadPackages(self):
        pass

    def _installPackages(self, filepath):
        # 清空目录下所有文件
        funchelper.remove_files_and_directories(self.alist_bin_path)

        # 解压文件到安装目录
        funchelper.extract_files(filepath, self.alist_bin_path)

    def _setalistenv(self):
        # 生成alist的json配置文件
        self._setalistjsoncfg()

        # 获取alist的管理密码
        returncode, stdout, stderr = funchelper.run_process_command(self.alist_admin_command, "'latin-1")

        user_info = stdout or stderr
        json_array = [
            {'match': "Admin", 'key': "username", 'value': r".*Admin.*:\s*(.*)$"},
            {'match': "Successfully", 'key': "password", 'value': r".*Successfully.*:\s*(.*)$"}
        ]

        json_obj = funchelper.get_regex_userinfo(user_info, json_array)
        if json_obj is None:
            return
        
        json_str = json.dumps(json_obj)
        with open(self.alist_admin_file, "w") as file:
            file.write(json_str)

    def _setalistjsoncfg(self):
        if os.path.exists(self.alist_cfg_file):
            os.remove(self.alist_cfg_file)

        data = {
            'force': False,
            'site_url': '',
            'cdn': '',
            'jwt_secret': secrets.token_urlsafe(12)[:16],
            'token_expires_in': 48,
            'database': {
                'type': 'sqlite3',
                'host': '',
                'port': 0,
                'user': '',
                'password': '',
                'name': '',
                'db_file': os.path.join(os.path.join(self.alist_etc_path, 'data'), 'data.db'),
                'table_prefix': 'x_',
                'ssl_mode': ''
            },
            'scheme': {
                'address': '0.0.0.0',
                'http_port': int(self.alist_http_port),
                'https_port': -1,
                'force_https': False,
                'cert_file': '',
                'key_file': '',
                'unix_file': '',
                'unix_file_perm': ''
            },
            'temp_dir': os.path.join(self.alist_etc_path, 'data', 'temp'),
            'bleve_dir': os.path.join(self.alist_etc_path, 'data', 'bleve'),
            'log': {
                'enable': True,
                'name': os.path.join(os.path.join(self.alist_etc_path, 'data', 'log'), 'log.log'),
                'max_size': 50,
                'max_backups': 30,
                'max_age': 28,
                'compress': False
            },
            'delayed_start': 0,
            'max_connections': 0,
            'tls_insecure_skip_verify': True
        }

        config_info = {}
        data.update(config_info)

        with open(self.alist_cfg_file, 'w') as file:
            json.dump(data, file)