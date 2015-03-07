import urllib
import json

# baseURL = "http://houseboat.bandcamp.com";
# album = "/album/the-delaware-octopus"
# baseFolder = "C:\Users\Max\Music\HouseBoat\the-delaware-octopus\a"
# response = urllib.urlopen(baseURL + album);

baseURL = "http://chamberband.bandcamp.com";
album = "/album/deities"
#baseFolder = "C:\Users\Max\Music\HouseBoat\the-delaware-octopus\a"

response = urllib.urlopen(baseURL + album);


html = response.read();

list = html.split('a href="/track/');
tracks = [];
for i in list:
	track = i.split('"')[0]
	if(len(tracks) ==0 or track != tracks[len(tracks)-1] and track !=( tracks[len(tracks)-1] +'?action=download')):
		tracks.append(track);

tracks.pop(0);

for t in tracks:
	trackURL = baseURL + '/track/' + t;
	r = urllib.urlopen(trackURL);
	page = r.read();
	mp3loc = page.split('{"mp3-128":"');
	mp3URL = mp3loc[1].split('"')[0];
	trackFile = t + '.mp3';
	urllib.urlretrieve(mp3URL,trackFile);
		


