#input-encoding: utf-8
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import glob
import os
import time
import autowrap
import shutil

decls = autowrap.parse(glob.glob(r"pyOpenMS\cython_code\selected_pxd\*.pxd"))
autowrap.generate(decls, r"pyOpenMS\cython_code\pyOpenMS.pyx", debug=True)

ext_modules = [Extension("pyOpenMS", ["pyOpenMS\cython_code\pyOpenMS.pyx"])]


#^setup(
#  name = 'pyOpenMS',
#  cmdclass = {'build_ext': build_ext},
#  ext_modules = ext_modules
#)

ctime = os.stat("pyOpenMS").st_mtime
ts = time.gmtime(ctime)
timestamp = "%02d-%02d-%4d" % (ts.tm_mday, ts.tm_mon, ts.tm_year)

from pyOpenMS.version import version
full_version= "%s_%s" % (version, timestamp)

# ADAPT THESE LINES ! ##################################

OPEN_MS_SRC = "e:/OpenMS-1.8/"

OPEN_MS_BUILD_DIR="e:/OpenMS-1.8_BUILD"
OPEN_MS_CONTRIB_BUILD_DIR=r"e:\OpenMS-1.8\contrib_build"
QT_HOME_DEVEL = r"C:\QtSDK\Desktop\Qt\4.7.3\msvc2008"

# ONLY ON WINDOWS: IF NOT WINDOWS: LET IT AS IT IS

MSVC_REDIST=r"C:\Programme\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT"
MSVCRDLL   ="msvcr90.dll"


###################################### ADAPT END #######

j=os.path.join

# package data must not be external, so copy here
local_share_dir = j("pyOpenMS", "share")
if not os.path.exists(local_share_dir):
    shutil.copytree(j(OPEN_MS_SRC, "share"), local_share_dir)

iswin = False

if sys.platform == "win32":
    iswin = True

    if not os.path.exists(j("pyOpenMS", MSVCRDLL)):
        shutil.copy(j(MSVC_REDIST, MSVCRDLL), "pyOpenMS")

    if not os.path.exists(j("pyOpenMS", "OpenMS.dll")):
        shutil.copy(j(OPEN_MS_BUILD_DIR, "bin", "OpenMS.dll"), "pyOpenMS")

    if not os.path.exists(j("pyOpenMS", "xerces-c_3_0.dll")):
        shutil.copy(j(OPEN_MS_CONTRIB_BUILD_DIR, "lib", "xerces-c_3_0.dll"), \
                    "pyOpenMS")

    libraries=["OpenMS", "xerces-c_3", "QtCore4", "gsl",
                        "cblas",
              ]

elif sys.platform == "linux2":

    libraries=["OpenMS", "xerces-c", "QtCore", "gsl",
                        "gslcblas",
              ]

else:
    print
    print "platform ", sys.platform, "not supported yet"
    print
    exit()

library_dirs=[OPEN_MS_BUILD_DIR, 
              j(OPEN_MS_CONTRIB_BUILD_DIR,"lib"),
              j(QT_HOME_DEVEL,"lib") ]


import numpy
include_dirs=[
              QT_HOME_DEVEL,                  # for linux
              j(QT_HOME_DEVEL, "QtCore"),     # for linux
              j(QT_HOME_DEVEL, "include"),
              j(QT_HOME_DEVEL, "include", "QtCore"),
              j(OPEN_MS_CONTRIB_BUILD_DIR, "include"),
              j(OPEN_MS_CONTRIB_BUILD_DIR, "src", "boost_1_42_0", "include", "boost-1_42"),
              j(OPEN_MS_SRC ,  "include"),
              j(numpy.core.__path__[0],"include"), 
             ]


ext = Extension(
        "pyOpenMS",
        sources = ["pyOpenMS/pyOpenMS.cpp"], 
        language="c++",
        library_dirs = library_dirs,
        libraries = libraries,
        include_dirs = include_dirs,
 
        # /EHs is important. It sets _CPPUNWIND which causes boost to
        # set BOOST_NO_EXCEPTION in <boost/config/compiler/visualc.hpp>
        # such that  boost::throw_excption() is declared but not implemented.
        # The linker does not like that very much ...
        extra_compile_args = iswin and [ "/EHs"] or []
     
    )


# share_data paths have to be relative to pyOpenMS not to ".",
# see the parameters when calling setup() below.
# so we have to strip a leading "pyOpenMS" in root:
share_data = []
for root, _, files in os.walk(local_share_dir):
    if ".svn" in root: continue #
    if ".git" in root: continue #
    fields = root.split(os.path.sep)
    if fields[0]=="pyOpenMS": 
        fields = fields[1:]
    # omit examples, make package too large and are not needed
    if len(fields) > 2 and fields[2] == "examples":
        continue
    root = os.path.sep.join(fields)
    for f in files:
        share_data.append(j(root, f))

if iswin:
    share_data +=[ "OpenMS.dll", MSVCRDLL, "xerces-c_3_0.dll"] 


share_data.append("License.txt")

#^setup(
#  name = 'pyOpenMS',
#  cmdclass = {'build_ext': build_ext},
#  ext_modules = ext_modules
#)
setup(

  name = "pyOpenMS",
  packages = ["pyOpenMS"],
  ext_package = "pyOpenMS",
  cmdclass = {'build_ext': build_ext},

  version = full_version,
  url="http://github.com/uweschmitt/msExpert",
  author="uwe schmitt",
  author_email="uschmitt@mineway.de",

  ext_modules = [ext ],
 
  package_data= { "pyOpenMS": share_data },
)