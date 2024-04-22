FROM python:3.12

RUN pip install poetry

COPY . .

RUN poetry install

ENTRYPOINT ["poetry", "run", "uvicorn" , 'simple_book_api.main:app' , '--port' , '8000']