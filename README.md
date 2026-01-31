# Запуск проекта

## Установка и настройка виртуального окружения
```bash
python -m venv venv  #1
```
**Что делает:**
- Создает виртуальное окружение Python в папке `venv`. Это изолирует зависимости проекта от глобальных пакетов.

## Активация окружения
```bash
# Windows:
source venv/Scripts/activate #2
# Linux/Mac:
source venv/bin/activate
```
**Что делает:**  
- Активирует виртуальное окружение. После активации в терминале появится `(venv)`.

## Установка зависимостей
```bash
pip install -r requirements.txt  #3
```
**Что делает:**  
- Устанавливает все пакеты из файла `requirements.txt` (Django и др.).

## Миграции базы данных
```bash
python manage.py makemigrations #4
python manage.py migrate  #5
```
**Что делает:**  
- `makemigrations` — создает файлы миграций на основе моделей Django.  
- `migrate` — применяет миграции к базе данных.

## Создание суперпользователя (опционально)
```bash
python manage.py createsuperuser
```
**Что делает:**  
- Создает администратора для доступа к панели Django (`/admin`).

 - git commit -m 'commit' 
 заливает коммит

 git clone "ссылку с гита"