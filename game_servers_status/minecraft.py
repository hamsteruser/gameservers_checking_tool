#!/usr/bin/env python
from mcstatus import MinecraftServer


class TargetGame(object):    
    def __init__(self, host: str, port: int, timeout: int):
        self.is_alive = False
        if port:
            self.hostname = f"{host}:{port}"
        else:
            self.hostname = host
        self.timeout = int(timeout)
        self.server = MinecraftServer.lookup(self.hostname)


    def server_monitoring(self) -> object:
        ''' UDP nothing returns if server is unavailable '''
        try:
            r = self.server.status(tries=self.timeout)            
            self.latency = r.latency/1000
            self.is_alive = True
            text = r.description
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
        pass   
    