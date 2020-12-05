# data_to_wav
Creating wav files from .txt documents - 8 bit data from ADC to wav

Example files given
  small_signal.txt:   8 bit datapoints separated by whitespace. The code reads these values and writes them into a wav file.
  small_signal_t.txt: hterm log save - this is useful, because the start and finsih time of recording can be extracted from it. The sample-rate and lenght of the .wav can then be
                      calculated - needed for .wav header.
                      
The sample data is from a small object moving gently in front of a dopler-radar. There output and a filtered version of that is also there as sample.

Quick-fix!
Some stuff might have to be changed before using, e.g. the number of characters deleted from the end of a time-stamp or the place for the line where
end-of-recording time is to be found.
