import importlib

class PingTesterBase():
    ''' Init module imports a file that is match the "game" argument '''
    def __init__(self, game, host, port=None, timeout=10):        
        if ":" in host:
            _host = host.split(':')[0]
            port = int(host.split(':')[1])
        else:
            _host = host
        self.game = __import__(game, globals(), level=1).TargetGame(_host, port, timeout)
        
    
    def getServerPing(self, *args, **kwargs):
        return self.game.get_server_ping(*args, **kwargs)
        
    
    def isServerAlive(self, *args, **kwargs):
        return self.game.is_server_alive(*args, **kwargs)
        

    def Monitor(self, *args, **kwargs):
        ''' Creates two attributes: self.game.latency and self.game.is_alive and returns answer from server
            Can be used instead of getServerPing and  isServerAlive          '''
        return self.game.server_monitoring(*args, **kwargs)
        
        
    def __del__(self):
        del(self.game)
    