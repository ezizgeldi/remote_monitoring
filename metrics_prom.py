from flask import Flask
from prometheus_client import start_http_server, Gauge
import psutil
import time

app = Flask(__name__)

# Определение метрик Prometheus
cpu_gauge = Gauge('cpu_usage', 'CPU Usage')
ram_gauge = Gauge('ram_usage', 'RAM Usage')

def collect_metrics():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        cpu_gauge.set(cpu_usage)
        ram_gauge.set(ram_usage)
        time.sleep(1)

@app.route('/')
def metrics():
    return "Metrics endpoint available at /metrics"

if __name__ == '__main__':
    # Запуск HTTP сервера для метрик
    start_http_server(8000)
    # Запуск сбора метрик
    collect_metrics()
