# Лог Анализатор

Это простой проект для анализа логов в формате JSON.  
Можно узнать сколько запросов было на каждый endpoint и какое у них было среднее время ответа.

## Как пользоваться

1. Клонируй проект или просто открой в папке
2. Установи зависимости (например tabulate)
3. Запусти через терминал так:

```
python main.py --file log.json --report average
```

Можно указать сразу несколько файлов и добавить фильтр по дате:

```
python main.py --file log1.json log2.json --report average --date 2024-07-01
```

## Что показывает

Программа выводит таблицу с endpoint'ами, сколько было запросов и сколько в среднем длился каждый.


## Для чего это

Чтобы быстро посмотреть что происходит в логах и где тормозит сервер.
