# Library that's check game servers. Just OOP example.

## class name is PingTesterBase.

### Class arguments:
* `game` child library. Available args: ['csgo', 'minecraft']
* `host` ip or domain name of the server. Valid formats is: ['myname.com', 'myname.com:port', 'ip:port', 'ip']
* `port` optional argument, the type is int or str.
* `timeout` optional argument, the type is int or float

## Methods:
* `getServerPing` returns latency or returns -1 if the server is not available.
* `isServerAlive` returns bool value True or False
* `Monitor` sets two attributes: self.game.latency and self.game.is_alive and returns answer from server.
   Can be used instead of getServerPing and isServerAlive.
