# -*- coding: UTF-8 -*-
import os
import json

from config import ConfigModule
from component import Component
from funchelper import funchelper

# aria2模块
class Aria2Module(Component):
    def __init__(self, config):
        self.config = config
        self.aria2_name = "aria2"
        
        self.aria2_usr_path = self.config.usr_path
        self.aria2_bin_path = os.path.join(self.config.bin_path, self.aria2_name)
        self.aria2_etc_path = os.path.join(self.config.etc_path, self.aria2_name)
        
        self.system_type = self.config.system_type.lower()
        self.aria2_tag_url = "https://api.github.com/repos/aria2/aria2/releases/latest"
        
        self.aria2_file_extension = f"{self.aria2_name}c{'.exe' if self.system_type == 'windows' else ''}"
        self.aria2_filename_pattern = f"{self.aria2_name}*.{'zip' if self.system_type == 'windows' else 'tar.gz'}"
        
        self.aria2_dht_file = os.path.join(self.aria2_etc_path, f"dht.dat")
        self.aria2_dht6_file = os.path.join(self.aria2_etc_path, f"dht6.dat")
        self.aria2_cfg_file = os.path.join(self.aria2_etc_path, f"{self.aria2_name}.conf")
        self.arai2_session_file = os.path.join(self.aria2_etc_path, f"{self.aria2_name}.session")
        
    def init(self):
        try:
            command = f"where {self.aria2_file_extension}" if self.system_type == 'windows' else f"which {self.aria2_file_extension}"
            returncode, stdout, stderr = funchelper.run_process_command(command)
            if returncode == 0 and stdout:
                self.aria2_installed = True
                self.aria2_bin_file = stdout
            else:
                self.aria2_installed = False
                self.aria2_bin_file = os.path.join(self.aria2_bin_path, self.aria2_file_extension)
            
            self.aria2_server_command = f"{self.aria2_bin_file}"
            self.aria2_server_command += f" --conf-path={self.aria2_cfg_file}"
            self.aria2_server_command += f" --dht-file-path={self.aria2_dht_file}"
            self.aria2_server_command += f" --dht-file-path6={self.aria2_dht6_file}"
            self.aria2_server_command += f" --input-file={self.arai2_session_file}"
            self.aria2_server_command += f" --save-session={self.arai2_session_file}"

            os.makedirs(self.aria2_bin_path, exist_ok=True)
            os.makedirs(self.aria2_etc_path, exist_ok=True)
        except Exception as e:
            print("An error occurred in Aria2Module:", str(e))

    def get(self):
        if not self.aria2_server_command:
            return None
        
        command_tuple = tuple(self.aria2_server_command.split())
        return command_tuple

    def exec(self):
        try:
            if self.aria2_installed:
                self._setaria2env() 
            else:    
                funchelper.copy_process_files(self.config.data_path, self.aria2_usr_path, self.aria2_name, self.aria2_filename_pattern)
                
                if not os.path.exists(self.aria2_bin_path) or os.path.exists(self.aria2_bin_file):
                    return
                
                filepath = funchelper.find_latest_files(self.aria2_usr_path, self.aria2_filename_pattern)
                if not filepath:
                    self._downloadPackages()
                        
                if len(filepath) == 0:
                    return
                    
                # 安装软件包
                self._installPackages(filepath)
                
                funchelper.search_and_copy_files(self.aria2_bin_path, self.aria2_file_extension)
                
                # 设置环境
                self._setaria2env() 
                
        except Exception as e:
            print("An error occurred in AlistModule:", str(e))
 
    def _downloadPackages(self):
        pass

    def _installPackages(self, filepath):
        # 清空目录下所有文件
        funchelper.remove_files_and_directories(self.aria2_bin_path)

        # 解压文件到安装目录
        funchelper.extract_files(filepath, self.aria2_bin_path)

    def _setaria2env(self):
        # aria2.conf
        conf_file = os.path.join(self.config.data_path, f"{self.aria2_name}", f"{self.aria2_name}.conf")
        if os.path.exists(conf_file):
            if os.path.exists(self.aria2_cfg_file):
                funchelper.remove_files_and_directories(self.aria2_cfg_file)
            funchelper.copy_files_or_directories(conf_file, self.aria2_etc_path)
        
        # dht.dat
        dht_file = os.path.join(self.config.data_path, f"{self.aria2_name}", f"dht.dat")
        if os.path.exists(dht_file):
            if os.path.exists(self.aria2_dht_file):
                funchelper.remove_files_and_directories(self.aria2_dht_file)
            funchelper.copy_files_or_directories(dht_file, self.aria2_etc_path)

        # dht6.dat
        dht6_file = os.path.join(self.config.data_path, f"{self.aria2_name}", f"dht6.dat")
        if os.path.exists(dht6_file):
            if os.path.exists(self.aria2_dht6_file):
                funchelper.remove_files_and_directories(self.aria2_dht6_file)
            funchelper.copy_files_or_directories(dht6_file, self.aria2_etc_path) 

        # 创建aria2.session空白文件
        if not os.path.exists(self.arai2_session_file):
            with open(self.arai2_session_file, 'w') as file:
                pass