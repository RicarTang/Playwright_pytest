"""文件读取"""
import json
from typing import Any

def call_and_return(func):
    """使类__call__直接返回"""
    def wrapper(*args, **kwargs):
        instance = func(*args, **kwargs)
        return instance()
    return wrapper

@call_and_return
class LoadFile:
    """读取文件类"""
    def __init__(self,file:str):
        self.file = file
        
    def loadjson(self, file:str):
        """读取json文件"""
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def loadyaml(self, file:str):
        """读取yaml文件"""
        with open(file, 'r', encoding='utf-8') as f:
            import yaml
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data
    
    def __call__(self, *args: Any, **kwds: Any) -> list:
        """判断文件后缀调用方法"""
        if self.file.endswith(".yaml") or self.file.endswith(".yml"):
            return self.loadyaml(self.file)
        elif self.file.endswith(".json"):
            return self.loadjson(self.file)
        elif self.file.endswith(".xlsx"):
            pass
        else:
            raise ValueError("请输入正确的文件path")


if __name__ == '__main__':
    print(LoadFile('data/test_data/create_wallet_data.yaml'))