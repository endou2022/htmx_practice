FROM python:3.12-bullseye

WORKDIR /app

#localeを日本語にする
# https://qiita.com/valzer0/items/db7639d8231bf5121297 (2024/10/01)
# https://www.rcnp.osaka-u.ac.jp/~kobayash/be_koba/mem/debian.html (2024/10/01)
RUN apt-get update && apt-get install -y locales
RUN echo "ja_JP.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen && update-locale LANG=ja_JP.UTF-8

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
