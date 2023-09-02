# -*- coding: UTF-8 -*-

from appfactory import AppFactory

# 安装模块
class InstallModule:
    def __init__(self, config):
        self.config = config
        self.factory = AppFactory.getInstance()
        
    def add(self, apptype):
        app = self.factory.createAppModule(apptype, self.config)
        if app is not None:
            app.init()

    def run(self):
        applist = self.factory.getAppModule(None)
        for app in applist:
            app.exec()