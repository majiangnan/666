from flask import Flask
import os

# 创建Flask应用实例
app = Flask(__name__)

# 基本配置
app.config['SECRET_KEY'] = 'dev-key-for-testing'
app.config['DEBUG'] = True

# 导入路由（放在最后避免循环导入）
from routes import *

if __name__ == '__main__':
    # 启动应用
    app.run(host='0.0.0.0', port=5000, debug=True)