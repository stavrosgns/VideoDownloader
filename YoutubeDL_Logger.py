class YoutubeDL_Logger(object):
    def debug(self,msg):
        pass

    def warning(self,msg):
        print("[!] Warning: {}".format(msg))
    
    def error(self,msg):
        print("[ :( ] ERROR: {}".format(msg))
    
