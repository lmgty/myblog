# myblog

一个使用了Django和Vue的单页面博客应用
http://123.207.107.211/

---

### Step 1: 装前端依赖

```
cd myblog/frontend
npm install
```

### Step 2: 构建前端

在 frontend 目录构建前端页面

```
npm run build
```

### Step 3: 通过 Django 自带 server 启动项目

In the directory where manage.py is located

```
pip install -r requirements.txt
python manage runserver
```

---


## 与前端结合的原理

前端构建完成就下面这两个资源

- index.html
- static/\*

让我们看看如何处理这两个资源

### 第一个. index.html

使用 [django template engines](https://docs.djangoproject.com/en/dev/topics/templates/) 去处理 `index.html` 文件

在 `settings.py` 中

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': ['frontend/dist'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

我们改变 `TEMPLATES.DIRS` 从而让 Django 能够找到 `index.html` 文件在哪。

### 第二个. static/\*

同样是在 `settings.py` 中

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/dist/static"),
]
```

我们添加 `STATICFILES_DIRS` 配置，这个配置可以让 Django 找以下资源的时候：

```html
<script type=text/javascript src=/static/js/vendor.677ef0c9485c32b4f6a9.js></script>
```

在 frontend/dist/static_ 这个目录寻找，但是需要注意的是，这只在 django 的开发模式下才生效。

## 生产环境

我们在生产环境使用 Nginx 处理前端页面

- index.html
- static/\*

使用 Django 来开发 API，JSON 来传输数据。



<div align=right>谢谢阅读</div>
<div align=right>Thanks for watching</div>
