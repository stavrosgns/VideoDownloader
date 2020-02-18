import os

class Navigator:
    
    def checkValidityOfFile(self, path):
        """
        @Description: This method takes the path name or the file name and checks if it exists
        @Parameter: path:: string
        @Return: True if the path or file name exists / it's valid, otherwise returns False
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        if(os.path.exists(path)):
            return True
        return False
    
    def changeToVideosFolder(self):
        """
        @Description: This method changes the current working directory (cwd) to $HOME/Video
        @Parameters: None
        @Return: Nothing
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        user_home = os.path.expandvars("$HOME")
        base_path = os.path.join(user_home, 'Videos')

        if(self.checkValidityOfFile(base_path)):
            os.chdir(base_path) # -> You are in ~/Videos now
        else:
            print("[!] I couldn't move to $HOME/Videos")
            print("[ :) ] Are you sure that there is a directory named Videos in your home directory? OR\nAre you sure that the enviroment variable $HOME is defined?")
    
    def changeToMusicFolder(self):
        """
        @Description: This method changes the current working directory (cwd) to $HOME/Music
        @Parameters: None
        @Return: Nothing
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        user_home = os.path.expandvars("$HOME")
        base_path = os.path.join(user_home, 'Music')

        if(self.checkValidityOfFile(base_path)):
            os.chdir(base_path) # -> You are in ~/Music now
        else:
            print("[!] I couldn't move to $HOME/Music")
            print("[ :) ] Are you sure that there is a directory named Music in your home directory? OR\nAre you sure that the enviroment variable $HOME is defined?")
    
    def dealWithTheFileOfURLs(self, filename):
        """
        @Description: This method takes the filename from the terminal arguments that the user provides, checks if that file of URLs exists and returns an array of URLs
        @Parameters: filename:: string, terminal argument
        @Return: An array of URLs
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        urls = []
        if(self.checkValidityOfFile(filename)):
            with open(filename, 'r') as urlFile:
                for url in urlFile:
                    urls.append(url)
            return urls
        else:
            print("[!] File Validity -> FAILED")
            print("[!] Please check if the path name is correct")