from pytube import YouTube, Playlist
import sys

SAVE_PATH = {"Videos": "YouTube" , "Playlist":"YouTubePlay"}
SAVE_PATHVideos = "YouTub"

#link of the video to be downloaded

if len(sys.argv) != 2 :
    exit()

#links= ["https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI"]

links = []
links.append(sys.argv[1])

def LetsDownload(SAVE_PATH):

	# object creation using YouTube which was imported in the beginning
	yt = YouTube(link)
	d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
	outfileName = d_video.download(SAVE_PATH)
	titleName = yt.title
	return outfileName, titleName
n=0

for link in links:

	if "playlist" in link:

		playlist = Playlist(link)
		PlaylistPath= SAVE_PATH["Playlist"]

		PlayListLinks = playlist.video_urls
		N = len(PlayListLinks)
		#print('Number of videos in playlist: %s' % len(PlayListLinks))

		print(f'This link found to be a Playlist "{playlist.title}" with number of videos equal to {N} ')
		print(f"\n Lets Download all {N} videos")

		for i,link in enumerate(PlayListLinks):

			outfileName, titleName = LetsDownload("Playlist_"+ playlist.title)

			print(i+1, '.', titleName,' is Downloaded.')

	else:
		VideosPath= SAVE_PATH["Videos"]

		print("This link found to be a Video Link")

		outfileName, titleName = LetsDownload(SAVE_PATH["Videos"])
		n=n+1
		print(n, '.', titleName, '  Video is Downloaded.')
