FROM python:3.12

WORKDIR /ImagesCaptureApp/

RUN apt update && apt install -y \
    wget \
    curl \
    chromium \
    chromium-driver

RUN apt install -y libpq-dev python-dev-is-python3

RUN python -m pip install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install python-dotenv

COPY . .
RUN pip3 install -r requirements.txt

# meu entrypoint podia ser um shell script
ENTRYPOINT [ "python" , "app.py"]
