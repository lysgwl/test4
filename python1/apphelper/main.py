# -*- coding: UTF-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import ConfigModule
from installmodule  import InstallModule
from runmodule import RunModule

def main(): 
    try:
        # 获取脚本路径
        if getattr(sys, 'frozen', False):
            root_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        else:
            root_path = os.path.dirname(os.path.abspath(__file__))

        # 创建配置模块
        config = ConfigModule(root_path)

        # 初始化配置环境
        config.init_env()

        # 检测运行实例
        config.check_run_instance()
        
        # 创建安装模块
        install_Module = InstallModule(config)

        # 添加应用至安装模块
        install_Module.add(config.AppType.ARIA2_TYPE)
        install_Module.add(config.AppType.ALIST_TYPE)
        
        # 运行安装模块
        install_Module.run()

        # 创建运行模块
        run_module = RunModule(config)

        # 运行应用 
        run_module.run(None)   #config.AppType.ALIST_TYPE

    except Exception as e: 
        # 处理异常
        print("An error occurred:", str(e))
    finally:    
        # 删除运行实例
        config.remove_run_instance()

if __name__ == '__main__': 
    main()