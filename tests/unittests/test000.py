import pyopenms




def _testMetaInfoInterface(what):

    #void getKeys(libcpp_vector[String] & keys)
    #void getKeys(libcpp_vector[unsigned int] & keys)
    #DataValue getMetaValue(unsigned int) nogil except +
    #DataValue getMetaValue(String) nogil except +
    #void setMetaValue(unsigned int, DataValue) nogil except +
    #void setMetaValue(String, DataValue) nogil except +
    #bool metaValueExists(String) nogil except +
    #bool metaValueExists(unsigned int) nogil except +
    #void removeMetaValue(String) nogil except +
    #void removeMetaValue(unsigned int) nogil except +

    what.setMetaValue("key", pyopenms.DataValue(42))
    what.setMetaValue("key2", pyopenms.DataValue(42))

    keys = []
    what.getKeys(keys)
    keys = [0]
    what.getKeys(keys)
    assert len(keys) and all(isinstance(k, (long, int)) for k in keys)
    assert what.getMetaValue(keys[0]).toInt() == 42
    keys = [""]
    what.getKeys(keys)
    assert len(keys) and all(isinstance(k, str) for k in keys)

    assert what.getMetaValue(keys[0]).toInt() == 42

    assert what.metaValueExists("key")
    what.removeMetaValue("key")

    what.setMetaValue(1024, pyopenms.DataValue(42))

    keys = []
    what.getKeys(keys)
    keys = [0]
    what.getKeys(keys)
    assert len(keys) and all(isinstance(k, (long, int)) for k in keys)
    assert what.getMetaValue(keys[0]).toInt() == 42
    keys = [""]
    what.getKeys(keys)
    assert len(keys) and all(isinstance(k, str) for k in keys)

    assert what.getMetaValue(keys[0]).toInt() == 42

    what.setMetaValue("key", pyopenms.DataValue(42))
    what.setMetaValue("key2", pyopenms.DataValue(42))

    assert what.metaValueExists("key")
    what.removeMetaValue("key")
    keys = []
    what.getKeys(keys)
    assert len(keys) == 2
    what.removeMetaValue("key2")
    keys = []
    what.getKeys(keys)
    assert len(keys) == 1


    what.clearMetaInfo()
    keys = []
    what.getKeys(keys)
    assert len(keys) == 0


def _testUniqueIdInterface(what):

    assert what.hasInvalidUniqueId()
    assert not what.hasValidUniqueId()
    assert what.ensureUniqueId()
    assert isinstance(what.getUniqueId(), (int, long))
    assert what.getUniqueId() > 0
    assert not what.hasInvalidUniqueId()
    assert what.hasValidUniqueId()

    what.clearUniqueId()
    assert what.getUniqueId() == 0
    assert what.hasInvalidUniqueId()
    assert not what.hasValidUniqueId()

    assert what.ensureUniqueId()
    assert isinstance(what.getUniqueId(), (int, long))
    assert what.getUniqueId() > 0
    assert not what.hasInvalidUniqueId()
    assert what.hasValidUniqueId()

    what.setUniqueId(1234)
    assert  what.getUniqueId() == 1234


def _testProgressLogger(ff):
    """
    @tests:
     ProgressLogger.__init__
     ProgressLogger.endProgress
     ProgressLogger.getLogType
     ProgressLogger.setLogType
     ProgressLogger.setProgress
     ProgressLogger.startProgress
    """

    ff.setLogType(pyopenms.LogType.NONE)
    assert ff.getLogType() == pyopenms.LogType.NONE
    ff.startProgress(0, 3, "label")
    ff.setProgress(0)
    ff.setProgress(1)
    ff.setProgress(2)
    ff.setProgress(3)
    ff.endProgress()



def testAAS():
    """
    @tests:
     AASequence.__init__
     AASequence.__add__
     AASequence.__radd__
     AASequence.__iadd__
     AASequence.getCTerminalModification
     AASequence.getNTerminalModification
     AASequence.setCTerminalModification
     AASequence.setModification
     AASequence.setNTerminalModification
     AASequence.setStringSequence
     AASequence.toString
     AASequence.toUnmodifiedString
    """
    aas = pyopenms.AASequence()

    aas + aas
    aas += aas

    aas.__doc__
    aas = pyopenms.AASequence("DFPIANGER")
    assert aas.getCTerminalModification() == ""
    assert aas.getNTerminalModification() == ""
    aas.setCTerminalModification("")
    aas.setNTerminalModification("")
    aas.setStringSequence("")
    assert aas.toString() == ""
    assert aas.toUnmodifiedString() == ""


def test_AcquisitionInfo():
    """
    @tests:
     AcquisitionInfo.__init__
     AcquisitionInfo.__eq__
     AcquisitionInfo.__ge__
     AcquisitionInfo.__gt__
     AcquisitionInfo.__le__
     AcquisitionInfo.__lt__
     AcquisitionInfo.__ne__
     AcquisitionInfo.getMethodOfCombination
     AcquisitionInfo.setMethodOfCombination
    """

    ai = pyopenms.AcquisitionInfo()
    ai.__doc__

    assert ai == ai
    assert not ai != ai
    ai.setMethodOfCombination("ABC")
    assert ai.getMethodOfCombination() == "ABC"

def test_BaseFeature():
    """
    @tests:
     BaseFeature.__init__
     BaseFeature.clearUniqueId
     BaseFeature.ensureUniqueId
     BaseFeature.getCharge
     BaseFeature.getKeys
     BaseFeature.getMetaValue
     BaseFeature.getQuality
     BaseFeature.getUniqueId
     BaseFeature.getWidth
     BaseFeature.hasInvalidUniqueId
     BaseFeature.hasValidUniqueId
     BaseFeature.metaValueExists
     BaseFeature.removeMetaValue
     BaseFeature.setCharge
     BaseFeature.setMetaValue
     BaseFeature.setQuality
     BaseFeature.setWidth
     BaseFeature.clearMetaInfo
     BaseFeature.setUniqueId
    """
    bf = pyopenms.BaseFeature()
    _testMetaInfoInterface(bf)
    _testUniqueIdInterface(bf)
    bf.clearUniqueId()
    assert bf.ensureUniqueId()
    assert bf.getCharge() == 0
    assert isinstance(bf.getQuality(), float)
    assert isinstance(bf.getUniqueId(), (long, int))
    assert isinstance(bf.getWidth(), float)

    assert not bf.hasInvalidUniqueId()
    assert bf.hasValidUniqueId()


    _testMetaInfoInterface(bf)
    bf.setCharge(1)
    bf.setQuality(0.0)
    bf.setWidth(1.0)

def testChecksumType():
    """
    @tests:
     ChecksumType.MD5
     ChecksumType.SHA1
     ChecksumType.SIZE_OF_CHECKSUMTYPE
     ChecksumType.UNKNOWN_CHECKSUM
    """
    assert isinstance(pyopenms.ChecksumType.MD5, int)
    assert isinstance(pyopenms.ChecksumType.SHA1, int)
    assert isinstance(pyopenms.ChecksumType.SIZE_OF_CHECKSUMTYPE, int)
    assert isinstance(pyopenms.ChecksumType.UNKNOWN_CHECKSUM, int)


