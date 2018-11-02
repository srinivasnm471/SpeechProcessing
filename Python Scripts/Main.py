#==============================================================================
import PyPlot as Plot
import PyWavRead as WavRead
import PySelectF as FileSelect
#==============================================================================
#Python Built-in Modules
#==============================================================================

#__init__

file_path = FileSelect.selectFile()
signal = WavRead.readWAVFile(file_path.name)
Plot.plotY(signal)