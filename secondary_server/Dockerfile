FROM python

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN python -m pip install -r /app/requirements.txt
RUN python -m grpc_tools.protoc -I ./ --python_out=. --grpc_python_out=. secondary_grpc/ReplicatedLog.proto

ENTRYPOINT ["python", "secondary_server.py"]
