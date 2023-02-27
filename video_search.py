from pytube import Search
#link = input("Enter URL=")
#video=pytube.YouTube(link)
#video.streams.first().download() #This controls the video quality of the stream
#video.streams.filter(progressive=True,file_extension='mp4')#Use this to further filter out the video
#video.streams.get_by_resolution("720p").download()
# See the url https://pytube.io/en/latest/api.html#stream-object for assitance
#print("Download Link =",link)
s=Search("Linus")
print(len(s.results))