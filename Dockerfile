FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install pydantic

CMD ["python", "baseline_agent.py"]
