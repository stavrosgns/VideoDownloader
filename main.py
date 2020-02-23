"""
@Author: Stavros Gkounis
@Date: 07/02/2020
@Description: This project was created with the aim of creating a intuitive terminal (at least in its first version) program
              for downloading various videos using the youtube-dl python module.

@Version: v1.5
#TODO -ADD: 3) Advance download status handling (if possible) - Metadata Extractor
            4) More Information about What's going on in the background -> It would be great using Threads
            

#TODO -Correct:

#TODO -Improve:
"""

import Downloader
import ViDo

def main():
    vido = ViDo.ViDo()
    tdownloader = Downloader.TDownloader()

    vido.signature()
    tdownloader.tDownload()


if(__name__ == '__main__'):
    main()


