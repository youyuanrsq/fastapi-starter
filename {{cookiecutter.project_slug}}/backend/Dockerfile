ARG PYTHON_VER=3.10
# Base stage for building the app
FROM python:${PYTHON_VER} AS base

WORKDIR /src

ENV PYTHONUNBUFFERED=1

# Set the timezone environment variable
ENV TZ=Asia/Shanghai

# Install time zone packages and set the default timezone
RUN apt-get update && apt-get install -y --no-install-recommends tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /src/

RUN poetry install --no-root

COPY . /src

# Final stage with slim image
FROM python:3.10-slim

WORKDIR /src

# Set the timezone environment variable
ENV TZ=Asia/Shanghai

# Copy files from the base stage
COPY --from=base /src /src
COPY --from=base /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=base /usr/local/bin /usr/local/bin

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]
