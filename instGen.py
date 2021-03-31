# By AladMocu (with linkhl09 help :v)
import pretty_midi as midi
import sys

songname =sys.argv[1]

song = midi.PrettyMIDI(songname)
print(song.instruments)
print(song.get_beats)

li=0
for instrument in song.instruments:
    li+=1
    transpose = ""
    # Don't want to shift drum notes
    transpose+="#{}\n".format(instrument)
    if not instrument.is_drum:
        mc=[["1",0],["2",0],["3",0],["4",0],["5",0],["6",0]]
        for note in instrument.notes:
            a = midi.note_number_to_name(note.pitch)
            a = a.replace('#','')
            t = int(a[-1:])
            mc[t-1][1] += 1
        print(instrument.name," : ",mc)
        t=[]
        maxv=0
        for n in range(4):
            if mc[n][1]+mc[n+1][1]+mc[n+2][1] > maxv:
                maxv=mc[n][1]+mc[n+1][1]+mc[n+2][1]
                t= mc[n:n+3]
        mc=list(map(lambda x: str(x[0]),t))
        print(mc)
        last = 0
        for i in range(len(instrument.notes)-1):
            note= instrument.notes[i]
            longitude=str(note.end-note.start)
            if note.start == instrument.notes[i+1].start:
                longitude = "0"
            else:
                last= note.start
            a = midi.note_number_to_name(note.pitch)
            a = a.replace('#','')
            if mc[0] in a:
                transpose += a.replace(mc[0],'1')
                transpose+=":"+longitude+"\n"
            elif mc[1] in a:
                transpose += a.replace(mc[1],'2')
                transpose+=":"+longitude+"\n"
            elif mc[2] in a:
                transpose += a.replace(mc[2],'3')
                transpose+=":"+longitude+"\n"
    nfile = open("{}-{}.txt".format(songname[0:-4],instrument.name+str(li)).replace(" ","_"), 'w')
    nfile.write(transpose)
    nfile.close()
 
