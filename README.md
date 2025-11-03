# Django Project

这是一个Django开发项目。

## 环境要求

- Python 3.8+
- pip

## 安装步骤

1. 创建虚拟环境（推荐）：
```bash
python -m venv venv
```

2. 激活虚拟环境：
   - Windows (PowerShell):
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```bash
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 创建Django项目：
```bash
django-admin startproject me .
```

5. 运行迁移：
```bash
python manage.py migrate
```

6. 创建超级用户（可选）：
```bash
python manage.py createsuperuser
```

7. 启动开发服务器：
```bash
python manage.py runserver
```

访问 http://127.0.0.1:8000/ 查看项目。

## 项目结构

```
.
├── manage.py          # Django管理脚本（运行django-admin startproject后生成）
├── me/                # 项目配置目录（运行django-admin startproject后生成）
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── requirements.txt   # 项目依赖
├── README.md         # 项目说明
└── .gitignore        # Git忽略文件
```

## 常用命令

- 创建应用: `python manage.py startapp app_name`
- 创建迁移: `python manage.py makemigrations`
- 应用迁移: `python manage.py migrate`
- 收集静态文件: `python manage.py collectstatic`
- 进入Django shell: `python manage.py shell`

