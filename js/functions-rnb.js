
/*
	Initializes AmplitudeJS
*/Amplitude.init({
	"bindings": {
		37: 'prev',
		39: 'next',
		32: 'play_pause'
	  },
	  "songs":[
   {
      "name":"Talk It Out",
      "artist":"Samie Bower",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Samie_Bower_-_Talk_It_Out.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1689/1689177/covers/1.300.jpg?du=1570263133",
      "duration":"02:44",
      "Category_type":"RNB"
   },
   {
      "name":"Gone",
      "artist":"Z-Major",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Z-Major_-_Gone.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1660/1660706/covers/1.300.jpg?du=1560561480",
      "duration":"03:19",
      "Category_type":"RNB"
   },
   {
      "name":"Fire ",
      "artist":"RXBYN",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Rxbyn_-_fire.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s185/185256/covers/1.300.jpg?du=1560561363",
      "duration":"03:45",
      "Category_type":"RNB"
   },
   {
      "name":"It Wasn’t You",
      "artist":"Natasha Niycole",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Natasha_Niycole_-_It_Wasn_t_You.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1679/1679618/covers/1.300.jpg?du=1566868700",
      "duration":"03:51",
      "Category_type":"RNB"
   },
   {
      "name":"Precious",
      "artist":"Caleb Doughty",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Caeleb_Doughty_-_Precious.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1681/1681810/covers/1.300.jpg?du=1567559820",
      "duration":"02:58",
      "Category_type":"RNB"
   }
]
	});



var songsobj = {	
		"songsinobj" :  
		[
   {
      "name":"Talk It Out",
      "artist":"Samie Bower",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Samie_Bower_-_Talk_It_Out.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1689/1689177/covers/1.300.jpg?du=1570263133",
      "duration":"02:44",
      "Category_type":"RNB"
   },
   {
      "name":"Gone",
      "artist":"Z-Major",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Z-Major_-_Gone.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1660/1660706/covers/1.300.jpg?du=1560561480",
      "duration":"03:19",
      "Category_type":"RNB"
   },
   {
      "name":"Fire ",
      "artist":"RXBYN",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Rxbyn_-_fire.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s185/185256/covers/1.300.jpg?du=1560561363",
      "duration":"03:45",
      "Category_type":"RNB"
   },
   {
      "name":"It Wasn’t You",
      "artist":"Natasha Niycole",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Natasha_Niycole_-_It_Wasn_t_You.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1679/1679618/covers/1.300.jpg?du=1566868700",
      "duration":"03:51",
      "Category_type":"RNB"
   },
   {
      "name":"Precious",
      "artist":"Caleb Doughty",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Caeleb_Doughty_-_Precious.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1681/1681810/covers/1.300.jpg?du=1567559820",
      "duration":"02:58",
      "Category_type":"RNB"
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
