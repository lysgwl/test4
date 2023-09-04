# encoding=utf-8

import os
import re
import sys
import glob
import json
import shutil
import zipfile
import tarfile
import subprocess

class funchelper(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance
    
    def __init__(self):
        pass

    # 指定目录遍历文件
    def search_files(directory, file_extension):
        found_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(file_extension):
                    found_files.append(os.path.join(root, file))
        return found_files
    
    # 指定目录遍历文件，并拷贝文件至指定的目录
    def search_and_copy_files(directory, file_extension):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(file_extension):
                    target_dir  = os.path.abspath(directory)
                    file_path = os.path.join(root, file)
                    shutil.copy(file_path, target_dir)
                    break

    # 查找匹配的文件列表并按名称排序
    def find_latest_files(usr_path, filename_pattern):
        if len(usr_path) == 0 or len(filename_pattern) == 0:
            return ""
        
        filelist = sorted(glob.glob(os.path.join(usr_path, filename_pattern)), key=lambda x: x.lower())
        if len(filelist) == 0:
            return ""
        
        filepath = filelist[-1]
        return filepath
    
    # 清空指定目录下所有文件
    def remove_files_and_directories(files_path):
        if os.path.isdir(files_path):
            for filename in os.listdir(files_path):
                file_path = os.path.join(files_path, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
        elif os.path.isfile(files_path):
             os.remove(files_path)        

    # 文件或目录的复制拷贝
    def copy_files_or_directories(source_path, dest_path):
        try:
            if os.path.isfile(source_path):
                shutil.copy2(source_path, dest_path)
            elif os.path.isdir(source_path):
                shutil.copytree(source_path, dest_path)
            else:
                raise Exception("Invalid source path")
            return 1
        except Exception as e:
            return 0

    # 解压文件到指定目录
    def extract_files(file_path, extract_path):
        if file_path.endswith(".zip"):
            with zipfile.ZipFile(file_path, 'r') as ref:
                ref.extractall(extract_path)
        elif file_path.endswith(".tar.gz"):
            with tarfile.open(file_path, 'r:gz') as ref:
                ref.extractall(extract_path)
        else:
            print("This file format is not supported!", file_path)

    # 检查进程是否在运行中
    def check_process_running(system_type, process_id, process_name=None, encode_type=None):
        def run_command(encode_type, command):
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, encoding=encode_type) 
            stdout, stderr = process.communicate()
            returncode = process.returncode
            if returncode != 0:
                return False
            return stdout
            
        if process_id is not None:
            command = f'tasklist /FI "PID eq {process_id}"' if system_type.lower() == 'windows' else f'ps -p {process_id}'
            stdout = run_command(encode_type, command)
            if not stdout:
                return False
            
            pattern = re.compile(rf'\b{process_id}\b')
            match = re.search(pattern, stdout)
            if not match:
                return False
            return True
            
        if process_name is not None:
            command = f'tasklist /FI "IMAGENAME eq {process_name}" /NH' if system_type.lower() == 'windows' else f'pgrep {process_name}'
            stdout = run_command(encode_type, command)
            if not stdout:
                return False
            
            pattern = re.compile(rf'\b{process_name}\b', re.IGNORECASE)
            process_names = re.findall(pattern, stdout)

            if not process_name in process_names:
                return False
            return True
    
    # 运行指定进程服务
    def run_process_server(system_type, command_args, encode_type=None):
        if system_type.lower() == 'windows':
            startupinfo = subprocess.STARTUPIFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE

            # creationflags=subprocess.DETACHED_PROCESS
            # creationflags=subprocess.CREATE_NO_WINDOW
            # creationflags=subprocess.CREATE_NEW_CONSOLE  # process.communicate()
            process = subprocess.Popen(command_args, shell=True, startupinfo=startupinfo, encoding=encode_type)
        elif system_type.lower() == 'linux':
            subprocess.Popen(command_args, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, encoding=encode_type)
        else:
            print("Unsupported system type!")
        return
    
    # 运行指定命令,并返回状态码和信息
    def run_process_command(command_args, encode_type=None):
        process = subprocess.Popen(command_args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, encoding=encode_type) 
        stdout, stderr = process.communicate()

        stdout = stdout.strip() if stdout else ''
        stderr = stderr.strip() if stderr else ''  
        returncode = process.returncode

        return returncode, stdout, stderr
    
    def get_regex_userinfo(user_info, json_array):
        if not isinstance(json_array, list):
            return None
        
        # 获取 JSON 数组的大小
        array_size = len(json_array)

        # 将字符串按行分割
        lines = user_info.split('\n')

        #返回的json对象数据
        json_obj = {}

        # 遍历 JSON 数组并获取对象
        for obj in json_array:
            for line in lines:
                regexp = obj['value']
                match = re.search(regexp, line)
                if not match:
                    continue

                key = obj['key']
                user_data = match.group(1).strip()

                json_obj[key] = user_data
                break

        return json_obj    
    
    # 备份目录查找软件安装包
    def copy_process_files(data_path, usr_path, usr_name, filename_pattern):
        if funchelper.find_latest_files(usr_path, filename_pattern):
            return
        
        tmp_usr_path = os.path.join(data_path, usr_name)
        if not os.path.exists(tmp_usr_path):
            return
        
        filepath = funchelper.find_latest_files(tmp_usr_path, filename_pattern)
        if len(filepath) <= 0:
            return
        
        funchelper.copy_files_or_directories(filepath, usr_path)