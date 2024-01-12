#ifndef Py_PYTHON_H
#define Py_PYTHON_H

#include "patchlevel.h"
#include "pyconfig.h"
#include "pymacconfig.h"



#include <assert.h>               
#include <inttypes.h>             
#include <limits.h>               
#include <math.h>                
#include <stdarg.h>               
#include <wchar.h>                
#ifdef HAVE_SYS_TYPES_H
#  include <sys/types.h>          
#endif

#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 < 0x030b0000
#  include <errno.h>              
#  include <stdio.h>              
#  include <stdlib.h>             
#  include <string.h>             
#endif
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 < 0x030d0000
#  include <ctype.h>              
#  ifndef MS_WINDOWS
#    include <unistd.h>           
#  endif
#endif



#include "pyport.h"
#include "pymacro.h"
#include "pymath.h"
#include "pymem.h"
#include "pytypedefs.h"
#include "pybuffer.h"
#include "pystats.h"
#include "pyatomic.h"
#include "object.h"
#include "objimpl.h"
#include "typeslots.h"
#include "pyhash.h"
#include "cpython/pydebug.h"
#include "bytearrayobject.h"
#include "bytesobject.h"
#include "unicodeobject.h"
#include "longobject.h"
#include "cpython/longintrepr.h"
#include "boolobject.h"
#include "floatobject.h"
#include "complexobject.h"
#include "rangeobject.h"
#include "memoryobject.h"
#include "tupleobject.h"
#include "listobject.h"
#include "dictobject.h"
#include "cpython/odictobject.h"
#include "enumobject.h"
#include "setobject.h"
#include "methodobject.h"
#include "moduleobject.h"
#include "cpython/funcobject.h"
#include "cpython/classobject.h"
#include "fileobject.h"
#include "pycapsule.h"
#include "cpython/code.h"
#include "pyframe.h"
#include "traceback.h"
#include "sliceobject.h"
#include "cpython/cellobject.h"
#include "iterobject.h"
#include "cpython/initconfig.h"
#include "pystate.h"
#include "cpython/genobject.h"
#include "descrobject.h"
#include "genericaliasobject.h"
#include "warnings.h"
#include "weakrefobject.h"
#include "structseq.h"
#include "cpython/picklebufobject.h"
#include "codecs.h"
#include "pyerrors.h"
#include "pythread.h"
#include "cpython/context.h"
#include "modsupport.h"
#include "compile.h"
#include "pythonrun.h"
#include "pylifecycle.h"
#include "ceval.h"
#include "sysmodule.h"
#include "osmodule.h"
#include "intrcheck.h"
#include "import.h"
#include "abstract.h"
#include "bltinmodule.h"
#include "cpython/pyctype.h"
#include "pystrtod.h"
#include "pystrcmp.h"
#include "fileutils.h"
#include "cpython/pyfpe.h"
#include "cpython/tracemalloc.h"
#include "cpython/optimizer.h"

#endif /* !Py_PYTHON_H */
