FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app 

COPY requirements.txt

RUN uv pip install --system -r requirements.txt 

COPY . /app 

CMD ["python", "app.py"]