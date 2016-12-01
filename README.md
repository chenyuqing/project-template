# 项目模板
---

实际项目中需要添加以下内容：

> 安装

- 请将本项目放到合适的位置，如：
```
mkdir /opt/pylibs/
cd /opt/pylibs/
git clone git@github.com:Witee/project-template.git
cd xxx
```

- 使用 `python setup.py` 进行安装本模块


> 使用

- 测试

```
cd tests
python test.py

```

> 更新

cd 到项目目录后 `git pull`



----
以下是模板中每个部分的介绍，实际项目中可以删除

> 参考文档


` https://pythonguidecn.readthedocs.io/zh/latest/writing/structure.html `


> 必须的文件

- 文件 README.md

```
位置: 项目根目录
说明: 使用 markdown 语法编写项目说明，如 安装、使用等
```

- 文件 setup.py

```
位置: 项目根目录
说明: 使用此脚本将会把项目中的模块安装到系统中
```

- 文件 .gitignore

```
位置: 项目根目录
说明: git 中忽略某些文件
```

- 目录 myPkgName/

```
位置: 项目根目录
说明: 真正的模块目录，名称需要符合 python 变量命名规则，目录中需要有 __init__.py 文件
```

- 目录 docs/

```
位置: 项目根目录
说明: 模块的参考文档
```

- 目录 tests/

```
位置: 项目根目录
说明: 模块的测试用例
      # 将测试用例的上层目录加入到 python 搜索路径中，这样就可以导入模块
      # 先创建加载环境的文件 tests/environment.py ，如下:
      import os
      import sys
      sys.path.insert(0, os.path.abspath('..'))

      # 然后，在每一个测试文件中，导入环境:
      import environment
      # 之后就可以加载模块中的方法了
      from myPkgName import myPkg

      print myPkg.myFunc()

```

> 可选的文件



- 文件 requirements.txt

```
位置: 项目根目录
说明: 开发依赖说明，参考文档: https://pip.pypa.io/en/stable/user_guide/#requirements-files
```

- 文件 Makefile

```
位置: 项目根目录
说明: 使用管理脚本可以读取此文件，进行安装、测试

manage.py

init:
    pip install -r requirements.txt

test:
    py.test tests
```

- 文件 LICENSE

```
位置: 项目根目录
说明: 可直接使用项目模板中的此文件，如参考: http://choosealicense.com/
```

- 文件 push.sh

```
位置: 项目根目录
说明: 方便 push 代码
```
