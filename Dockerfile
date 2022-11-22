FROM python:3.9.7
WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY .streamlit/config.toml /root/.streamlit/config.toml
COPY .streamlit/secrets.toml /root/.streamlit/secrets.toml
RUN pip install -r requirements.txt

COPY . /app
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]      
  
