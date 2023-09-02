# -*- coding: UTF-8 -*-

from alistmodule import AlistModule
from aria2module import Aria2Module

# 应用工厂  
class AppFactory:
    __instance = None

    @staticmethod
    def getInstance():
        if AppFactory.__instance is None:
            AppFactory()
        return AppFactory.__instance
    
    def __init__(self):
        self.applist = {}
        if AppFactory.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AppFactory.__instance = self

    def createAppModule(self, apptype, config):
        app_types = {
            config.AppType.ALIST_TYPE: AlistModule,
            config.AppType.ARIA2_TYPE: Aria2Module
        }

        appobj = app_types.get(apptype)
        if appobj:
            appobj = appobj(config)
            self.applist[apptype] = appobj

        return appobj
    
    def getAppModule(self, apptype):
        if apptype is not None:
            return self.applist[apptype]
        else:
            return self.applist.values()