def testChromatogramPeak():
    """
    @tests:
     ChromatogramPeak.__init__
     ChromatogramPeak.__eq__
     ChromatogramPeak.__ge__
     ChromatogramPeak.__gt__
     ChromatogramPeak.__le__
     ChromatogramPeak.__lt__
     ChromatogramPeak.__ne__
     ChromatogramPeak.getIntensity
     ChromatogramPeak.getRT
     ChromatogramPeak.setIntensity
     ChromatogramPeak.setRT
    """
    p = pyopenms.ChromatogramPeak()
    assert p == p
    assert not p != p


    p.setIntensity(12.0)
    p.setRT(34.0)
    assert p.getIntensity() == 12.0
    assert p.getRT() == 34.0



def testChromatogramToosl():
    """
    @tests:
     ChromatogramTools.__init__
     ChromatogramTools.convertChromatogramsToSpectra
     ChromatogramTools.convertSpectraToChromatograms
    """
    pyopenms.ChromatogramTools()
    pyopenms.ChromatogramTools.convertChromatogramsToSpectra
    pyopenms.ChromatogramTools.convertSpectraToChromatograms


def testConsensusFeature():
    """
    @tests:
     ConsensusFeature.__eq__
     ConsensusFeature.__ge__
     ConsensusFeature.__gt__
     ConsensusFeature.__le__
     ConsensusFeature.__lt__
     ConsensusFeature.__ne__
     ConsensusFeature.__init__
     ConsensusFeature.clearUniqueId
     ConsensusFeature.computeConsensus
     ConsensusFeature.computeDechargeConsensus
     ConsensusFeature.computeMonoisotopicConsensus
     ConsensusFeature.ensureUniqueId
     ConsensusFeature.getCharge
     ConsensusFeature.getKeys
     ConsensusFeature.getMetaValue
     ConsensusFeature.getQuality
     ConsensusFeature.getUniqueId
     ConsensusFeature.getWidth
     ConsensusFeature.hasInvalidUniqueId
     ConsensusFeature.hasValidUniqueId
     ConsensusFeature.insert
     ConsensusFeature.metaValueExists
     ConsensusFeature.removeMetaValue
     ConsensusFeature.setCharge
     ConsensusFeature.setMetaValue
     ConsensusFeature.setQuality
     ConsensusFeature.setWidth
     ConsensusFeature.clearMetaInfo
     ConsensusFeature.setUniqueId
    """


    f = pyopenms.ConsensusFeature()
    _testUniqueIdInterface(f)
    _testMetaInfoInterface(f)

    f.setCharge(1)
    f.setQuality(2.0)
    f.setWidth(4.0)
    assert f.getCharge() == 1
    assert f.getQuality() == 2.0
    assert f.getWidth() == 4.0

    f.insert(0, pyopenms.Peak2D(), 1)
    f.insert(1, pyopenms.BaseFeature())
    f.insert(2, pyopenms.ConsensusFeature())

    f.computeConsensus()
    f.computeDechargeConsensus
    f.computeMonoisotopicConsensus()


def testDataProcessing(dp=pyopenms.DataProcessing()):

    """
    @tests:
     DataProcessing.__init__
     DataProcessing.getKeys
     DataProcessing.getMetaValue
     DataProcessing.getProcessingActions
     DataProcessing.getSoftware
     DataProcessing.isMetaEmpty
     DataProcessing.metaValueExists
     DataProcessing.removeMetaValue
     DataProcessing.setCompletionTime
     DataProcessing.setMetaValue
     DataProcessing.setProcessingActions
     DataProcessing.setSoftware
     DataProcessing.__eq__
     DataProcessing.__ge__
     DataProcessing.__gt__
     DataProcessing.__le__
     DataProcessing.__lt__
     DataProcessing.__ne__
     DataProcessing.clearMetaInfo
     DataProcessing.getCompletionTime
    """

    _testMetaInfoInterface(dp)

    assert dp == dp
    assert not dp != dp

    assert isinstance(dp.getCompletionTime().getDate(), str)
    assert isinstance(dp.getCompletionTime().getTime(), str)
    dp.clearMetaInfo()
    k = []
    dp.getKeys(k)
    assert k == []
    dp.getMetaValue
    ac = dp.getProcessingActions()
    assert ac == set(())
    dp.setProcessingActions(ac)
    assert isinstance(dp.getSoftware().getName(), str)
    assert isinstance(dp.getSoftware().getVersion(), str)
    dp.isMetaEmpty()
    dp.metaValueExists
    dp.removeMetaValue
    dp.setCompletionTime(pyopenms.DateTime.now())
    s = dp.getSoftware()
    s.setName("pyopenms")
    dp.setSoftware(s)

    assert dp.getSoftware().getName() == "pyopenms"


def testDataType():
    """
    @tests:
     DataType.DOUBLE_LIST
     DataType.DOUBLE_VALUE
     DataType.EMPTY_VALUE
     DataType.INT_LIST
     DataType.INT_VALUE
     DataType.STRING_LIST
     DataType.STRING_VALUE
    """
    assert isinstance(pyopenms.DataType.DOUBLE_LIST, int)
    assert isinstance(pyopenms.DataType.DOUBLE_VALUE, int)
    assert isinstance(pyopenms.DataType.EMPTY_VALUE, int)
    assert isinstance(pyopenms.DataType.INT_LIST, int)
    assert isinstance(pyopenms.DataType.INT_VALUE, int)
    assert isinstance(pyopenms.DataType.STRING_LIST, int)
    assert isinstance(pyopenms.DataType.STRING_VALUE, int)

def testDataValue():
    """
    @tests:
     DataValue.__init__
     DataValue.isEmpty
     DataValue.toDoubleList
     DataValue.toDouble
     DataValue.toInt
     DataValue.toIntList
     DataValue.toString
     DataValue.toStringList
     DataValue.valueType

    """
    a = pyopenms.DataValue()
    assert a.isEmpty()

    a = pyopenms.DataValue(1)
    assert not a.isEmpty()
    assert a.toInt() == 1
    assert a.valueType() == pyopenms.DataType.INT_VALUE

    a = pyopenms.DataValue(1.0)
    assert not a.isEmpty()
    assert a.toDouble() == 1.0
    assert a.valueType() == pyopenms.DataType.DOUBLE_VALUE

    a = pyopenms.DataValue("1")
    assert not a.isEmpty()
    assert a.toString() == "1"
    assert a.valueType() == pyopenms.DataType.STRING_VALUE

    a = pyopenms.DataValue([1])
    assert not a.isEmpty()
    assert a.toIntList() == [1]
    assert a.valueType() == pyopenms.DataType.INT_LIST

    a = pyopenms.DataValue([1.0])
    assert not a.isEmpty()
    assert a.toDoubleList() == [1.0]
    assert a.valueType() == pyopenms.DataType.DOUBLE_LIST

    a = pyopenms.DataValue(["1.0"])
    assert not a.isEmpty()
    assert a.toStringList() == ["1.0"]
    assert a.valueType() == pyopenms.DataType.STRING_LIST


def testDateTime():
    """
    @tests:
     DateTime.__init__
     DateTime.getDate
     DateTime.getTime
     DateTime.now
    """
    d = pyopenms.DateTime()
    assert isinstance( d.getDate(), str)
    assert isinstance( d.getTime(), str)
    d = pyopenms.DateTime.now()
    assert isinstance( d.getDate(), str)
    assert isinstance( d.getTime(), str)

