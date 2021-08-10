## Сайт знакомств

Бекэнд для сайта Meeting_website(сайт знакомств) имеет следующие возможности:

1) Регистрация пользователя с указанием полей имени, фамилия, email, пола, личной фотографии и местоположения
2) При регистрации вычисляется удаленность нового пользователя от всех зарегистрированных пользователей
3) Также при на личное фото пользователя накладывается водяной знак
4) Авторизация участника 
5) Реализован функционал оценивания пользователя другим пользователем, а при взаимной симпатии, уведомление обоих по почте.
6) Реализовано получения списка участников по следующим фильтрам (удаленность от авторизанного участника, имя, фамилие, пол)

# Описание API

В headers необходимо передавать ключ во всех api запросах

HEADERS
```
API-SECURE-KEY:       # Ключ безопасности(строка)
```

#### POST /trainees/api/clients/create

Регистрация нового пользователя

Тело запроса: multipart/form-data
```
name        # Имя пользователя(строка)
surname     # Фамилие пользователя(строка)
email       # Email пользователя(строка)
gender      # Пол пользователя, необходимо указать букву F или M (строка)
password    # Пароль пользователя(строка)
password2   # Повторение пароля пользователя для соответствия(строка)
latitude    # Географическая широта места нахождения пользователя(строка)
longitude   # Географическая долгота места нахождения пользователя(строка)
avatar      # Личное фото пользователя(файл)
```
Тело ответа:
```
{
    "result": "User created successfully"
}
```

#### POST /trainees/api/auth/login

Авторизация пользователя 

Тело запроса: multipart/form-data
```
email       # Email пользователя(строка)
password    # Пароль пользователя(строка)
```
Тело ответа:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyODY5MDE5MiwianRpIjoiM2IxNWFjOWJiNjQ3NDZjMWI5ZWEwZmU1ODkxOWFhNWQiLCJ1c2VyX2lkIjozLCJlbWFpbCI6ImNAZ21haWwuY29tIn0.z5mNCHWfJQlF6pKZnEOllX-CrjPsUcHLvaMJuHBmJok",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI4NjA0MDkyLCJqdGkiOiJkZTI5YTA0YzY1NmI0ZTdmOWFiN2IzYTk2MTBiZjEyNSIsInVzZXJfaWQiOjMsImVtYWlsIjoiY0BnbWFpbC5jb20ifQ.rpHdL-xhyY7wH1lwS_GfLiWyhdWgyqYJRn5lfNxXcc0"
}
```

#### GET /trainees/api/list

Получение списка пользователей с фильтрами

Необходимо передавать токен авторизанного пользователя

Тело запроса: multipart/form-data
```
gender      # Пол пользователя, необходимо указать букву F или M (строка, опционально)
name        # Имя пользователя(строка, опционально)
surname     # Фамилие пользователя(строка, опционально)
distance    # Расстояние до участников(строка, опционально)
```
Тело ответа:
```
[
    {
        "id": 2,
        "name": "Sasha",
        "surname": "Ivanova",
        "email": "sivanov@gmail.com",
        "gender": "M",
        "avatar": "/media/user_avatars/0_5F2pXZ6.jpg",
        "longitude": "37.6156",
        "latitude": "55.7522"
    },
    {
        "id": 1,
        "name": "Masha",
        "surname": "Petrova",
        "email": "mpetrova@gmail.com",
        "gender": "F",
        "avatar": "/media/user_avatars/0_hBAUSoi.jpg",
        "longitude": "39.7257",
        "latitude": "43.5992"
    }
]
```

#### POST /clients/(user_id)/match

Оценивание участника другим участником 

Необходимо передавать токен авторизанного пользователя


Тело ответа 1:
```
{
    "result": "Liked"
}
```
Тело ответа 2:
```
{
    "result": "Already liked"
}
```
Тело ответа 3:
```
{
    "result": "Mutual sympathy",
    "email": "mpetrova@gmail.com"
}
```

#### Развернуть проект локально

Ссылка на репозиторий [Gitlab](https://github.com/Zeroitman/Meeting_website)

Установите python на ваш пк [Python](https://www.python.org/downloads/)

Установите пакет менеджер [pip](https://pip.pypa.io/en/stable/)

Установка:
- Склонировать проект из репозитория
- Зайдите в папку проекта и создайте виртуальное окружение c помощью команды 
```bash
sudo pip install virtualenv
```
- В папке проекта пропишите в консоли команду для установки виртуального окружения:
```bash
virtualenv -p python3.7 venv
```
- После установки можно будет активировать виртуальное окружение:
```bash
source venv/bin/activate
```
- Установите все зависимости проекта:
```bash
pip install -r requirements.txt
```
- Проведите миграции:
```bash
./manage.py migrate
```

- В файле config.env, который находится в папке conf замените переменные окружения на свои.
```
Запустите проект:
```bash
./manage.py runserver
```
- Для останоки проекта:
```bash
CTRL + C
```
