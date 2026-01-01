FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

# --- ADD THIS LINE TO DEBUG ---
RUN find . -name "manage.py"
# ------------------------------

EXPOSE 8000

# If your manage.py is in a subfolder, you must point to it here
# Example if it's in 'my_site/manage.py':
# CMD ["python", "my_site/manage.py", "runserver", "0.0.0.0:8000"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