def testFeature():
    """
    @tests:
     Feature.__init__
     Feature.clearUniqueId
     Feature.ensureUniqueId
     Feature.getCharge
     Feature.getIntensity
     Feature.getKeys
     Feature.getMZ
     Feature.getMetaValue
     Feature.getQuality
     Feature.getRT
     Feature.getUniqueId
     Feature.getWidth
     Feature.hasInvalidUniqueId
     Feature.hasValidUniqueId
     Feature.metaValueExists
     Feature.removeMetaValue
     Feature.setCharge
     Feature.setIntensity
     Feature.setMZ
     Feature.setMetaValue
     Feature.setQuality
     Feature.setRT
     Feature.setWidth
     Feature.__eq__
     Feature.__ge__
     Feature.__gt__
     Feature.__le__
     Feature.__lt__
     Feature.__ne__
     Feature.clearMetaInfo
    """
    f = pyopenms.Feature()
    _testMetaInfoInterface(f)
    _testUniqueIdInterface(f)

    assert f == f
    assert not f != f

    f.setCharge(-1)
    assert f.getCharge() == -1
    f.setIntensity(10.0)
    assert f.getIntensity() == 10.0
    f.setQuality(0, 20.0)
    assert f.getQuality(0) == 20.0
    f.setRT(30.0)
    assert f.getRT() == 30.0
    f.setWidth(40.0)
    assert f.getWidth() == 40.0


def testFeatureFinder():
    """
    @tests:
     FeatureFinder.__init__
     FeatureFinder.endProgress
     FeatureFinder.getLogType
     FeatureFinder.getParameters
     FeatureFinder.run
     FeatureFinder.setLogType
     FeatureFinder.setProgress
     FeatureFinder.startProgress
    """
    ff = pyopenms.FeatureFinder()
    name = pyopenms.FeatureFinderAlgorithmPicked.getProductName()
    ff.run(name, pyopenms.MSExperiment(), pyopenms.FeatureMap() ,
            pyopenms.Param(), pyopenms.FeatureMap())

    _testProgressLogger(ff)

    p = ff.getParameters(name)
    _testParam(p)


def _testParam(p):
    """
    @tests:
     Param.__init__
     Param.addTag
     Param.addTags
     Param.asDict
     Param.clearTags
     Param.copy
     Param.exists
     Param.getDescription
     Param.getEntry
     Param.getSectionDescription
     Param.getTags
     Param.getValue
     Param.hasTag
     Param.insert
     Param.load
     Param.setMaxFloat
     Param.setMaxInt
     Param.setMinFloat
     Param.setMinInt
     Param.setSectionDescription
     Param.setValidStrings
     Param.setValue
     Param.size
     Param.store
     Param.update
     Param.updateFrom
     Param.__eq__
     Param.__ge__
     Param.__gt__
     Param.__le__
     Param.__lt__
     Param.__ne__
     ParamEntry.__init__
     ParamEntry.description
     ParamEntry.isValid
     ParamEntry.max_float
     ParamEntry.max_int
     ParamEntry.min_float
     ParamEntry.min_int
     ParamEntry.name
     ParamEntry.tags
     ParamEntry.valid_strings
     ParamEntry.value
     ParamEntry.__eq__
     ParamEntry.__ge__
     ParamEntry.__gt__
     ParamEntry.__le__
     ParamEntry.__lt__
     ParamEntry.__ne__
    """

    assert p == p

    dd = p.asDict()
    assert len(dd) == p.size()
    assert isinstance(dd, dict)

    keys = dd.keys()
    for k in keys:
        value = p.getValue(k)
        desc  = p.getDescription(k)
        tags  = p.getTags(k)
        p.setValue(k, value, desc, tags)
        p.setValue(k, value, desc)
        assert p.exists(k)
        f = k.split(":")[0]
        p.setSectionDescription(f, k)
        assert p.getSectionDescription(f) == k

    assert not p.exists("asdflkj01231321321v")
    p.addTag(k, "a")
    p.addTags(k, ["b", "c"])
    assert sorted(p.getTags(k)) == ["a", "b", "c"]
    p.clearTags(k)
    assert p.getTags(k) == []

    pn = pyopenms.Param()
    pn.insert("master:", p)
    assert pn.exists("master:"+k)

    p1 = pn.copy("master:", True)
    assert p1 == p

    p1.update(p, True, False)

    p.setValidStrings
    p.setMinFloat
    p.setMaxFloat
    p.setMinInt
    p.setMaxInt
    p.store("test.ini")
    p1 = pyopenms.Param()
    p1.load("test.ini")
    assert p == p1

    e1 = p1.getEntry(k)
    for f in ["name", "description", "value", "tags", "valid_strings",
              "min_float", "max_float", "min_int", "max_int"]:
        assert getattr(e1, f) is not None

    assert e1 == e1



def testFeatureFinderAlgorithmPicked():
    """
    @tests:
     FeatureFinderAlgorithmPicked.__init__
     FeatureFinderAlgorithmPicked.getDefaults
     FeatureFinderAlgorithmPicked.getName
     FeatureFinderAlgorithmPicked.getParameters
     FeatureFinderAlgorithmPicked.getProductName
     FeatureFinderAlgorithmPicked.setName
     FeatureFinderAlgorithmPicked.setParameters
    """
    ff = pyopenms.FeatureFinderAlgorithmPicked()
    p = ff.getDefaults()
    _testParam(p)

    _testParam(ff.getParameters())

    assert ff.getName() == "FeatureFinderAlgorithm"
    assert pyopenms.FeatureFinderAlgorithmPicked.getProductName() == "centroided"

    ff.setParameters(pyopenms.Param())

    ff.setName("test")
    assert ff.getName() == "test"


def testFeatureMap():
    """
    @tests:
     FeatureMap.__init__
     FeatureMap.__add__
     FeatureMap.__iadd__
     FeatureMap.__radd__
     FeatureMap.__getitem__
     FeatureMap.clear
     FeatureMap.clearUniqueId
     FeatureMap.ensureUniqueId
     FeatureMap.getDataProcessing
     FeatureMap.getProteinIdentifications
     FeatureMap.getUnassignedPeptideIdentifications
     FeatureMap.getUniqueId
     FeatureMap.hasInvalidUniqueId
     FeatureMap.hasValidUniqueId
     FeatureMap.push_back
     FeatureMap.setDataProcessing
     FeatureMap.setProteinIdentifications
     FeatureMap.setUnassignedPeptideIdentifications
     FeatureMap.setUniqueIds
     FeatureMap.size
     FeatureMap.sortByIntensity
     FeatureMap.sortByMZ
     FeatureMap.sortByOverallQuality
     FeatureMap.sortByPosition
     FeatureMap.sortByRT
     FeatureMap.swap
     FeatureMap.updateRanges
    """
    fm = pyopenms.FeatureMap()
    _testUniqueIdInterface(fm)
    fm.clear()
    fm.clearUniqueId()

    f = pyopenms.Feature()
    fm.push_back(f)


    assert fm.size() == 1
    assert fm[0] == f

    fm.sortByIntensity()
    assert fm.size() == 1
    assert fm[0] == f

    fm.sortByIntensity(False)
    assert fm.size() == 1
    assert fm[0] == f

    fm.sortByPosition()
    assert fm.size() == 1
    assert fm[0] == f

    fm.sortByRT()
    assert fm.size() == 1
    assert fm[0] == f

    fm.sortByMZ()
    assert fm.size() == 1
    assert fm[0] == f

    fm.sortByOverallQuality()
    assert fm.size() == 1
    assert fm[0] == f

    fm2 = pyopenms.FeatureMap()

    fm.swap(fm2)
    assert fm2.size() == 1
    assert fm2[0] == f

    assert fm.size() == 0

    fm2.updateRanges()

    assert fm2.getProteinIdentifications() == []
    fm2.setProteinIdentifications([])

    assert fm2.getUnassignedPeptideIdentifications() == []
    fm2.setUnassignedPeptideIdentifications([])

    fm2.clear()
    assert fm2.size() == 0

    dp = pyopenms.DataProcessing()
    fm2.setDataProcessing([dp])
    assert fm2.getDataProcessing() == [dp]
    testDataProcessing(dp)

    fm2.setUniqueIds()

    fm += fm
    assert fm + fm != fm


