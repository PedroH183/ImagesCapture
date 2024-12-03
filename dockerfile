FROM python:3.10.14

RUN pip3 install poetry

WORKDIR /app

COPY . .

RUN  poetry lock --no-update && poetry install && rm -rf $POETRY_CACHE_DIR
RUN touch README.md

EXPOSE 5000

ENTRYPOINT [ "poetry", "run", "python", "main.py" ]