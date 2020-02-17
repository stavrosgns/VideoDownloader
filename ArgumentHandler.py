import argparse

class ArgumentHandler:
    
    def listArguments(self):
        """
        @Description: This method informs the user about the possible options he / she can choose
        @Parameters: None
        @Return: The terminal arguments with their values
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        parser = argparse.ArgumentParser(description="Options To Bypass Interaction With The Script During Its Execution")
        
        parser.add_argument('-u', '--single-url', dest='singleUrl', action='store', help="Provide Only One URL")
        parser.add_argument('-U', '--multiple-url', dest='multipleUrl', action="store_true", help="Provide Multiple URLs In The Script")
        parser.add_argument('-f', '--file', dest='filename', action='store', help="Provide A File With URLs")
        parser.add_argument('-J', '--just-video', dest='justVideo', action="store_true", help="Use This Option If You Want Only To Download The Video (Default)")
        parser.add_argument('-A', '--audio', dest='toAudio', action="store_true", help="Use This Option If You Want To Convert The Video To MP3")
        parser.add_argument('-i', '--interactive', dest='interactive', action="store_true", help="If You Use This Option, The Script Will Ask All The Questions That It needs To Operate Successfully")

        args = parser.parse_args()
        return args


