from MSSpectrum cimport *
from MSExperiment cimport *
from ChromatogramPeak cimport *
from Peak1D cimport *
from Param cimport *
from ProgressLogger_LogType cimport *

cdef extern from "<OpenMS/TRANSFORMATIONS/RAW2PEAK/PeakPickerHiRes.h>" namespace "OpenMS":
    
    cdef cppclass PeakPickerHiRes:  # wrap=True
        PeakPickerHiRes()
        PeakPickerHiRes(PeakPickerHiRes)
        void pick(MSSpectrum[Peak1D] input, MSSpectrum[Peak1D] output)
        void pickExperiment(MSExperiment[Peak1D, ChromatogramPeak] input, MSExperiment[Peak1D, ChromatogramPeak] output)
        Param getParameters()
        Param getDefaults()
        void setParameters(Param param)

        void setLogType(LogType type)
