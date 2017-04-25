From python:3.4 

USER root
RUN pip install --upgrade pip
RUN pip install flask && pip install flask --upgrade
RUN pip install plotly && pip install plotly --upgrade
RUN pip install numpy && pip install numpy --upgrade
RUN pip install pandas && pip install pandas --upgrade
RUN cd && mkdir apps
RUN apt-get update && apt-get install -y vim
RUN apt-get install -y tmux
# set bash completion
RUN echo "# enable bash completion" >> ~/.bashrc && \
      echo "if [ -f /etc/bash_completion ] && ! shopt -oq posix; then" >> ~/.bashrc && \
      echo "   . /etc/bash_completion" >> ~/.bashrc && \
      echo "fi" >> ~/.bashrc

