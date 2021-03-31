# Genshin MIDI Player

this is a little project that tries to may MIDI song files inside of the Genshin Impact Game and its music instrument, there are some limitatios as there are no flats and there are only 3 octaves in the game.


There are 2 main ways to use this scripts:

* Instrument scripts

* Song scripts

the main diference whitin this modes its the final sound, with the Instrument mode you can get one playable file per instrument in the original MIDI song, and with the Song mode it will give you one single file for the song.

  

## Instrument Script

For using this mode you have to run `instGen.py songname.mid` to generate each instrument file, and `instPlay.mid songname-instrument.txt` to play the instrument. **Note that you have 5 seconds to swtch to Genshin lyre mode before it starts playing the song.**
## Song Script

For using this script you have to run `wholeGen.py songname.mid` to generate each instrument file, and `wholeGen.py songname-instrument.gs` to play the song. **Note that you have 5 seconds to swtch to Genshin lyre mode before it starts playing the song.**

## Example final result:

For this example I runned the megalovania MIDI song and the instrument mode:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/yMC8xY8uUIU/0.jpg)](https://www.youtube.com/watch?v=yMC8xY8uUIU)
