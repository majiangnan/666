from flask import render_template, request, jsonify
from datetime import datetime, timedelta
import random
from app import app

# 首页路由
@app.route('/')
def index():
    return render_template('index.html')

# 简化版首页路由
@app.route('/simple')
def simple_view():
    # 生成模拟数据
    photos = []
    gifs = []
    categories = {
        'class': '课堂时光',
        'activity': '活动瞬间',
        'outdoor': '户外出行'
    }
    
    # 生成15张照片
    for i in range(15):
        category = ['class', 'activity', 'outdoor'][i % 3]
        photos.append({
            'id': i + 1,
            'title': f'{categories[category]} - 照片{i + 1}',
            'category': category,
            'category_name': categories[category],
            'url': f'https://picsum.photos/seed/class_album_{i}_{category}/600/400',
            'date': datetime.now().strftime('%Y-%m-%d')
        })
    
    # 生成5张动图
    for i in range(5):
        gifs.append({
            'id': i + 1,
            'title': f'精彩动图 {i + 1}',
            'url': f'https://picsum.photos/seed/class_gif_{i}/800/600'
        })
    
    return render_template('simple_index.html', photos=photos, gifs=gifs)

# 生成模拟数据函数
def generate_mock_data():
    # 分类数据
    categories = {
        'class': {'name': 'class', 'display_name': '课堂时光', 'description': '记录课堂上的精彩瞬间'},
        'activity': {'name': 'activity', 'display_name': '活动瞬间', 'description': '各种班级活动和聚会照片'},
        'outdoor': {'name': 'outdoor', 'display_name': '户外出行', 'description': '户外游玩和旅行的照片'}
    }
    
    # 照片标题数据
    photo_titles = {
        'class': ['认真听讲', '小组讨论', '课堂演示', '实验课', '提问环节', '课堂互动', '笔记分享', '课后辅导'],
        'activity': ['班级聚会', '才艺表演', '游戏环节', '合影留念', '生日庆祝', '颁奖仪式', '团队建设', '节日活动'],
        'outdoor': ['春游', '野餐', '徒步旅行', '风景照', '集体照', '自然探索', '户外运动', '参观学习']
    }
    
    # 生成照片数据
    photos = []
    photo_id = 1
    
    for cat_name, titles in photo_titles.items():
        for title in titles:
            # 生成随机日期
            days_ago = random.randint(0, 365)
            random_date = datetime.now() - timedelta(days=days_ago)
            
            photos.append({
                'id': photo_id,
                'title': title,
                'url': f"https://picsum.photos/seed/class_album_{photo_id}_{cat_name}/600/400",
                'category': cat_name,
                'category_name': categories[cat_name]['display_name'],
                'date': random_date.isoformat()
            })
            photo_id += 1
    
    # 生成动图数据
    gif_titles = ['班级舞蹈表演', '有趣的课堂瞬间', '运动会精彩时刻', '春游路上', '课间游戏', '才艺展示', '生日惊喜', '户外活动']
    gifs = []
    
    for i, title in enumerate(gif_titles, 1):
        days_ago = random.randint(0, 365)
        random_date = datetime.now() - timedelta(days=days_ago)
        
        gifs.append({
            'id': i,
            'title': title,
            'url': f"https://picsum.photos/seed/class_gif_{i}/800/400",
            'date': random_date.isoformat()
        })
    
    return {
        'photos': photos,
        'gifs': gifs,
        'categories': list(categories.values())
    }

# 获取模拟数据
mock_data = generate_mock_data()

# API 路由 - 获取照片列表
@app.route('/api/photos', methods=['GET'])
def get_photos():
    # 获取查询参数
    category = request.args.get('category', 'all')
    search = request.args.get('search', '')
    sort = request.args.get('sort', 'default')
    page = int(request.args.get('page', 1))
    per_page = 12
    
    # 获取照片数据
    photos = mock_data['photos']
    
    # 按分类筛选
    if category != 'all':
        photos = [p for p in photos if p['category'] == category]
    
    # 搜索筛选
    if search:
        photos = [p for p in photos if search.lower() in p['title'].lower()]
    
    # 排序
    if sort == 'date-desc':
        photos.sort(key=lambda x: x['date'], reverse=True)
    elif sort == 'date-asc':
        photos.sort(key=lambda x: x['date'])
    else:
        photos.sort(key=lambda x: x['id'], reverse=True)
    
    # 分页
    total = len(photos)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_photos = photos[start:end]
    pages = (total + per_page - 1) // per_page
    
    return jsonify({
        'photos': paginated_photos,
        'total': total,
        'page': page,
        'pages': pages,
        'per_page': per_page
    })

# API 路由 - 获取动图列表
@app.route('/api/gifs', methods=['GET'])
def get_gifs():
    return jsonify(mock_data['gifs'])

# API 路由 - 获取分类列表
@app.route('/api/categories', methods=['GET'])
def get_categories():
    return jsonify(mock_data['categories'])

# API 路由 - 健康检查
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.now().isoformat()
    })