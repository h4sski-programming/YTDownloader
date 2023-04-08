from pytube import YouTube
import os

def ytdownloader():
    print('Welcome to YTDownloader.')
    input_txt = 'input.txt'
    output_url = 'download/'
    output_txt = 'output.txt'
    
    with open(file=input_txt, mode='r') as input_file:
        urls = input_file.readlines()
        for url in urls:
            url = url.strip()
            
            try:
                yt = YouTube(url)
            except Exception:
                print('YouTube not found content based on url: {url}. Please check the link.\n')
                # print(yt.title)       # for debur purpouse
            
            try:
                stream = yt.streams.filter(only_audio=True)
            except Exception:
                print('Stream not found based on url: {url}. Title of this stream is: {yt.title}.\n')
                # print(yt.title, stream[0])       # for debur purpouse
            stream[0].download(output_path=output_url, filename=yt.title+'.mp3')
            print(yt.title)
            
            write_output(file_url=output_txt, url_string=url)
            
            

def write_output(file_url, url_string):
    with open(file_url, 'a') as output_file:
        output_file.write(url_string + os.linesep)


if __name__ == '__main__':
    ytdownloader()