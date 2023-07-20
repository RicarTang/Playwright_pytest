使用pytest+playwright+allure进行e2e自动化测试
## 依赖
- pytest-playwright
- PyYAML
- allure-pytest
## 使用
1. 初始化pipenv并安装依赖
```Bash
pipenv install
```
2. 下载playwright运行的浏览器环境
```Bash
pipenv shell
playwright install
```
3. 启动测试
```Bash
pipenv run test
```