def testFeatureXMLFile():
    """
    @tests:
     FeatureXMLFile.__init__
     FeatureXMLFile.load
     FeatureXMLFile.store
     FileHandler.__init__
     FileHandler.loadFeatures
    """

    fm = pyopenms.FeatureMap()
    fm.setUniqueIds()
    fh = pyopenms.FeatureXMLFile()
    fh.store("test.featureXML", fm)
    fh.load("test.featureXML", fm)

    fh = pyopenms.FileHandler()
    fh.loadFeatures("test.featureXML", fm)

def testFileHandler():
    """
    @tests:
     FileHandler.__init__
     FileHandler.getType
     FileHandler.loadExperiment
     FileHandler.storeExperiment
    """
    mse = pyopenms.MSExperiment()

    fh = pyopenms.FileHandler()
    fh.storeExperiment("test1.mzML", mse)
    fh.loadExperiment("test1.mzML", mse)
    fh.storeExperiment("test1.mzXML", mse)
    fh.loadExperiment("test1.mzXML", mse)
    fh.storeExperiment("test1.mzData", mse)
    fh.loadExperiment("test1.mzData", mse)

def testInstrumentSettings():
    """
    @tests:
     InstrumentSettings.__init__
     InstrumentSettings.clearMetaInfo
     InstrumentSettings.getKeys
     InstrumentSettings.getMetaValue
     InstrumentSettings.getPolarity
     InstrumentSettings.isMetaEmpty
     InstrumentSettings.metaValueExists
     InstrumentSettings.removeMetaValue
     InstrumentSettings.setMetaValue
     InstrumentSettings.setPolarity
     InstrumentSettings.__eq__
     InstrumentSettings.__ge__
     InstrumentSettings.__gt__
     InstrumentSettings.__le__
     InstrumentSettings.__lt__
     InstrumentSettings.__ne__
     """
    ins = pyopenms.InstrumentSettings()
    _testMetaInfoInterface(ins)
    ins.setPolarity(pyopenms.Polarity.NEGATIVE)
    assert ins.getPolarity() == pyopenms.Polarity.NEGATIVE

    assert ins == ins
    assert not ins != ins


def testLogType():

    """
    @tests:
     LogType.CMD
     LogType.GUI
     LogType.NONE
     """
    assert isinstance(pyopenms.LogType.CMD, int)
    assert isinstance(pyopenms.LogType.GUI, int)
    assert isinstance(pyopenms.LogType.NONE, int)

def testMSExperiment():
    """
    @tests:
     MSExperiment.__init__
     MSExperiment.getLoadedFilePath
     MSExperiment.getMaxMZ
     MSExperiment.getMaxRT
     MSExperiment.getMetaValue
     MSExperiment.getMinMZ
     MSExperiment.getMinRT
     MSExperiment.push_back
     MSExperiment.setLoadedFilePath
     MSExperiment.setMetaValue
     MSExperiment.size
     MSExperiment.sortSpectra
     MSExperiment.updateRanges
     MSExperiment.__eq__
     MSExperiment.__ge__
     MSExperiment.__getitem__
     MSExperiment.__gt__
     MSExperiment.__iter__
     MSExperiment.__le__
     MSExperiment.__lt__
     MSExperiment.__ne__
     MSExperiment.clearMetaInfo
     MSExperiment.getKeys
     MSExperiment.isMetaEmpty
     MSExperiment.metaValueExists
     MSExperiment.removeMetaValue
    """
    mse = pyopenms.MSExperiment()
    _testMetaInfoInterface(mse)
    mse.updateRanges()
    mse.sortSpectra(True)
    assert isinstance(mse.getMaxRT(), float)
    assert isinstance(mse.getMinRT(), float)
    assert isinstance(mse.getMaxMZ(), float)
    assert isinstance(mse.getMinMZ(), float)
    assert isinstance(mse.getLoadedFilePath(), str)
    mse.setLoadedFilePath("")
    assert mse.size() == 0

    mse.push_back(pyopenms.MSSpectrum())
    assert mse.size() == 1

    assert mse[0] is not None

    assert isinstance(list(mse), list)

    assert mse == mse
    assert not mse != mse

def testMSSpectrum():
    """
    @tests:
     MSSpectrum.clear
     MSSpectrum.clearMetaInfo
     MSSpectrum.findNearest
     MSSpectrum.getAcquisitionInfo
     MSSpectrum.getComment
     MSSpectrum.getDataProcessing
     MSSpectrum.getInstrumentSettings
     MSSpectrum.getKeys
     MSSpectrum.getMSLevel
     MSSpectrum.getMetaValue
     MSSpectrum.getName
     MSSpectrum.getNativeID
     MSSpectrum.getPeptideIdentifications
     MSSpectrum.getPrecursors
     MSSpectrum.getProducts
     MSSpectrum.getRT
     MSSpectrum.getSourceFile
     MSSpectrum.getType
     MSSpectrum.get_peaks
     MSSpectrum.intensityInRange
     MSSpectrum.isMetaEmpty
     MSSpectrum.metaValueExists
     MSSpectrum.push_back
     MSSpectrum.removeMetaValue
     MSSpectrum.setAcquisitionInfo
     MSSpectrum.setComment
     MSSpectrum.setDataProcessing
     MSSpectrum.setInstrumentSettings
     MSSpectrum.setMSLevel
     MSSpectrum.setMetaValue
     MSSpectrum.setName
     MSSpectrum.setNativeID
     MSSpectrum.setPeptideIdentifications
     MSSpectrum.setPrecursors
     MSSpectrum.setProducts
     MSSpectrum.setRT
     MSSpectrum.setSourceFile
     MSSpectrum.setType
     MSSpectrum.set_peaks
     MSSpectrum.size
     MSSpectrum.unify
     MSSpectrum.updateRanges
     MSSpectrum.__eq__
     MSSpectrum.__ge__
     MSSpectrum.__getitem__
     MSSpectrum.__gt__
     MSSpectrum.__le__
     MSSpectrum.__lt__
     MSSpectrum.__ne__
     """
    spec = pyopenms.MSSpectrum()
    _testMetaInfoInterface(spec)

    testSpectrumSetting(spec)

    spec.setRT(3.0)
    assert spec.getRT() == 3.0
    spec.setMSLevel(2)
    assert spec.getMSLevel() == 2
    spec.setName("spec")
    assert spec.getName() == "spec"

    p = pyopenms.Peak1D()
    p.setMZ(1000.0)
    p.setIntensity(200.0)

    spec.push_back(p)
    assert spec.size() == 1
    assert spec[0] == p

    spec.updateRanges()
    assert isinstance(spec.findNearest(0.0), int)

    assert spec == spec
    assert not spec != spec

    assert spec.get_peaks().shape == (1,2), spec.get_peaks().shape


