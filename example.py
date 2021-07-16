from game_servers_status import PingTesterBase

lat = PingTesterBase(game="csgo", host="216.52.148.47", port=27015, timeout=5).getServerPing()
print(lat)

ptb = PingTesterBase(game="csgo", host="216.52.148.47", port=27015, timeout=5)
isAlive = ptb.isServerAlive()
latency = ptb.getServerPing()
print(latency)
print(isAlive)
print(ptb.game.latency)
print(ptb.game.is_alive)
print(ptb.Monitor())
del(ptb)


ptb = PingTesterBase(game="csgo", host="216.52.148.47:27015", timeout=5)
isAlive = ptb.isServerAlive()
latency = ptb.getServerPing()
print(latency)
print(isAlive)
print(ptb.game.latency)
print(ptb.game.is_alive)
print(ptb.Monitor())
del(ptb)


ptb = PingTesterBase(game="csgo", host="216.52.148.47", timeout=5)
isAlive = ptb.isServerAlive()
latency = ptb.getServerPing()
print(latency)
print(isAlive)
print(ptb.game.latency)
print(ptb.game.is_alive)
print(ptb.Monitor())
del(ptb)


ptb = PingTesterBase(game="minecraft", host="server.minesuperior.com", timeout=5)
isAlive = ptb.isServerAlive()
latency = ptb.getServerPing()
print(latency)
print(isAlive)
print(ptb.game.latency)
print(ptb.game.is_alive)
print(ptb.Monitor())
del(ptb)


ptb = PingTesterBase(game="csgo", host="8.8.8.8", port=27015, timeout=5)
isAlive = ptb.isServerAlive()
latency = ptb.getServerPing()
print(latency)
print(isAlive)
print(ptb.game.latency)
print(ptb.game.is_alive)
print(ptb.Monitor())
del(ptb)


ptb = PingTesterBase(game="minecraft", host="8.8.8.8", timeout=5)
isAlive = ptb.isServerAlive()
latency = ptb.getServerPing()
print(latency)
print(isAlive)
print(ptb.game.latency)
print(ptb.game.is_alive)
print(ptb.Monitor())
del(ptb)