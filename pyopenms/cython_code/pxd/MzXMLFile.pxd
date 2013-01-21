
from MSExperiment  cimport *
from ChromatogramPeak cimport *
from Peak1D cimport *
from libcpp.string cimport *

cdef extern from "<OpenMS/FORMAT/MzXMLFile.h>" namespace "OpenMS":

    cdef cppclass MzXMLFile:  # wrap=True
        MzXMLFile()
        # cython does not support free template args, so Peak1D has
        # to be used as a fixed argument
        void load(string, MSExperiment[Peak1D, ChromatogramPeak]) except+
        void store(string, MSExperiment[Peak1D, ChromatogramPeak]) except+