# {{ cookiecutter.project_name }}

## 开发与部署

### 部署

首先需要按照env-template文件创建.env文件，然后填入对应的配置。

在本地通过docker-compose启动

```bash
docker-compose up -d

# 数据库迁移

```shell

docker-compose exec backend alembic upgrade head
```

启动后就可以通过这个URL访问OpenAPI文档

- 后端OpenAPI文档: "http://localhost:{{ cookiecutter.backend_port }}/docs/"

打开这个链接后可以看到FastAPI提供的可交互式的API文档，可以直接在这里进行测试。

### 本地开发

后端服务起来后会挂载src目录，并且会自动识别到代码的改动，自动重启服务，这一点非常方便在本地开发。

#### Poetry 环境搭建

在本地开发时，需要[安装](https://python-poetry.org/docs/)poetry，然后通过poetry安装依赖。

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

安装好Poetry后，在/backend目录下执行命令来安装对应的环境：

```bash
poetry install
```

如果需要增加新的依赖，比如增加新的包，可以通过以下命令来安装：

```bash
poetry add <package_name>
```

### 重新构建容器

如果增加了新的依赖，那么需要通过以下命令重新构建容器：

```bash
docker-compose up -d --build
```

### 数据库迁移/更新

使用alembic进行数据库迁移时，主要使用这两个命令。更多信息请参考[Alembic's tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)。

```bash
# 自动生成一个 revision
docker-compose exec backend alembic revision --autogenerate -m 'message'

# 将最新的改动同步到数据库
docker-compose exec backend alembic upgrade head
```

如果增加了一个新的package，如completion，那么都需要将其中的models import到`./backend/alembic/env.py`
中，否则alembic无法识别到新的models。

当有新的models或者改动了原先的models，需要同步到数据库时，需要先执行`alembic revision --autogenerate -m 'message'`
来生成一个revision，然后再执行`alembic upgrade head`来同步到数据库。
