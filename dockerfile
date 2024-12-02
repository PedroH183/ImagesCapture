# TIP : o entrypoint do postgres já é definido por padrão no docker-entrypoint.initdb.d !
FROM postgres:15

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_DB=ImageCaptureDb

COPY ./Database/ /docker-entrypoint-initdb.d/

EXPOSE 5432

# ------------------------------------------------------------------ #
FROM python:3.9

WORKDIR /api-sys
RUN pip3 install poetry

COPY . .

RUN pip install --upgrade pip
RUN poetry install

EXPOSE 5000
ENTRYPOINT [ "poetry", "run", "python", "main.py" ]