import os

class Config:
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///album.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 应用程序配置
    SECRET_KEY = 'your-secret-key-here'
    DEBUG = True
    
    # 上传配置
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    
    # 图片配置
    PICKSUM_BASE_URL = 'https://picsum.photos'
    PHOTO_SIZE = '600/400'
    GIF_SIZE = '800/400'