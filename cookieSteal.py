#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import threading


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print("")
        print("%s - %s\t%s" % (
            datetime.now().strftime("%Y-%m-%d %I:%M %p"),
            self.client_address[0],
            self.headers['user-agent']))
        print("-------------------" * 6)
        for k, v in list(query_components.items()):
            print("%s\t\t\t%s" % (k.strip(), v))

        return

    def log_message(self, format, *args):
        return


class HTTPServerThread(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.server = HTTPServer((host, port), MyHandler)
        self.running = threading.Event()

    def run(self):
        self.running.set()
        print(f'Started http server at {self.host}:{self.port}')
        self.server.serve_forever()

    def stop(self):
        if self.running.is_set():
            self.server.shutdown()
            self.running.clear()
            print(f'Stopped http server at {self.host}:{self.port}')


def start_server(host, port):
    server_thread = HTTPServerThread(host, port)
    server_thread.start()
    return server_thread


def stop_server(server_thread):
    if server_thread:
        server_thread.stop()
        server_thread.join()


def print_help():
    print("Available commands:")
    print("  start <host> <port>: Start the HTTP server")
    print("  stop: Stop the HTTP server")
    print("  exit: Exit the CLI")
    print("  help: Print this help message")


def main():
    server_thread = None

    print("Welcome to HTTP Server CLI!")
    print_help()

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "start":
            print("Usage: start <host> <port>")
        elif command.startswith("start "):
            _, host, port_str = command.split(" ", 2)
            try:
                port = int(port_str)
                if server_thread and server_thread.running.is_set():
                    print("Server is already running. Please stop it first.")
                else:
                    server_thread = start_server(host, port)
            except ValueError:
                print("Invalid port number. Please enter a valid integer.")
        elif command == "stop":
            stop_server(server_thread)
            server_thread = None
        elif command == "exit":
            if server_thread and server_thread.running.is_set():
                stop_server(server_thread)
            break
        elif command == "help":
            print_help()
        else:
            print("Invalid command. Type 'help' for available commands.")


if __name__ == "__main__":
    main()
