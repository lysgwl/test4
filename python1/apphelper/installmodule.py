# -*- coding: UTF-8 -*-

from appfactory import AppFactory

# 安装模块
class InstallModule:
    def __init__(self, config):
        self.config = config
        self.factory = AppFactory.getInstance()
        
    def add(self, apptype):
        try:
            app = self.factory.createAppModule(apptype, self.config)
            if app is not None:
                app.init()
        except Exception as e:
            print("An error occurred in InstallModule.add:", str(e))

    def run(self):
        try:
            applist = self.factory.getAppModule(None)
            for app in applist:
                app.exec()
        except Exception as e:
            print("An error occurred in InstallModule.run:", str(e))