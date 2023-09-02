# -*- coding: UTF-8 -*-

from config import ConfigModule
from appfactory import AppFactory
from processmgr import ProcessMgr

class RunModule:
    def __init__(self, config):
        self.config = config
        self.factory = AppFactory.getInstance()
        self.process = ProcessMgr()

    def run(self, apptype):
        if apptype is not None:
            app = self.factory.getAppModule(apptype)
            if app is None:
                return
            
            command_tuple = app.get()
            if len(command_tuple) > 0:
                command_str = ' '.join(command_tuple)
                self.process.start_process(self.config.system_type, command_str)
        else:
            applist = self.factory.getAppModule(None)
            for app in applist:
                if app is None:
                    continue

                command_tuple = app.get()
                if len(command_tuple) > 0:
                    command_str = ' '.join(command_tuple)
                    self.process.start_process(self.config.system_type, command_str)

        self.process.wait_for_processes()