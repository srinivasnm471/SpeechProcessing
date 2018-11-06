[file,path] = uigetfile;
[signal,fs] = audioread(strcat(path,'\',file));
plot(signal)
[coeffs,delta,deltaDelta,loc] = mfcc(signal,fs);
