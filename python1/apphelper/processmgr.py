# -*- coding: UTF-8 -*-
import subprocess

class ProcessMgr:
    def __init__(self):
        self.processes = []

    def start_process(self, system_type, command):
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

        process = subprocess.Popen(command, shell=True, stdout=stdout, stderr=stderr, startupinfo=startupinfo)
        self.processes.append(process)

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
            