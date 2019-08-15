class Options():
    default_options = { 'port' : 21, 'host' : 'localhost', 'username' : None, 'passwrod' : None, 'debug' : False }
    
    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)
        
    def __getitem__(self,key):
        return self.options[key]
