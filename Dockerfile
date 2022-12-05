FROM ubuntu
    RUN apt update && apt upgrade -y
    RUN apt install g++ -y
    RUN apt install python3 -y
    CMD /bin/bash