from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8015  # Порт для доступа по сети


def get_index(path):
    if path == '':
        path = 'index.html'
    return open(path, 'r', encoding='utf-8').read()

class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов

    """
    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        parsed_url = urlparse(self.path)
        file_path = parsed_url.path.strip('/')
        page_content = get_index(file_path)
        self.send_response(200)  # Отправка кода ответа
        self.send_header(
            "Content-type", "text/html"
        )  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, 'utf-8'))  # Тело ответа


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети.
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше.
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш (Ctrl + C)
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал.
    webServer.server_close()
    print("Server stopped.")