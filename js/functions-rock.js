
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
      "name":"Saint Cecelia",
      "artist":"Foo Fighters",
      "album":"single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/01%20-%20Saint%20Cecilia.mp3",
      "cover_art_url":"https://m.media-amazon.com/images/I/7142gOmVnTL._AC_UY436_FMwebp_QL65_.jpg",
      "duration":"03:41",
      "Category_type":"Rock"
   },
   {
      "name":"Sean",
      "artist":"Foo Fighters",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/02%20-%20Sean.mp3",
      "cover_art_url":"https://m.media-amazon.com/images/I/7142gOmVnTL._AC_UY436_FMwebp_QL65_.jpg",
      "duration":"02:11",
      "Category_type":"Rock"
   },
   {
      "name":"The Neverending Sign",
      "artist":"Foo Fighters",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/05%20-%20The%20Neverending%20Sigh.mp3",
      "cover_art_url":"https://m.media-amazon.com/images/I/7142gOmVnTL._AC_UY436_FMwebp_QL65_.jpg",
      "duration":"04:45",
      "Category_type":"Rock"
   },
   {
      "name":"Wild Heart",
      "artist":"Omonoko",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Omonoko_-_Wild_Heart.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s181/181920/covers/1.300.jpg?du=1547720144",
      "duration":"04:02",
      "Category_type":"Rock"
   },
   {
      "name":"Repentance",
      "artist":"Carrying Goodness",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Carrying_Goodness_-_Repentance.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s183/183627/covers/1.300.jpg?du=1553048310",
      "duration":"02:47",
      "Category_type":"Rock"
   }
]
	});



var songsobj = {	
		"songsinobj" :  
		[
   {
      "name":"Saint Cecelia",
      "artist":"Foo Fighters",
      "album":"single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/01%20-%20Saint%20Cecilia.mp3",
      "cover_art_url":"https://m.media-amazon.com/images/I/7142gOmVnTL._AC_UY436_FMwebp_QL65_.jpg",
      "duration":"03:41",
      "Category_type":"Rock"
   },
   {
      "name":"Sean",
      "artist":"Foo Fighters",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/02%20-%20Sean.mp3",
      "cover_art_url":"https://m.media-amazon.com/images/I/7142gOmVnTL._AC_UY436_FMwebp_QL65_.jpg",
      "duration":"02:11",
      "Category_type":"Rock"
   },
   {
      "name":"The Neverending Sign",
      "artist":"Foo Fighters",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/05%20-%20The%20Neverending%20Sigh.mp3",
      "cover_art_url":"https://m.media-amazon.com/images/I/7142gOmVnTL._AC_UY436_FMwebp_QL65_.jpg",
      "duration":"04:45",
      "Category_type":"Rock"
   },
   {
      "name":"Wild Heart",
      "artist":"Omonoko",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Omonoko_-_Wild_Heart.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s181/181920/covers/1.300.jpg?du=1547720144",
      "duration":"04:02",
      "Category_type":"Rock"
   },
   {
      "name":"Repentance",
      "artist":"Carrying Goodness",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Carrying_Goodness_-_Repentance.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s183/183627/covers/1.300.jpg?du=1553048310",
      "duration":"02:47",
      "Category_type":"Rock"
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
