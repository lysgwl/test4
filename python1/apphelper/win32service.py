# encoding=utf-8

import subprocess

class win32service:
    def __init__(self, service_name, display_name, binary_path, start_type="auto"):
        self.service_name = service_name
        self.display_name = display_name
        self.binary_path = binary_path
        self.start_type = start_type

    def svc_create(self):
        command = f'sc create "{self.service_name}" binPath= "{self.binary_path}" start= {self.start_type} displayname= "{self.display_name}"'
        result = subprocess.run(command, shell=True)

        success = 1 if result.returncode == 0 else 0
        return success

    def svc_delete(self):
        command = f'sc delete "{self.service_name}"'
        result = subprocess.run(command, shell=True)

        success = 1 if result.returncode == 0 else 0
        return success

    def svc_open(self):
        command = f'sc start "{self.service_name}"'
        result = subprocess.run(command, shell=True)

        success = 1 if result.returncode == 0 else 0
        return success

    def svc_close(self):
        command = f'sc stop "{self.service_name}"'
        result = subprocess.run(command, shell=True)

        success = 1 if result.returncode == 0 else 0
        return success

    def svc_getstatus(self):
        command = f'sc query "{self.service_name}"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout.strip()

        if result.returncode == 0 and output.startswith("State="):
            status = output.split('=')[1]
            if "RUNNING" in output:
                return 1
            elif "STOPPED" in output:
                return 0
            else:
                return 2
        return -1