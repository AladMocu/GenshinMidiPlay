# By AladMocu (with linkhl09 help :v)
import pretty_midi as midi
import sys

songname =sys.argv[1]

song = midi.PrettyMIDI(songname)
songNotes={}



for instrument in song.instruments:
    if not instrument.is_drum:
        mc=[["1",0],["2",0],["3",0],["4",0],["5",0],["6",0],["7",0]]
        for note in instrument.notes:
            a = midi.note_number_to_name(note.pitch)
            a = a.replace('#','')
            t = int(a[-1:])
            mc[t-1][1] += 1
        t=[]
        maxv=0
        print(instrument.name," : ",mc)
        for n in range(5):
            if mc[n][1]+mc[n+1][1]+mc[n+2][1] > maxv:
                maxv=mc[n][1]+mc[n+1][1]+mc[n+2][1]
                t= mc[n:n+3]
        mc=list(map(lambda x: str(x[0]),t))
        last = 0
        for i in range(len(instrument.notes)-1):
            note= instrument.notes[i]
            a = midi.note_number_to_name(note.pitch)
            a = a.replace('#','')
            if mc[0] in a:
                transpose = a.replace(mc[0],'1')
                if str(note.start) in songNotes.keys():
                    songNotes[str(note.start)].append(transpose)
                else:
                    songNotes[str(note.start)] =[transpose]
            elif mc[1] in a:
                transpose = a.replace(mc[1],'2')
                if str(note.start) in songNotes.keys():
                    songNotes[str(note.start)].append(transpose)
                else:
                    songNotes[str(note.start)] =[transpose]
            elif mc[2] in a:
                transpose = a.replace(mc[2],'3')
                if str(note.start) in songNotes.keys():
                    songNotes[str(note.start)].append(transpose)
                else:
                    songNotes[str(note.start)] =[transpose]

lastts="0"
lastnotes=[]
songFinal=[]
firtst = True
for key in songNotes:
    duration=float(key)-float(lastts)
    if not firtst:
        songFinal.append([str(duration),lastnotes])
    lastnotes = songNotes[key]
    lastts=float(key)
    firtst = False
nfile = open("{}.gm".format(songname[0:-4]).replace(" ","_"), 'w')
nfile.write(str(songFinal))
nfile.close()
