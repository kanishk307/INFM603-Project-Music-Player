
/*
	Initializes AmplitudeJS
*/Amplitude.init({
	"bindings": {
		37: 'prev',
		39: 'next',
		32: 'play_pause'
	  },
	  "songs": [
   {
      "name":"Freedom",
      "artist":"Mama Sun System",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Mama_Sun_System_-_Freedom.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s182/182336/covers/1.300.jpg?du=1548469153",
      "duration":"04:45",
      "Category_type":"Reggae"
   },
   {
      "name":"Take Control",
      "artist":"Deezy",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/DEEZY_-_DEEZY-TAKE_CONTROL.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1666/1666442/covers/1.300.jpg?du=1562116723",
      "duration":"03:43",
      "Category_type":"Reggae"
   },
   {
      "name":"Pick Me Up",
      "artist":"Blackship",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Black_Ship_-_Pick_me_up.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1352/1352590/covers/1.300.jpg?du=1529884331",
      "duration":"04:04",
      "Category_type":"Reggae"
   },
   {
      "name":"Harmony",
      "artist":"Dr Groove Gang",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/DR_GROOVE_GANG_-_harmony.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1528/1528680/covers/1.300.jpg?du=1538325413",
      "duration":"03:27",
      "Category_type":"Reggae"
   },
   {
      "name":"Palm Trees",
      "artist":"Ridgway",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Ridgway_-_Palm_Trees.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s163/163960/covers/1.300.jpg?du=1529731969",
      "duration":"04:00",
      "Category_type":"Reggae"
   }
]
	});



var songsobj = {	
		"songsinobj" :  
		[
   {
      "name":"Freedom",
      "artist":"Mama Sun System",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Mama_Sun_System_-_Freedom.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s182/182336/covers/1.300.jpg?du=1548469153",
      "duration":"04:45",
      "Category_type":"Reggae"
   },
   {
      "name":"Take Control",
      "artist":"Deezy",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/DEEZY_-_DEEZY-TAKE_CONTROL.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1666/1666442/covers/1.300.jpg?du=1562116723",
      "duration":"03:43",
      "Category_type":"Reggae"
   },
   {
      "name":"Pick Me Up",
      "artist":"Blackship",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Black_Ship_-_Pick_me_up.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1352/1352590/covers/1.300.jpg?du=1529884331",
      "duration":"04:04",
      "Category_type":"Reggae"
   },
   {
      "name":"Harmony",
      "artist":"Dr Groove Gang",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/DR_GROOVE_GANG_-_harmony.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1528/1528680/covers/1.300.jpg?du=1538325413",
      "duration":"03:27",
      "Category_type":"Reggae"
   },
   {
      "name":"Palm Trees",
      "artist":"Ridgway",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Ridgway_-_Palm_Trees.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s163/163960/covers/1.300.jpg?du=1529731969",
      "duration":"04:00",
      "Category_type":"Reggae"
   }
]
}


var songcount = Object.keys(songsobj.songsinobj).length;
var i;

for(i=0;i<songcount;i++){	
	$('#amplitude-right').append('<div class="song amplitude-song-container amplitude-play-pause"'+'data-amplitude-song-index="'+ i +'"> <div class="song-now-playing-icon-container"> <div class="play-button-container">    </div> <img class="now-playing" src="./img/now-playing.svg"/> </div> <div class="song-meta-data"> <span class="song-title">' + songsobj.songsinobj[i].name + '</span> <span class="song-artist">'+ songsobj.songsinobj[i].artist +'</span> </div> <a href="'+songsobj.songsinobj[i].url +'" class="bandcamp-link" target="_blank"></a> <span class="song-duration">'+songsobj.songsinobj[i].duration+'</span> </div>'
	)
}

// console.log(songsobj.songsinobj[1].name);

/*
	When the bandcamp link is pressed, stop all propagation so AmplitudeJS doesn't
	play the song.
*/
// let bandcampLinks = document.getElementsByClassName('bandcamp-link');

// for( var i = 0; i < bandcampLinks.length; i++ ){
// 	bandcampLinks[i].addEventListener('click', function(e){
// 		e.stopPropagation();
// 	});
// }


let songElements = document.getElementsByClassName('song');

for( var i = 0; i < songElements.length; i++ ){
	/*
		Ensure that on mouseover, CSS styles don't get messed up for active songs.
	*/
	songElements[i].addEventListener('mouseover', function(){
		this.style.backgroundColor = '#00A0FF';

		this.querySelectorAll('.song-meta-data .song-title')[0].style.color = '#FFFFFF';
		this.querySelectorAll('.song-meta-data .song-artist')[0].style.color = '#FFFFFF';

		if( !this.classList.contains('amplitude-active-song-container') ){
			this.querySelectorAll('.play-button-container')[0].style.display = 'block';
		}

		// this.querySelectorAll('img.bandcamp-grey')[0].style.display = 'none';
		// this.querySelectorAll('img.bandcamp-white')[0].style.display = 'block';
		// 
	
	});

	/*
		Ensure that on mouseout, CSS styles don't get messed up for active songs.
	*/
	songElements[i].addEventListener('mouseout', function(){
		this.style.backgroundColor = '#FFFFFF';
		this.querySelectorAll('.song-meta-data .song-title')[0].style.color = '#272726';
		this.querySelectorAll('.song-meta-data .song-artist')[0].style.color = '#607D8B';
		this.querySelectorAll('.play-button-container')[0].style.display = 'none';
		// this.querySelectorAll('img.bandcamp-grey')[0].style.display = 'block';
		// this.querySelectorAll('img.bandcamp-white')[0].style.display = 'none';
		// this.querySelectorAll('.song-duration')[0].style.color = '#607D8B';
	});

	/*
		Show and hide the play button container on the song when the song is clicked.
	*/
	songElements[i].addEventListener('click', function(){
		this.querySelectorAll('.play-button-container')[0].style.display = 'none';
	});
}
