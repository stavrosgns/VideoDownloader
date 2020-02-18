import Navigator
import User
import ArgumentHandler
import YoutubeDL_Logger
import youtube_dl # <- The core module where the whole script is based on

class Downloader:
    """
    @Description: This class is useful in interactive mode
    @Name: Downloader
    @Author: Stavros Gkounis (Steve Gkounis)
    """

    def _downloadAndConverterProgressStatus(self, d):
        """
        @Description: This function acts a progress hook that informs the user that the download has been completed
                      and the converting progress is about to start
        @Parameters: d is a array that includes some metadata as 'status'
        @Return: Nothing
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        if(d['status'] == 'finished'):
            print("[*] Downloading --> DONE")
            print("[*] Converting --> IN PROGRESS")
    
    def _progressStatus(self, d):
        """
        @Description: This function acts a progress hook that informs the user that the download has been completed
        @Parameters: d:: a array that includes some metadata as 'status'
        @Return: Nothing
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        if(d['status'] == 'finished'):
            print("[*] Downloading --> DONE")
    
    def _downloadAndConvert2Mp3(self, url):
        """
        @Description: This function is responsible for downloading and converting the video into a MP3 audio file
        @Parameter: url:: string, the url of the video
        @Return: Nothing
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        try:
            ydl_options = {
                'format' : 'bestaudio/best',
                'postprocessors' : [{
                    'key' : 'FFmpegExtractAudio',
                    'preferredcodec' : 'mp3',
                    'preferredquality' : '192'
                }],
                'logger' : YoutubeDL_Logger.YoutubeDL_Logger(),
                'progress_hooks' : [self._downloadAndConverterProgressStatus]
            }

            with youtube_dl.YoutubeDL(ydl_options) as downloader:
                downloader.download([url])
        
        except:
            print("[!] An Error occured during the execution. It seems that youtube_dl itself is responsible")
            print("[ :) ] Please check if there is a more recent version of youtube_dl available and upgrade to that version")
    
    def _downloadVideo(self, url):
        """
        @Description: This function is responsible for downloading the desired video
        @Parameter: url:: string, the url of the video
        @Return: Nothing
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        try:
            ydl_options = {
                'format': 'best',
                'logger': YoutubeDL_Logger.YoutubeDL_Logger(),
                'progress_hooks' : [self._progressStatus]
            }

            with youtube_dl.YoutubeDL(ydl_options) as downloader:
                downloader.download([url])
        except:
            print("[!] An Error occured during the execution. It seems that youtube_dl itself is responsible")
            print("[ :) ] Please check if there is a more recent version of youtube_dl available and upgrade to that version")

    
    def downloadSingleURL(self, downloading_options, url):
        """
        @Description: This function uses the Navigator module for filesystem actions and according to user choice
                      it downloads only the video or converts it into a MP3 audio file
        
        @Parameter: downloading_options:: array with two members which represent whether the user want just the video
                                          or to convert it into a MP3 file
        
                    url :: string, the URL of video
        
        @Return: Nothing
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        navigator = Navigator.Navigator()

        if(downloading_options[1] == '1'):
            navigator.changeToVideosFolder()
            self._downloadVideo(url)
        elif(downloading_options[1] == '2'):
            navigator.changeToMusicFolder()
            self._downloadAndConvert2Mp3(url)
    
    def downloadMultipleURLs(self, downloading_options, urls):
        """
        @Description: This function uses the Navigator module for filesystem actions and according to user choice
                      it downloads only the multiple videos or converts them into a MP3 audio file
        
        @Parameter: downloading_options:: array with two members which represent whether the user want just the videos
                                          or to convert them into a MP3 file
        
                    urls :: array of multiple URLs
        
        @Return: Nothing
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        navigator = Navigator.Navigator()

        if(downloading_options[1] == '1'):
            navigator.changeToVideosFolder()
            for url in urls:
                self._downloadVideo(url)
        elif(downloading_options[1] == '2'):
            navigator.changeToMusicFolder()
            for url in urls:
                self._downloadAndConvert2Mp3(url)

    
    def download(self):
        """
        @Description: This function ask the user if he / she wants to download just a video, multiple videos or have a file of URLs to be downloaded
                      and according to their choice this method uses the proprer methods to download the video(s).
        @Parameter: None
        @Return : Nothing
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        try:
            user = User.User()
            downloading_options = user.askForDownloadingOptions()

            if(downloading_options[0] == '1'):
                url = user.askForUrl() 
                self.downloadSingleURL(downloading_options, url)
            elif(downloading_options[0] == '2'):
                urls = user.askForMultipleUrl()
                self.downloadMultipleURLs(downloading_options, urls)
            elif(downloading_options[0] == '3'):
                urls = user.askForFileWithUrls()
                self.downloadMultipleURLs(downloading_options, urls)
        except KeyboardInterrupt:
            print("[!] Script was interrupted by the user")

class TDownloader(Downloader):
    """
    @Description: This class is useful when the user gives terminal arguments
    @Name: TDownloader
    @Author: Stavros Gkounis (Steve Gkounis)
    """
    
    def tDownloadSingleURL(self, justVideo, toAudio, url):
        """
        @Description: This function downloads the desired video or converts it into a MP3 audio file, according to user's choice
        @Parameter: justVideo:: boolean, True if user wants to download just the video
                    toAudio:: boolean, True if user wants to convert the video into a MP3 audio file
                    url:: string, the URL of the desired video
        
        @Return: Nothing
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        navigator = Navigator.Navigator()

        if((justVideo == True) and (toAudio == False)):
            navigator.changeToVideosFolder()
            self._downloadVideo(url)
        elif((justVideo == False) and (toAudio == True)):
            navigator.changeToMusicFolder()
            self._downloadAndConvert2Mp3(url)
        else:
            print("[!] Please Select Either '-J' or '-A'")
        
    def tDownloadMultipleURLs(self, justVideo, toAudio, urls):
        """
        @Description: This function downloads the desired videos or converts them into a MP3 audio file, according to user's choice
        @Parameter: justVideo:: boolean, True if user wants to download just the videos
                    toAudio:: boolean, True if user wants to convert the videos into a MP3 audio file
                    urls:: array of multiple URLs of the desired videos
        
        @Return: Nothing
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        navigator = Navigator.Navigator()

        if((justVideo == True) and (toAudio == False)):
            navigator.changeToVideosFolder()
            for url in urls:
                self._downloadVideo(url)
        elif((justVideo == False) and (toAudio == True)):
            navigator.changeToMusicFolder()
            for url in urls:
                self._downloadAndConvert2Mp3(url)
        else:
            print("[!] Please Select Either '-J' or '-A'")
    
    
    def tDownload(self):
        """
        @Description: This function handles the arguments that the user gives using the ArgumentHandler Module and according them the process of
                      downloading starts
        @Parameter: None
        @Return: Nothing
        @Author: Stavros Gkounis (Steve Gkounis)
        """
        try:
            argsHandler = ArgumentHandler.ArgumentHandler()
            user = User.User()
            navigator = Navigator.Navigator()

            args = argsHandler.listArguments()
            if(args.singleUrl is not None):
                self.tDownloadSingleURL(args.justVideo, args.toAudio, args.singleUrl)
            elif((args.singleUrl is None) and (args.multipleUrl == True)):
                urls = user.askForMultipleUrl()
                self.tDownloadMultipleURLs(args.justVideo, args.toAudio, urls)
            elif((args.singleUrl is None) and (args.multipleUrl == False) and (args.filename is not None)):
                urls = navigator.dealWithTheFileOfURLs(args.filename)
                self.tDownloadMultipleURLs(args.justVideo, args.toAudio, urls)
            elif(args.interactive == True):
                self.download()
            else:
                print("[!] You have to specify '-u' or '-U' or '-f'. For help use the '-h' option")
        except KeyboardInterrupt:
            print("[!] Script was interrupted by the user")