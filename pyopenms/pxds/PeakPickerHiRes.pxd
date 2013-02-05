from MSSpectrum cimport *
from MSExperiment cimport *
from ChromatogramPeak cimport *
from Peak1D cimport *
from Param cimport *
from ProgressLogger_LogType cimport *

cdef extern from "<OpenMS/TRANSFORMATIONS/RAW2PEAK/PeakPickerHiRes.h>" namespace "OpenMS":

    cdef cppclass PeakPickerHiRes:
        PeakPickerHiRes()                  except +
        PeakPickerHiRes(PeakPickerHiRes)   except + #wrap-ignore
        void pick(MSSpectrum[Peak1D] & input, MSSpectrum[Peak1D] & output) except +
        void pickExperiment(MSExperiment[Peak1D, ChromatogramPeak] & input, MSExperiment[Peak1D, ChromatogramPeak] & output) except +
        Param getParameters() except +
        Param getDefaults()   except +
        void setParameters(Param param) except +

        void setLogType(LogType type) except +
