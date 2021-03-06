import json
import socket

import os

from Base.common import deprint


class Dealer:
    _client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    _client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_sock_path = '/tmp/shadowsocks-client.sock'
    try:
        os.remove(client_sock_path)
    except FileNotFoundError as err:
        pass
    _client.bind(client_sock_path)
    try:
        _client.connect('/var/run/shadowsocks-manager.sock')
    except FileNotFoundError as err:
        pass

    @classmethod
    def _send(cls, data):
        cls._client.send(data.encode())

    @classmethod
    def add_port(cls, port, password):
        # deprint('add port debug')
        # return
        data = {
            'server_port': port,
            'password': password,
        }
        data_str = json.dumps(data)
        deprint(data_str)
        cls._send('add: %s' % data_str)

    @classmethod
    def remove_port(cls, port):
        # deprint('remove port debug')
        # return
        data = {
            'server_port': port,
        }
        data_str = json.dumps(data)
        deprint(data_str)
        cls._send('remove: %s' % data_str)