def testMapAlignerAlgorithmPoseClustering():

    """
    @tests:
     MapAlignmentAlgorithmPoseClustering.__init__
     MapAlignmentAlgorithmPoseClustering.alignFeatureMaps
     MapAlignmentAlgorithmPoseClustering.alignPeakMaps
     MapAlignmentAlgorithmPoseClustering.fitModel
     MapAlignmentAlgorithmPoseClustering.getDefaults
     MapAlignmentAlgorithmPoseClustering.getName
     MapAlignmentAlgorithmPoseClustering.getParameters
     MapAlignmentAlgorithmPoseClustering.setName
     MapAlignmentAlgorithmPoseClustering.setParameters
     MapAlignmentAlgorithmPoseClustering.setReference
     MapAlignmentAlgorithmPoseClustering.transformFeatureMaps
     MapAlignmentAlgorithmPoseClustering.transformPeakMaps
     """
    ma = pyopenms.MapAlignmentAlgorithmPoseClustering()
    assert isinstance(ma.getDefaults(), pyopenms.Param)
    assert isinstance(ma.getParameters(), pyopenms.Param)
    assert isinstance(ma.getName(), str)

    ma.setReference(0, "")
    ma.alignFeatureMaps
    ma.alignPeakMaps
    pyopenms.MapAlignmentAlgorithmPoseClustering.transformPeakMaps
    pyopenms.MapAlignmentAlgorithmPoseClustering.transformFeatureMaps

def testMxxxFile():
    """
    @tests:
     MzDataFile.__init__
     MzDataFile.endProgress
     MzDataFile.getLogType
     MzDataFile.load
     MzDataFile.setLogType
     MzDataFile.setProgress
     MzDataFile.startProgress
     MzDataFile.store
     MzMLFile.__init__
     MzMLFile.endProgress
     MzMLFile.getLogType
     MzMLFile.load
     MzMLFile.setLogType
     MzMLFile.setProgress
     MzMLFile.startProgress
     MzMLFile.store
     MzXMLFile.__init__
     MzXMLFile.endProgress
     MzXMLFile.getLogType
     MzXMLFile.load
     MzXMLFile.setLogType
     MzXMLFile.setProgress
     MzXMLFile.startProgress
     MzXMLFile.store
    """
    mse = pyopenms.MSExperiment()

    fh = pyopenms.MzDataFile()
    _testProgressLogger(fh)
    fh.store("test.mzData", mse)
    fh.load("test.mzData", mse)

    fh = pyopenms.MzMLFile()
    _testProgressLogger(fh)
    fh.store("test.mzML", mse)
    fh.load("test.mzML", mse)

    fh = pyopenms.MzXMLFile()
    _testProgressLogger(fh)
    fh.store("test.mzXML", mse)
    fh.load("test.mzXML", mse)


def testPeak():

    """
    @tests:
     Peak1D.__init__
     Peak1D.getIntensity
     Peak1D.getMZ
     Peak1D.setIntensity
     Peak1D.setMZ
     Peak1D.__eq__
     Peak1D.__ge__
     Peak1D.__gt__
     Peak1D.__le__
     Peak1D.__lt__
     Peak1D.__ne__
     Peak2D.__init__
     Peak2D.getIntensity
     Peak2D.getMZ
     Peak2D.getRT
     Peak2D.setIntensity
     Peak2D.setMZ
     Peak2D.setRT
     Peak2D.__eq__
     Peak2D.__ge__
     Peak2D.__gt__
     Peak2D.__le__
     Peak2D.__lt__
     Peak2D.__ne__
    """
    p1 = pyopenms.Peak1D()
    p1.setIntensity(12.0)
    assert p1.getIntensity() == 12.0
    p1.setMZ(13.0)
    assert p1.getMZ() == 13.0

    assert p1 == p1
    assert not p1 != p1

    p2 = pyopenms.Peak2D()
    assert p2 == p2
    assert not p2 != p2
    p2.setIntensity(22.0)
    assert p2.getIntensity() == 22.0
    p2.setMZ(23.0)
    assert p2.getMZ() == 23.0
    p2.setRT(45.0)
    assert p2.getRT() == 45.0

def testPeakPickerHiRes():
    """
    @tests:
     PeakPickerHiRes.__init__
     PeakPickerHiRes.endProgress
     PeakPickerHiRes.getDefaults
     PeakPickerHiRes.getLogType
     PeakPickerHiRes.getName
     PeakPickerHiRes.getParameters
     PeakPickerHiRes.pick
     PeakPickerHiRes.pickExperiment
     PeakPickerHiRes.setLogType
     PeakPickerHiRes.setName
     PeakPickerHiRes.setParameters
     PeakPickerHiRes.setProgress
     PeakPickerHiRes.startProgress
    """

def testPeakTypeEstimator():
    """
    @tests:
     PeakTypeEstimator.__init__
     PeakTypeEstimator.estimateType
    """

    pyopenms.PeakTypeEstimator().estimateType(pyopenms.MSSpectrum())

def testPeptideHit():
    """
    @tests:
     PeptideHit.__init__
     PeptideHit.addProteinAccession
     PeptideHit.clearMetaInfo
     PeptideHit.getAAAfter
     PeptideHit.getAABefore
     PeptideHit.getKeys
     PeptideHit.getMetaValue
     PeptideHit.getProteinAccessions
     PeptideHit.getRank
     PeptideHit.getScore
     PeptideHit.getSequence
     PeptideHit.isMetaEmpty
     PeptideHit.metaValueExists
     PeptideHit.removeMetaValue
     PeptideHit.setAAAfter
     PeptideHit.setAABefore
     PeptideHit.setCharge
     PeptideHit.setMetaValue
     PeptideHit.setProteinAccessions
     PeptideHit.setRank
     PeptideHit.setScore
     PeptideHit.setSequence
     PeptideHit.__eq__
     PeptideHit.__ge__
     PeptideHit.__gt__
     PeptideHit.__le__
     PeptideHit.__lt__
     PeptideHit.__ne__
    """
    ph = pyopenms.PeptideHit()
    assert ph == ph
    assert not ph != ph

    ph = pyopenms.PeptideHit(1.0, 1, 0, pyopenms.AASequence("A"))
    _testMetaInfoInterface(ph)
    ph.addProteinAccession("A")
    assert ph.getProteinAccessions() == ["A"]

    assert ph.getScore() == 1.0
    assert ph.getRank() == 1
    assert ph.getSequence().toString() == "A"

    ph.setScore(2.0)
    assert ph.getScore() == 2.0
    ph.setRank(30)
    assert ph.getRank() == 30
    ph.setSequence(pyopenms.AASequence("AAA"))
    assert ph.getSequence().toString() == "AAA"

    ph.setAABefore('B')
    assert ph.getAABefore() == "B"
    ph.setAAAfter('C')
    assert ph.getAAAfter() == 'C'

    assert ph == ph
    assert not ph != ph


