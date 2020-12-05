#Erfasste Werte in .wav file konvertieren
#aus timestamps_test.log wird die Zeitdauer der Aufnahme ausgewonnen
#dann werden die Werte einzeln aus wtest_values.txt ausgelesen und in die Ausgang .wav gespeischert.





import wave, struct, math
from decimal import Decimal
from datetime import datetime


f = open("decimal.txt", 'r')                            #Datei mit Werten öffnen


with open('timestamps01.txt', 'r') as g:                 #Anfang- und Endezeit auslesen
    first_line = g.readline()
    lines = g.read().splitlines()
    last_line = lines[-1]

first_line = first_line[:-2]                                #Anfang- und Endzeitstring für Substrahieren schneiden
last_line = last_line[:-3]

print(first_line)
print(last_line)

start_time = datetime.strptime(first_line, '%H:%M:%S.%f')   #Zeiten in datetime Format speichern
end_time = datetime.strptime(last_line, '%H:%M:%S.%f')
time_d = end_time - start_time                              #Zeitdauer ausrechnen



sampleRate = 4000.0 #Hz                                     #Sample rate - im Programm der REB165 eingestellt...
duration = math.ceil(time_d.total_seconds())                #Zeitdauer - hier wird der ausgerechnete Wert auf Sekunden umgerechnet
wavefile = wave.open('rain.wav', 'w')                       #Öffnen der Ausgang .wav
wavefile.setnchannels(1)                                    #Mono channel einstellen
wavefile.setsampwidth(1)                                    #Sample width =  1 Byte (8 Bit Messwerte)
wavefile.setframerate(sampleRate)

print("Length of record:")
print(duration)

print("Writing into .wav file...")
while (1):                                                  #Schleife, in der die Werte in die .wav file geschrieben werden.
    lastread = (f.read(3))                                  #3 Charakter lesen
    if (len(lastread) == 3):                                #wenn tatsächlich 3 Charakter gelesen wurde, dann EOF noch nicht erreicht.
        value = int(lastread)                               #Cast: Gelesene String auf int
        data = struct.pack('<h', value)                     #Wert als für .wav geeignete Datenstruktur speichern
        wavefile.writeframesraw(data)                       #Wert in .wav schreiben
        f.read(1)                                           #Lesezeichen zwischen Werte überspringen
    else:
        break
print("Closing file...")
wavefile.close()

print("Goodbye!")