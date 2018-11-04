

# Documentation for Python Scripts

## Authors and Contributors
- Shashank Sharma
- Srinivas N M
- Thilak M
- Varun S S

## Recommended Installation of packages
1. numpy
2. scipy
3. python_speech_features
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
Throws:
	1. File not found Error 
	2. File not readable
	3. Module Not Found
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
Throws:
	1. Module Not Found
Args:
	 
Return: 
	folder_path
Return Info:
	1. folder_path = Path of the selected Folder
````
##### 2. Method Name : `selectFile()`
````
Throws:
	1. Module Not Found
Args:
	 
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
Throws:
	1. Module Not Found
	2. File Not Readable Error
	3. File Not found Error
Args:
	1. file_path (Type=str)
	2. plot=False (Type=Boolean)
Return: 
	data
Return Info:
	1. data = Dictionary of Frequency(Hz) and Level(dB)
````
##### 2. Method Name : `cepstrumDataFromAudacity(file_path,plot=False)`
- Will be added soon
````
Throws:
	1. Module Not Found
	2. File Not Readable Error
	3. File Not found Error
Args:
	1. file_path (Type=str)
	2. plot=False (Type=Boolean)
Return: 
	data
Return Info:
	1. data = Dictionary of Lag(s) Frequency(Hz) and Level
````
---
### File Name : *PyPlot.py*
All Plotting methods are written here
##### 1. Method Name : `plotY(signal,stem=False,title='',xLabel='',yLabel='')`
````
Description:
	Plots range(1,len(signal)) vs signal and returns the plot object
Throws:
	1. List/Array Error
Args:
	1. signal (Type=numpy array/list)
	2. stem=False (Type=Boolean)
	3. title='' (Type=str)
	4. xLabel=''(Type=str)
	5. yLabel='' (Type=str)
Return: 
	Matpotlib.PyPlot.plot() object 
Return Info:
	1. The plot object
````
##### 2. Method Name : `plotXY(x=[],y=[],stem=False,title='',xLabel='',yLabel='')`
````
Description:
	Plots x vs y and returns the plot object. x and y must be of the same length
Throws:
	1. List/Array Error
Args:
	1. x,y (Type=numpy array/list)
	2. stem=False (Type=Boolean)
	3. title='' (Type=str)
	4. xLabel=''(Type=str)
	5. yLabel='' (Type=str)
Return: 
	Matpotlib.PyPlot.plot() object 
Return Info:
	1. The plot object of X vs Y plot
````
##### 3. Method Name : `plotSpectrum(y,frequency,log=False,title='',xLabel='',yLabel='')`
````
Description:
	Plots the spectrum data of frequency vs y. x and y must be of same length
	if log=True:
		frequency is plotted in logarithmic scale
Throws:
	1. List/Array Error
Args:
	1. y,frequency (Type=numpy array/list)
	2. log=False (Type=Boolean)
	3. title='' (Type=str)
	4. xLabel=''(Type=str)
	5. yLabel='' (Type=str)
Return: 
	Matpotlib.PyPlot.plot() object 
Return Info:
	1. The plot object of X vs Y plot
````
##### 3. Method Name : `plotSpectrogram(signal,fs)`
Implementation errors may exist
````
Description:
	Plots the spectrogram of a discrete signal sampled at fs
Throws:
	1. List/Array Error
Args:
	1. signal (Type=numpy array/list)
	2. fs (Type=int)
````
---
