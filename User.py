import Navigator

class User:

    def askForUrl(self):
        """
        @Description: This function asks the user for a single URL
        @Parameters: None
        @Return: Returns the user's single URL
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        video_url = input("[*] Give the URL: ")
        return video_url

    def askForMultipleUrl(self):
        """
        @Description: This function asks the user for multiple URLs to be downloaded
        @Parameters: None
        @Return: An array of URLs
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        urls = []
        video_url = ''
        RUDONE= False
        while(not RUDONE):
            video_url = input("[*] Give multiple URLs (For exit press enter or type q): ")
            urls.append(video_url)
            if(video_url == '' or video_url == 'q'):
                RUDONE = True
                del urls[len(urls) - 1] # Removes the '' or 'q' that the user enters when he breaks the loop
        
        return urls
    
    def askForFileWithUrls(self):
        """
        @Description: This function ask the user for the file which contains the URLs to be downloaded
        @Parameters: None
        @Return: An array of URLs
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        navigator = Navigator.Navigator() # Responsible for filesystem actions

        urls = []
        path = input("[*] Give the path of the file or the filename: ")
        if(navigator.checkValidityOfFile(path)):
            with open(path,'r') as urlFile:
                for url in urlFile:
                    urls.append(url)
            return urls
        else:
            print("[!] File Validity -> FAILED")
            print("[!] Please check that the path is correct")

    def askForDownloadingOptions(self):
        """
        @Description: This function is useful only in interactive mode. It asks the user if he / she wants to give a single or multiple URLs or a file of URLs
        @Parameters: None
        @Return: An array with two records. In the first place there is the answer regarding to the URLs and
                                           In the second place there is the answer regarding to 'how the download will occur
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        user_choice = [None, None]
        url_option = input("[*] Please choose one of the options regarding to url:\n\t1: URL\t2: Multiple URLs\n\t3: File With URLs\n: ")
        downloading_option = input("\n[*] Please choose one of the downloading options:\n\t1: Just Download The Video\n\t2: Download and Convert The Video To MP3\n: ")

        user_choice[0] = url_option ; user_choice[1] = downloading_option
        return user_choice