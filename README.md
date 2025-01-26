[![main](https://github.com/inferno681/wb_bot/actions/workflows/main.yaml/badge.svg)](https://github.com/inferno681/wb_bot/actions/workflows/main.yaml)

# WB Collection Bot

Телеграм бот для отслеживания информации о товарах.

<details><summary><h2>Реализованные возможности</h2></summary>
- Получение информации о товаре из бд.
- Запуск загрузки информации о товаре в базу данных.
- Запуск загрузки информации о товаре в базу данных с обновлением каждые 30 минут.
- Остановка обновления информации о товаре в базе данных.
</details>

<details><summary><h2>Запуск проекта</h2></summary>
1. Клонируйте репозиторий, создайте виртуальное окружение и активируйте его.

2. Установите poetry:
```bash
pip install poetry
```
3. Установите зависимости:
```bash
poetry install
```
Можно использовать ключ "--only main", если не нужно запускать тесты или линтеры.

4. Создайте .env файл с токеном:
```
token=
```
5. Все настройки приложения находятся в файле src/config/config.yaml. Измените значение host раздела redis на "localhost".

6. Базу данных можно запустить в контейнере:
```bash
docker compose -f ./infra/docker-compose-dev.yaml up -d
```
7. Запустите приложение:
```bash
export PYTHONPATH=src/
```
```bash
python src/bot/main.py
```
</details>

<details><summary><h2>Запуск проекта через докер</h2></summary>

1. Создайте .env файл с токеном:
```
token=
```
2. Скопируйте файл docker-compose-prod.yaml в директорию с .env файлом.

3. Выполните команду:
```bash
docker compose -f .\docker-compose-prod.yaml up -d
```
</details>

<details><summary><h2>Запуск проекта через докер без загрузки образа</h2></summary>

1. Клонируйте репозиторий, создайте виртуальное окружение и активируйте его.

2. Создайте .env файл с токеном:
```
token=
```
3. Все настройки приложения находятся в файле src/config/config.yaml.

4. Запустите приложение из папки infra:
```bash
docker compose up -d
```
</details>

<details><summary><h2>Преимущества</h2></summary>

- реализовано в соответствии с заданием https://docs.google.com/document/d/12qJvn8WZAxDsFTOGBC2uiaAioIg4x3JF-TvGvq2Povs/edit?tab=t.0

- Там где это необходимо используется конкурентность.

- Реализовано CI/CD.

- Имеется дополнительный функционал соответствующий API.
</details>
