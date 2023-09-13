# LowRent_Heardle
Heardle game from mp3 files on local machine

## How to play
* Point the game at the directory with the music files you wish to use. (game will ignore subdirectories)
* Hit 'Play' to hear a the opening section of a randomized song.
* Player guesses which song is being played.
* Hitting 'Skip' goes on to the next (longer) section of song.
* Player has six guess, for six increasing lengths of song.
* Reaching the end the song title will display and the song will play through until the end.
* To continue playing hit 'Skip' to move on to the next randomized song and start over.
* Hitting 'Reveal' at any time will take the player directly to displaying the song title and full play through.

## Uses:
 pygame.mixer for mp3 player   
 tkinter for GUI  
 For volume use system volume.

## Music
 Prompt at beginning to point it to where your music files are.   
 It will ignore subfolders.  


## Premise of game:
App will randomly select a song from the music folder you supplied.  
It will play clips of the song (starting at the beginning each time) of increasing length.  
Player will guess which song it is, before the reveal stage where the song title is displayed and the full song played.  
Hitting skip after the reveal will go to the next random song.  
Hitting reveal at any time will go to the reveal stage.  
