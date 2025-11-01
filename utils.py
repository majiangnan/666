import random
import string
from datetime import datetime, timedelta


def generate_photo_seed(photo_id, category):
    """生成照片的seed参数"""
    return f"class_album_{photo_id}_{category}"


def generate_gif_seed(gif_id):
    """生成动图的seed参数"""
    return f"class_gif_{gif_id}"


def generate_random_date(days=90):
    """生成随机日期（过去指定天数内）"""
    return datetime.now() - timedelta(days=random.randint(0, days))


def generate_random_string(length=8):
    """生成随机字符串"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def allowed_file(filename, allowed_extensions):
    """检查文件扩展名是否允许"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


def format_date(date_obj):
    """格式化日期显示"""
    return date_obj.strftime('%Y-%m-%d %H:%M:%S')


def paginate(data_list, page, per_page):
    """简单分页功能"""
    start = (page - 1) * per_page
    end = start + per_page
    total = len(data_list)
    pages = (total + per_page - 1) // per_page
    
    return {
        'items': data_list[start:end],
        'total': total,
        'page': page,
        'pages': pages,
        'per_page': per_page
    }