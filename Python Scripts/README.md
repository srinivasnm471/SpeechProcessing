# Documentation for Python Scripts

## Authors and Contributors
- Shashank Sharma
- Srinivas N M
- Thilak M
- Varun S S

## Recommended Installation of packages
1. numpy
2. scipy
3. librosa
4. gTTS
5. tkinter
6. matpotlib
7. speech_recognition
8. playsound
----
## Code Documentation
### File Name : *Main.py*
The Execution of the Project starts from here. 

---
### File Name : *PyWavRead.py*
To read a .wav file and return the discrete signal points. Uses wave package.
````
Py Modules Imported
	    1. scipy
	    2. sys
````
##### 1. Method Name : `readWAVFile(file_path='')`
````
Args:
	1. file_path = '' (Type = str)  
Return: 
	fs,signal
Return Info:
	1. fs = Sampling Rate of the audio file / Sampling frequency
	2. signal = (1*n) numpy array
````
---
### File Name : *PySelectF.py*
To select a file/folder with GUI
````
Py Modules Imported
	1. tkinter
````
##### 1. Method Name : `selectFolder()`
````
Return: 
	folder_path
Return Info:
	1. folder_path = Path of the selected Folder
````
##### 2. Method Name : `selectFile()`
````
Return: 
	file_path.name
Return Info:
	1. file_path.name = Path of the selected File
````
---
### File Name : *PyAutomateDataCollection.py*
Automatically Parses audacity data to Python dictionary
[Sample Spectrum Data From Audacity](https://github.com/shashankrnr32/SpeechProcessing/blob/master/Data%20Samples/DataPoints/A35Male.txt)
[Sample Cepstrum Data From Audacity](https://github.com/shashankrnr32/SpeechProcessing/blob/master/Data%20Samples/DataPoints/A35MaleCep.txt)
##### 1. Method Name : `spectrumDataFromAudacity(file_path,plot=False)`
````
Args:
	1. file_path (Type=str)
	2. plot=False (Type=Boolean)
Return: 
	data
Return Info:
	1. data = Dictionary of Frequency(Hz) and Level(dB)
````
##### 2. Method Name : `cepstrumDataFromAudacity(file_path,plot=False)`
- ***Will be added soon***
````
Args:
	1. file_path (Type=str)
	2. plot=False (Type=bool)
Return: 
	data
Return Info:
	1. data = Dictionary of Lag(s) Frequency(Hz) and Level
````
---
### File Name : *PyPlot.py*
All Plotting methods are written here
````
Py Modules Imported
	1. matpotlib
	2. scipy
	3. librosa
````
##### 1. Method Name : `plotY(signal,stem=False,title='',xLabel='',yLabel='',subPlot=None)`
````
Description:
	Plots range(1,len(signal)) vs signal and returns the plot object
Args:
	1. signal (Type=numpy array/list)
	2. stem=False (Type=bool)
	3. title='' (Type=str)
	4. xLabel=''(Type=str)
	5. yLabel='' (Type=str)
	6. subPlot=None (Type=int)
Return: 
	Matpotlib.PyPlot.plot() object 
````
##### 2. Method Name : `plotXY(x=[],y=[],stem=False,title='',xLabel='',yLabel='',subPlot=None)`
````
Description:
	Plots x vs y and returns the plot object. x and y must be of the same length
Args:
	1. x,y (Type=numpy array/list)
	2. stem=False (Type=bool)
	3. title='' (Type=str)
	4. xLabel=''(Type=str)
	5. yLabel='' (Type=str)
	6. subPlot=None (Type=int)
Return: 
	Matpotlib.PyPlot object 
````
##### 3. Method Name : `plotSpectrum(y,frequency,log=False,title='',xLabel='',yLabel='',subPlot=None)`
````
Description:
	Plots the spectrum data of frequency vs y. x and y must be of same length
	if log==True:
		frequency is plotted in logarithmic scale
Args:
	1. y,frequency (Type=numpy array/list)
	2. log=False (Type=bool)
	3. title='' (Type=str)
	4. xLabel=''(Type=str)
	5. yLabel='' (Type=str)
	6. subPlot=None (Type=int)
Return: 
	Matpotlib.PyPlot object 
````
##### 3. Method Name : `plotSpectrogram(signal,fs,ret='False',subPlot=None)`
````
Description:
	Plots the spectrogram of a discrete signal sampled at fs
	Hamming Window: Length = 2048 ,No of Points = 2000
Args:
	1. signal (Type=numpy array/list)
	2. fs (Type=int)
	3. ret (Type=bool)
	4. subPlot (Type=int)
Return:
	frequency,times,spectrogram (if ret == True)
````
##### 3. Method Name : `plotFeatures(feature,title='',subPlot=None)`
````
Description:
	Plots the colormap plot of Feature vectors
Args:
	1. feature (Type=np.array)
	2. title='' (Type=str)
	3. subPlot=None (Type=int)
````
---
