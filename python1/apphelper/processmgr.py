# -*- coding: UTF-8 -*-
import os
import subprocess

class ProcessMgr:
    def __init__(self):
        self.processes = []

    def start_process(self, system_type, command, encode_type=None):
        if system_type.lower() == 'windows':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE

            stdout =  subprocess.PIPE
            stderr =  subprocess.PIPE
        elif system_type.lower() == 'linux':  
            startupinfo = None
             
            stdout =  subprocess.DEVNULL
            stderr =  subprocess.DEVNULL

        try:
            # 启动一个新的子进程
            process = subprocess.Popen(command, shell=True, stdout=stdout, stderr=stderr, startupinfo=startupinfo, encoding=encode_type)
            # 将子进程对象 process 添加到 self.processes 列表中
            self.processes.append(process)
        except subprocess.CalledProcessError as e:
            print(f"子进程引发异常: 异常类型:{type(e)}, 错误号:{e.returncode}, 错误消息:{e.stderr}")

    def pause_processes(self):
        for process in self.processes:
            process.send_signal(subprocess.signal.SIGSTOP)

    def resume_processes(self):
        for process in self.processes:
            process.send_signal(subprocess.signal.SIGCONT)

    def stop_processes(self):
        for process in self.processes:
            process.terminate()

    def wait_for_processes(self):
        for process in self.processes:
            try:
                process.wait()
            except KeyboardInterrupt: 
                process.terminate()    
            