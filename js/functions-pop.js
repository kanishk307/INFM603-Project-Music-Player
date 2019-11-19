
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
      "name":"Wake Up",
      "artist":"Square A Saw",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Square_a_Saw_-_Wake_Up%20(1).mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1672/1672835/covers/1.300.jpg?du=1564363054",
      "duration":"02:42",
      "Category_type":"Pop"
   },
   {
      "name":"Don’t Wanna Go",
      "artist":"The DLX",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/THE_DLX_-_Don_t_Wanna_Go.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1662/1662389/covers/1.300.jpg?du=1561166211",
      "duration":"03:03",
      "Category_type":"Pop"
   },
   {
      "name":"Breathe",
      "artist":"George Capon",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/George_Capon_-_Breathe.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1667/1667044/covers/1.300.jpg?du=1568855763",
      "duration":"02:46",
      "Category_type":"Pop"
   },
   {
      "name":"You",
      "artist":"RVNS",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/RVNS_-_You.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1651/1651860/covers/1.300.jpg?du=1572309910",
      "duration":"02:58",
      "Category_type":"Pop"
   },
   {
      "name":"Shine On",
      "artist":"Square A Saw",
      "album":"single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Square_a_Saw_-_Shine_On.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1672/1672836/covers/1.300.jpg?du=1564363055",
      "duration":"02:57",
      "Category_type":"Pop"
   },
   {
      "name":"Wasn’t Enough",
      "artist":"Tom Orlando ",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Square_a_Saw_-_Wake_Up%20(1).mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1672/1672835/covers/1.300.jpg?du=1564363054",
      "duration":"02:42",
      "Category_type":"Pop"
   }
]
	});



var songsobj = {	
		"songsinobj" :  
		[
   {
      "name":"Wake Up",
      "artist":"Square A Saw",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Square_a_Saw_-_Wake_Up%20(1).mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1672/1672835/covers/1.300.jpg?du=1564363054",
      "duration":"02:42",
      "Category_type":"Pop"
   },
   {
      "name":"Don’t Wanna Go",
      "artist":"The DLX",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/THE_DLX_-_Don_t_Wanna_Go.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1662/1662389/covers/1.300.jpg?du=1561166211",
      "duration":"03:03",
      "Category_type":"Pop"
   },
   {
      "name":"Breathe",
      "artist":"George Capon",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/George_Capon_-_Breathe.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1667/1667044/covers/1.300.jpg?du=1568855763",
      "duration":"02:46",
      "Category_type":"Pop"
   },
   {
      "name":"You",
      "artist":"RVNS",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/RVNS_-_You.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1651/1651860/covers/1.300.jpg?du=1572309910",
      "duration":"02:58",
      "Category_type":"Pop"
   },
   {
      "name":"Shine On",
      "artist":"Square A Saw",
      "album":"single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Square_a_Saw_-_Shine_On.mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1672/1672836/covers/1.300.jpg?du=1564363055",
      "duration":"02:57",
      "Category_type":"Pop"
   },
   {
      "name":"Wasn’t Enough",
      "artist":"Tom Orlando ",
      "album":"Single",
      "url":"https://terpconnect.umd.edu/~nletang/Songs/Square_a_Saw_-_Wake_Up%20(1).mp3",
      "cover_art_url":"https://cdn-img.jamendo.com/track/s1672/1672835/covers/1.300.jpg?du=1564363054",
      "duration":"02:42",
      "Category_type":"Pop"
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
