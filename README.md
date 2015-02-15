

# Preliminary

set up paths.

http://eli.thegreenplace.net/2011/07/03/parsing-c-in-python-with-clang

```
export LD_LIBRARY_PATH=$(llvm-config --libdir):$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH:/llvm/lib/python2.7/site-packages/
```

# Reference

http://clang.llvm.org/docs/IntroductionToTheClangAST.html



# Show

clang -Xclang -ast-dump -fsyntax-only sample.cpp
