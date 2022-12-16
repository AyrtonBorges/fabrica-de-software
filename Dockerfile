FROM ubuntu
    RUN apt update && apt upgrade -y
    RUN apt install g++ -y
    RUN apt install python3 -y
    RUN apt install python3-pip -y
    RUN pip install snscrape
    RUN pip install pandas
    COPY main.py .
    RUN python3 main.py