from bing_image_downloader import downloader
import wikipedia

def lrn():
    inp = input("Enter : ")
    downloader.download(inp, limit = 5, output_dir = 'objects')
    result = str(wikipedia.summary(inp, sentences=2))
    dir = "objects/"
    dir+=inp
    dir+="/data.txt"
    topic = open(dir, "w")
    topic.write('\n')
    topic.write(result)
    topic.close()