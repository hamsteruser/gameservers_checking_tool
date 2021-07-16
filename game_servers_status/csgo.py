#!/usr/bin/env python
import socket
import time


class TargetGame(object):    
    def __init__(self, host: str, port: int, timeout: float):
        self.is_alive = False
        self.host = host
        if port:
            self.port = int(port)
        else:
            self.port = 27015 #Default CS:GO UDP port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(timeout)
        self.sock.connect((self.host, self.port))


    def server_monitoring(self) -> object:
        ''' UDP nothing returns if server is unavailable '''
        string = b'\377\377\377\377TSource Engine Query\0'
        time_start = time.time()
        self.sock.send(string)
        try:
            text = self.sock.recv(4096)
            self.latency = time.time()-time_start
            self.is_alive = True
        except Exception as err:
            self.latency = -1
            self.is_alive = False
            text = "There is no answer from server"
        return text


    def get_server_ping(self) -> float:
        self.server_monitoring()
        return self.latency
        
        
    def is_server_alive(self) -> bool:
        self.server_monitoring()
        return self.is_alive
    
        
    def __del__(self):
        self.sock.close()    
    