# News Service API (db)

Это реализация бэкенд сервиса новостей с REST API на Python с использованием фреймворка FastAPI и SQLAlchemy. 

## Описание

Сервис предоставляет RESTful API, который позволяет:

- Получать список новостей с количеством комментариев.
- Получать конкретную новость по её ID с соответствующими комментариями.
- Добавлять новые новости и комментарии.
- Обрабатывать ситуации, когда новости не существуют или были удалены.

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/eleneaa/NewsServiceDB
```
2. Установите зависимости:
```bash
pip install -r requirements.txt
```

### Использование

1. Запустите сервер:

```bash
uvicorn main:app --reload
```

2. Просмотреть возможные запросы можно по адресу: http://127.0.0.1:8000/docs#


### Эндпоинты

1. **GET `/`**: Получает список новостей с комментариями.

   **Ответ:**
   ```json
   {
     "news": [
       {
         "id": 1,
         "title": "news_1",
         "date": "2024-01-01T20:56:35",
         "body": "The news",
         "deleted": false,
         "comments_count": 1
       }
     ],
     "news_count": 1
   }
   ```

2. **GET `/news/{id}`**: Получает новость по её ID.

   **Параметры:**
   - `id`: ID новости, которую нужно получить.

   **Ответ при успешном запросе:**
   ```json
   {
     "id": 1,
     "title": "news_1",
     "date": "2024-01-01T20:56:35",
     "body": "The news",
     "deleted": false,
     "comments": [
       {
         "id": 1,
         "news_id": 1,
         "title": "comment_1",
         "date": "2024-01-02T21:58:25",
         "comment": "Comment"
       }
     ],
     "comments_count": 1
   }
   ```

   **Ошибка 404:** Если новость не найдена или была удалена.

3. **POST `/news`**: Добавляет новую новость.

   **Тело запроса:**
   ```json
   {
    "title": "News1",
    "date": "2025-03-20T15:20:31.955Z",
    "body": "news body 1"
    }
   ```

   **Ответ:**
   ```json
   {
    "id": 1,
    "title": "News1",
    "body": "news body 1",
    "date": "2025-03-20T15:20:31.955000+00:00"
    }
   ```

4. **POST `/comment`**: Добавляет новый комментарий к новости.

   **Тело запроса:**
   ```json
   {
    "news_id": 1,
    "title": "string1",
    "comment": "string1"
    }
   ```

   **Ответ:**
   ```json
   {
    "id": 1,
    "title": "string1",
    "comment": "string1",
    "news_id": 1
    }
   ```
