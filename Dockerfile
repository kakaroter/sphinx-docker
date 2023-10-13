FROM ubuntu:latest
COPY . /home
WORKDIR /home
RUN apt update && apt install python3 python3-pip -y 
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
RUN apt install vim tree -y
EXPOSE 3000
EXPOSE 8080
