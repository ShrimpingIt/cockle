import ujson as json                                                                         

def loadConfig():
	with open("config.json","r") as f:
		return json.loads(f.readall())
		  
def saveConfig(config):
	with open("config.json","w") as f:
		f.write(json.dumps(config))  

def getConfigValue(name):
	try:
		config = loadConfig()
	except:
		config = {}
	return config[name]

def setConfigValue(name, value):
	try:
		config = loadConfig()
	except:
		config = {}
	config[name]=value
	saveConfig(config)
