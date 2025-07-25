import argparse
import json
from tabulate import tabulate # для красивой таблицы
from collections import defaultdict # удобно для группировки
from datetime import datetime

parser = argparse.ArgumentParser(description="Простой анализ логов")
parser.add_argument('--file', nargs='+', required=True, help='Путь к логам можно несколько')
parser.add_argument('--report', required=True, choices=['average'], help='Название отчета  average')
parser.add_argument('--date', required=False, help='Фильтрация по дате формат такой YYYY-MM-DD')
args = parser.parse_args()

logs = []

for filename in args.file:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                    if args.date:
                        entry_date = entry.get("timestamp", "").split("T")[0]
                        if entry_date != args.date:
                            continue
                    logs.append(entry)
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        print(f"Файла нет {filename}")

stats = defaultdict(list)

for log in logs:
    endpoint = log.get("endpoint")
    response_time = log.get("response_time")
    if endpoint and isinstance(response_time, (int, float)):
        stats[endpoint].append(response_time)

report_data = []

for endpoint, times in stats.items():
    count = len(times)
    avg = sum(times) / count if count else 0
    report_data.append([endpoint, count, round(avg, 2)])

report_data.sort(key=lambda x: x[1], reverse=True)

print(tabulate(report_data, headers=["Endpoint", "Requests", "Avg. Time"], tablefmt="pretty"))