def testPeptideIdentification():
    """
    @tests:
     PeptideIdentification.__init__
     PeptideIdentification.assignRanks
     PeptideIdentification.clearMetaInfo
     PeptideIdentification.empty
     PeptideIdentification.getHits
     PeptideIdentification.getIdentifier
     PeptideIdentification.getKeys
     PeptideIdentification.getMetaValue
     PeptideIdentification.getNonReferencingHits
     PeptideIdentification.getReferencingHits
     PeptideIdentification.getScoreType
     PeptideIdentification.getSignificanceThreshold
     PeptideIdentification.insertHit
     PeptideIdentification.isHigherScoreBetter
     PeptideIdentification.isMetaEmpty
     PeptideIdentification.metaValueExists
     PeptideIdentification.removeMetaValue
     PeptideIdentification.setHigherScoreBetter
     PeptideIdentification.setHits
     PeptideIdentification.setIdentifier
     PeptideIdentification.setMetaValue
     PeptideIdentification.setScoreType
     PeptideIdentification.sort
     PeptideIdentification.__eq__
     PeptideIdentification.__ge__
     PeptideIdentification.__gt__
     PeptideIdentification.__le__
     PeptideIdentification.__lt__
     PeptideIdentification.__ne__
     """
    pi = pyopenms.PeptideIdentification()
    _testMetaInfoInterface(pi)
    assert pi == pi
    assert not pi != pi

    ph = pyopenms.PeptideHit(1.0, 1, 0, pyopenms.AASequence("A"))
    pi.insertHit(ph)
    phx, = pi.getHits()
    assert phx == ph

    pi.setHits([ph])
    phx, = pi.getHits()
    assert phx == ph

    assert isinstance(pi.getSignificanceThreshold(), float)
    assert isinstance(pi.getScoreType(), str)
    pi.setScoreType("A")
    assert isinstance(pi.isHigherScoreBetter(), int)
    assert isinstance(pi.getIdentifier(), str)
    pi.setIdentifier("id")
    pi.assignRanks()
    pi.sort()
    assert not pi.empty()

    rv = []
    pi.getReferencingHits("A", rv)
    assert rv == []
    pi.getNonReferencingHits("A", rv)
    hit, = rv
    assert hit.getSequence().toString()== "A"
    assert hit.getScore() == 1.0
    assert hit.getRank() == 1

    rv = []
    pi.getReferencingHits(["A"], rv)
    assert rv == []
    pi.getNonReferencingHits(["A"], rv)
    hit, = rv
    assert hit.getSequence().toString()== "A"
    assert hit.getScore() == 1.0
    assert hit.getRank() == 1

    ph = pyopenms.ProteinHit()
    pi.getReferencingHits([ph], rv)
    hit, = rv
    assert hit.getSequence().toString()== "A"
    assert hit.getScore() == 1.0
    assert hit.getRank() == 1
    rv = []
    pi.getNonReferencingHits([ph], rv)
    hit, = rv
    assert hit.getSequence().toString()== "A"
    assert hit.getScore() == 1.0
    assert hit.getRank() == 1


def testPolarity():
    """
    @tests:
     Polarity.NEGATIVE
     Polarity.POLNULL
     Polarity.POSITIVE
     Polarity.SIZE_OF_POLARITY
    """
    assert isinstance(pyopenms.Polarity.NEGATIVE, int)
    assert isinstance(pyopenms.Polarity.POLNULL, int)
    assert isinstance(pyopenms.Polarity.POSITIVE, int)


def testPrecursor():
    """
    @tests:
     Precursor.__init__
     Precursor.getIntensity
     Precursor.getMZ
     Precursor.setIntensity
     Precursor.setMZ
    """
    pc = pyopenms.Precursor()
    pc.setMZ(123.0)
    pc.setIntensity(12.0)
    assert pc.getMZ() == 123.0
    assert pc.getIntensity() == 12.0

def testProcessingAction():
    """
    @tests:
     ProcessingAction.ALIGNMENT
     ProcessingAction.BASELINE_REDUCTION
     ProcessingAction.CALIBRATION
     ProcessingAction.CHARGE_CALCULATION
     ProcessingAction.CHARGE_DECONVOLUTION
     ProcessingAction.CONVERSION_DTA
     ProcessingAction.CONVERSION_MZDATA
     ProcessingAction.CONVERSION_MZML
     ProcessingAction.CONVERSION_MZXML
     ProcessingAction.DATA_PROCESSING
     ProcessingAction.DEISOTOPING
     ProcessingAction.FEATURE_GROUPING
     ProcessingAction.FILTERING
     ProcessingAction.FORMAT_CONVERSION
     ProcessingAction.IDENTIFICATION_MAPPING
     ProcessingAction.NORMALIZATION
     ProcessingAction.PEAK_PICKING
     ProcessingAction.PRECURSOR_RECALCULATION
     ProcessingAction.QUANTITATION
     ProcessingAction.SIZE_OF_PROCESSINGACTION
     ProcessingAction.SMOOTHING
    """
    assert isinstance(pyopenms.ProcessingAction.ALIGNMENT, int)
    assert isinstance(pyopenms.ProcessingAction.BASELINE_REDUCTION, int)
    assert isinstance(pyopenms.ProcessingAction.CALIBRATION, int)
    assert isinstance(pyopenms.ProcessingAction.CHARGE_CALCULATION, int)
    assert isinstance(pyopenms.ProcessingAction.CHARGE_DECONVOLUTION, int)
    assert isinstance(pyopenms.ProcessingAction.CONVERSION_DTA, int)
    assert isinstance(pyopenms.ProcessingAction.CONVERSION_MZDATA, int)
    assert isinstance(pyopenms.ProcessingAction.CONVERSION_MZML, int)
    assert isinstance(pyopenms.ProcessingAction.CONVERSION_MZXML, int)
    assert isinstance(pyopenms.ProcessingAction.DATA_PROCESSING, int)
    assert isinstance(pyopenms.ProcessingAction.DEISOTOPING, int)
    assert isinstance(pyopenms.ProcessingAction.FEATURE_GROUPING, int)
    assert isinstance(pyopenms.ProcessingAction.FILTERING, int)
    assert isinstance(pyopenms.ProcessingAction.FORMAT_CONVERSION, int)
    assert isinstance(pyopenms.ProcessingAction.IDENTIFICATION_MAPPING, int)
    assert isinstance(pyopenms.ProcessingAction.NORMALIZATION, int)
    assert isinstance(pyopenms.ProcessingAction.PEAK_PICKING, int)
    assert isinstance(pyopenms.ProcessingAction.PRECURSOR_RECALCULATION, int)
    assert isinstance(pyopenms.ProcessingAction.QUANTITATION, int)
    assert isinstance(pyopenms.ProcessingAction.SIZE_OF_PROCESSINGACTION, int)
    assert isinstance(pyopenms.ProcessingAction.SMOOTHING, int)


def testProduct():
    """
    @tests:
     Product.__init__
     Product.getIsolationWindowLowerOffset
     Product.getIsolationWindowUpperOffset
     Product.getMZ
     Product.setIsolationWindowLowerOffset
     Product.setIsolationWindowUpperOffset
     Product.setMZ
     Product.__eq__
     Product.__ge__
     Product.__gt__
     Product.__le__
     Product.__lt__
     Product.__ne__
    """
    p = pyopenms.Product()
    p.setMZ(12.0)
    p.setIsolationWindowLowerOffset(10.0)
    p.setIsolationWindowUpperOffset(15.0)
    assert p.getMZ() == 12.0
    assert p.getIsolationWindowLowerOffset() == 10.0
    assert p.getIsolationWindowUpperOffset() == 15.0

    assert p == p
    assert not p != p

