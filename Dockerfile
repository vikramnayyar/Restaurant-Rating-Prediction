FROM python:3.7
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --upgrade pip
# RUN conda uninstall numpy
# RUN conda uninstall tornado 
RUN pip install -r requirements.txt 
# CMD python app/flask-app.py
CMD streamlit run app/app.py