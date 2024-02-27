FROM python:latest
WORKDIR /lab1
COPY degree.py ./
COPY output/ ./output/
RUN pip install python-dotenv
CMD ["python", "./degree.py"]