def testProteinHit():
    """
    @tests:
     ProteinHit.__init__
     ProteinHit.clearMetaInfo
     ProteinHit.getAccession
     ProteinHit.getCoverage
     ProteinHit.getKeys
     ProteinHit.getMetaValue
     ProteinHit.setMetaValue
     ProteinHit.getRank
     ProteinHit.__eq__
     ProteinHit.__ge__
     ProteinHit.__gt__
     ProteinHit.__le__
     ProteinHit.__lt__
     ProteinHit.__ne__
     ProteinHit.getScore
     ProteinHit.getSequence
     ProteinHit.isMetaEmpty
     ProteinHit.metaValueExists
     ProteinHit.removeMetaValue
     ProteinHit.setAccession
     ProteinHit.setCoverage
     ProteinHit.setRank
     ProteinHit.setScore
     ProteinHit.setSequence
     """
    ph = pyopenms.ProteinHit()
    assert ph == ph
    assert not ph != ph
    _testMetaInfoInterface(ph)
    ph.setAccession("A")
    ph.setCoverage(0.5)
    ph.setRank(2)
    ph.setScore(1.5)
    ph.setSequence("ABA")
    assert ph.getAccession() == ("A")
    assert ph.getCoverage() == (0.5)
    assert ph.getRank() == (2)
    assert ph.getScore() == (1.5)
    assert ph.getSequence() == ("ABA")

def testProteinIdentification():
    """
    @tests:
     ProteinIdentification.DigestionEnzyme
     ProteinIdentification.PeakMassType
     ProteinIdentification.__init__
     ProteinIdentification.clearMetaInfo
     ProteinIdentification.getHits
     ProteinIdentification.getKeys
     ProteinIdentification.getMetaValue
     ProteinIdentification.insertHit
     ProteinIdentification.isMetaEmpty
     ProteinIdentification.metaValueExists
     ProteinIdentification.removeMetaValue
     ProteinIdentification.setHits
     ProteinIdentification.setMetaValue
     ProteinIdentification.__eq__
     ProteinIdentification.__ge__
     ProteinIdentification.__gt__
     ProteinIdentification.__le__
     ProteinIdentification.__lt__
     ProteinIdentification.__ne__
    """
    pi = pyopenms.ProteinIdentification()
    _testMetaInfoInterface(pi)
    assert pi == pi
    assert not pi != pi

    assert pi.getHits() == []
    ph = pyopenms.ProteinHit()
    pi.insertHit(ph)
    ph2, = pi.getHits()
    assert ph2 == ph

    pi.setHits([ph])
    ph2, = pi.getHits()
    assert ph2 == ph

    assert isinstance(pyopenms.ProteinIdentification.PeakMassType.MONOISOTOPIC, int)
    assert isinstance(pyopenms.ProteinIdentification.PeakMassType.AVERAGE, int)

    assert isinstance(pyopenms.ProteinIdentification.DigestionEnzyme.TRYPSIN,
            int)
    assert isinstance(pyopenms.ProteinIdentification.DigestionEnzyme.PEPSIN_A, int)
    assert isinstance(pyopenms.ProteinIdentification.DigestionEnzyme.PROTEASE_K,
            int)
    assert isinstance(pyopenms.ProteinIdentification.DigestionEnzyme.CHYMOTRYPSIN,
            int)
    assert isinstance(pyopenms.ProteinIdentification.DigestionEnzyme.NO_ENZYME, int)
    assert isinstance(pyopenms.ProteinIdentification.DigestionEnzyme.UNKNOWN_ENZYME,
            int)


def testRichPeak():
    """
    @tests:
     RichPeak1D.__init__
     RichPeak1D.getIntensity
     RichPeak1D.getKeys
     RichPeak1D.getMZ
     RichPeak1D.__eq__
     RichPeak1D.__ge__
     RichPeak1D.__gt__
     RichPeak1D.__le__
     RichPeak1D.__lt__
     RichPeak1D.__ne__
     RichPeak1D.getMetaValue
     RichPeak1D.clearMetaInfo
     RichPeak1D.isMetaEmpty
     RichPeak1D.metaValueExists
     RichPeak1D.removeMetaValue
     RichPeak1D.setIntensity
     RichPeak1D.setMZ
     RichPeak1D.setMetaValue
     RichPeak2D.__init__
     RichPeak2D.clearUniqueId
     RichPeak2D.clearMetaInfo
     RichPeak2D.isMetaEmpty
     RichPeak2D.ensureUniqueId
     RichPeak2D.getIntensity
     RichPeak2D.getKeys
     RichPeak2D.getMZ
     RichPeak2D.getMetaValue
     RichPeak2D.getRT
     RichPeak2D.getUniqueId
     RichPeak2D.hasInvalidUniqueId
     RichPeak2D.hasValidUniqueId
     RichPeak2D.metaValueExists
     RichPeak2D.removeMetaValue
     RichPeak2D.setIntensity
     RichPeak2D.setMZ
     RichPeak2D.setMetaValue
     RichPeak2D.setUniqueId
     RichPeak2D.setRT
     RichPeak2D.__eq__
     RichPeak2D.__ge__
     RichPeak2D.__gt__
     RichPeak2D.__le__
     RichPeak2D.__lt__
     RichPeak2D.__ne__
     """
    p1 = pyopenms.RichPeak1D()
    _testMetaInfoInterface(p1)
    assert p1 == p1
    assert not p1 != p1
    p1.setMZ(12.0)
    p1.setIntensity(23.0)
    assert p1.getMZ() == (12.0)
    assert p1.getIntensity() == (23.0)

    p2 = pyopenms.RichPeak2D()
    _testMetaInfoInterface(p2)
    _testUniqueIdInterface(p2)
    assert p2 == p2
    assert not p2 != p2
    p2.setMZ(22.0)
    p2.setIntensity(23.0)
    p2.setRT(43.0)
    assert p2.getMZ() == (22.0)
    assert p2.getIntensity() == (23.0)
    assert p2.getRT() == (43.0)


def testSoftware():
    """
    @tests:
     Software.__init__
     Software.getName
     Software.getVersion
     Software.setName
     Software.setVersion
    """
    sw = pyopenms.Software()
    sw.setName("name")
    sw.setVersion("1.0.0")
    assert sw.getName() == "name"
    assert sw.getVersion() == "1.0.0"



def testSourceFile():
    """
    @test:
     SourceFile.__init__
     SourceFile.getChecksum
     SourceFile.getChecksumType
     SourceFile.getFileSize
     SourceFile.getFileType
     SourceFile.getNameOfFile
     SourceFile.getNativeIDType
     SourceFile.getPathToFile
     SourceFile.setChecksum
     SourceFile.setFileSize
     SourceFile.setFileType
     SourceFile.setNameOfFile
     SourceFile.setNativeIDType
     SourceFile.setPathToFile
    """
    sf = pyopenms.SourceFile()
    sf.setNameOfFile("file.txt")
    assert sf.getNameOfFile() == "file.txt"
    sf.setPathToFile("file.txt")
    assert sf.getPathToFile() == "file.txt"
    sf.setFileType(".txt")
    assert sf.getFileType() == ".txt"
    sf.setChecksum("abcde000", pyopenms.ChecksumType.UNKNOWN_CHECKSUM)
    assert sf.getChecksum() == "abcde000"

    assert sf.getChecksumType() in (pyopenms.ChecksumType.UNKNOWN_CHECKSUM,
                                    pyopenms.ChecksumType.SHA1,
                                    pyopenms.ChecksumType.MD5)

