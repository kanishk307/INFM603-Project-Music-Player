
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
      "name":"Break The Ice",
      "artist":"Adraxx",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Adraxx_-_Break_The_Ice.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1651/1651644/covers/1.300.jpg?du=1563373266",
      "duration":"03:53",
      "Category_type":"Hip Hop"
   },
   {
      "name":"Phoneline",
      "artist":"Samie Bower",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Samie_Bower_-_Phoneline.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s184/184380/covers/1.300.jpg?du=1557882976",
      "duration":"03:55",
      "Category_type":"Hip Hop"
   },
   {
      "name":"Fake Love",
      "artist":"Ralph Da God",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Ralph_Da_God_-_Fake_Love.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1686/1686730/covers/1.300.jpg?du=1569201651",
      "duration":"03:22",
      "Category_type":"Hip Hop"
   },
   {
      "name":"Love Her",
      "artist":"J Bert",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/J_Bert_-_Love_Her.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s187/187961/covers/1.300.jpg?du=1569806260",
      "duration":"03:09",
      "Category_type":"Hip Hop"
   }
]
	});



var songsobj = {	
		"songsinobj" :  
		[
   {
      "name":"Break The Ice",
      "artist":"Adraxx",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Adraxx_-_Break_The_Ice.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1651/1651644/covers/1.300.jpg?du=1563373266",
      "duration":"03:53",
      "Category_type":"Hip Hop"
   },
   {
      "name":"Phoneline",
      "artist":"Samie Bower",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Samie_Bower_-_Phoneline.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s184/184380/covers/1.300.jpg?du=1557882976",
      "duration":"03:55",
      "Category_type":"Hip Hop"
   },
   {
      "name":"Fake Love",
      "artist":"Ralph Da God",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Ralph_Da_God_-_Fake_Love.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1686/1686730/covers/1.300.jpg?du=1569201651",
      "duration":"03:22",
      "Category_type":"Hip Hop"
   },
   {
      "name":"Love Her",
      "artist":"J Bert",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/J_Bert_-_Love_Her.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/albums/s187/187961/covers/1.300.jpg?du=1569806260",
      "duration":"03:09",
      "Category_type":"Hip Hop"
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