def testSpectrumSetting(s=pyopenms.SpectrumSettings()):
    """
    @tests:
     SpectrumSettings.SpectrumType
     SpectrumSettings.__init__
     SpectrumSettings.getAcquisitionInfo
     SpectrumSettings.getComment
     SpectrumSettings.getDataProcessing
     SpectrumSettings.getInstrumentSettings
     SpectrumSettings.getNativeID
     SpectrumSettings.getPeptideIdentifications
     SpectrumSettings.getPrecursors
     SpectrumSettings.getProducts
     SpectrumSettings.getSourceFile
     SpectrumSettings.getType
     SpectrumSettings.setAcquisitionInfo
     SpectrumSettings.setComment
     SpectrumSettings.setDataProcessing
     SpectrumSettings.setInstrumentSettings
     SpectrumSettings.setNativeID
     SpectrumSettings.setPeptideIdentifications
     SpectrumSettings.setPrecursors
     SpectrumSettings.setProducts
     SpectrumSettings.setSourceFile
     SpectrumSettings.setType
     SpectrumSettings.unify
    """

    assert s.getType() in [ pyopenms.SpectrumSettings.SpectrumType.UNKNOWN,
                               pyopenms.SpectrumSettings.SpectrumType.PEAKS,
                               pyopenms.SpectrumSettings.SpectrumType.RAWDATA]

    assert isinstance(s.getAcquisitionInfo(), pyopenms.AcquisitionInfo)
    assert isinstance(s.getInstrumentSettings(), pyopenms.InstrumentSettings)
    assert isinstance(s.getSourceFile(), pyopenms.SourceFile)
    assert isinstance(s.getPeptideIdentifications(), list)
    assert isinstance(s.getDataProcessing(), list)

    s.setAcquisitionInfo(s.getAcquisitionInfo())
    s.setInstrumentSettings(s.getInstrumentSettings())
    s.setSourceFile(s.getSourceFile())
    s.setPeptideIdentifications(s.getPeptideIdentifications())
    s.setDataProcessing(s.getDataProcessing())
    s.setComment(s.getComment())
    s.setPrecursors(s.getPrecursors())
    s.setProducts(s.getProducts())
    s.setType(s.getType())
    s.setNativeID(s.getNativeID())
    s.setType(s.getType())
    if isinstance(s, pyopenms.SpectrumSettings):
        s.unify(s)


def testTransformationDescription():
    """
    @tests:
     TransformationDescription.__init__
     TransformationDescription.apply
     TransformationDescription.getDataPoints
    """
    td = pyopenms.TransformationDescription()
    assert td.getDataPoints() == []
    assert isinstance(td.apply(0.0), float)

def testTransformationModels():
    """
    @tests:
     TransformationModelBSpline.getDefaultParameters
     TransformationModelBSpline.getParameters
     TransformationModelInterpolated.getDefaultParameters
     TransformationModelInterpolated.getParameters
     TransformationModelLinear.getDefaultParameters
     TransformationModelLinear.getParameters
    """
    for clz in [pyopenms.TransformationModelBSpline,
                pyopenms.TransformationModelLinear,
                pyopenms.TransformationModelInterpolated]:
        mod = clz()
        p = pyopenms.Param()
        clz.getDefaultParameters(p)

def testTransformationXMLFile():
    """
    @tests:
     TransformationXMLFile.__init__
     TransformationXMLFile.load
     TransformationXMLFile.store
    """
    fh = pyopenms.TransformationXMLFile()
    td = pyopenms.TransformationDescription()
    fh.store("test.transformationXML", td)
    fh.load("test.transformationXML", td)
    assert td.getDataPoints() == []

def testType():
    """
    @tests:
     Type.CONSENSUSXML
     Type.DTA
     Type.DTA2D
     Type.EDTA
     Type.FASTA
     Type.FEATUREXML
     Type.GELML
     Type.HARDKLOER
     Type.IDXML
     Type.INI
     Type.KROENIK
     Type.MASCOTXML
     Type.MGF
     Type.MS2
     Type.MSP
     Type.MZDATA
     Type.MZIDENTML
     Type.MZML
     Type.MZXML
     Type.OMSSAXML
     Type.PEPLIST
     Type.PEPXML
     Type.PNG
     Type.PROTXML
     Type.SIZE_OF_TYPE
     Type.TOPPAS
     Type.TRAML
     Type.TRANSFORMATIONXML
     Type.TSV
     Type.UNKNOWN
     Type.XMASS
    """
    for ti in  [
      pyopenms.Type.CONSENSUSXML
     ,pyopenms.Type.DTA
     ,pyopenms.Type.DTA2D
     ,pyopenms.Type.EDTA
     ,pyopenms.Type.FASTA
     ,pyopenms.Type.FEATUREXML
     ,pyopenms.Type.GELML
     ,pyopenms.Type.HARDKLOER
     ,pyopenms.Type.IDXML
     ,pyopenms.Type.INI
     ,pyopenms.Type.KROENIK
     ,pyopenms.Type.MASCOTXML
     ,pyopenms.Type.MGF
     ,pyopenms.Type.MS2
     ,pyopenms.Type.MSP
     ,pyopenms.Type.MZDATA
     ,pyopenms.Type.MZIDENTML
     ,pyopenms.Type.MZML
     ,pyopenms.Type.MZXML
     ,pyopenms.Type.OMSSAXML
     ,pyopenms.Type.PEPLIST
     ,pyopenms.Type.PEPXML
     ,pyopenms.Type.PNG
     ,pyopenms.Type.PROTXML
     ,pyopenms.Type.SIZE_OF_TYPE
     ,pyopenms.Type.TOPPAS
     ,pyopenms.Type.TRAML
     ,pyopenms.Type.TRANSFORMATIONXML
     ,pyopenms.Type.TSV
     ,pyopenms.Type.UNKNOWN
     ,pyopenms.Type.XMASS]:
        assert isinstance(ti, int)

def testVersion():
    """
    @tests:
     VersionDetails.__init__
     VersionDetails.create
     VersionDetails.version_major
     VersionDetails.version_minor
     VersionDetails.version_patch
     VersionDetails.__eq__
     VersionDetails.__ge__
     VersionDetails.__gt__
     VersionDetails.__le__
     VersionDetails.__lt__
     VersionDetails.__ne__
     VersionInfo.getRevision
     VersionInfo.getTime
     VersionInfo.getVersion
     version.version
    """
    assert isinstance( pyopenms.VersionInfo.getVersion(), str)
    assert isinstance( pyopenms.VersionInfo.getRevision(), str)
    assert isinstance( pyopenms.VersionInfo.getTime(), str)

    vd = pyopenms.VersionDetails.create("19.2.1")
    assert vd.version_major == 19
    assert vd.version_minor == 2
    assert vd.version_patch == 1

    assert vd == vd
    assert not vd < vd
    assert not vd > vd

    assert  isinstance(pyopenms.version.version, str)
