# pkg-gcc

RPM packaging of GCC for Sailfish. 

This package installs GCC (C and C++) together with its libraries and
headers into /opt/gcc6 . Compiler is configured to use the same ABI as
4.8 series of GCC (`-fabi-version=8 --with-default-libstdcxx-abi=gcc4-compatible`).
This should allow to use the compiled programs on current SFOS and mix the
objects compiled with the different compilers (/opt/gcc6/bin/g++ and
/usr/bin/g++).

Here gcc spec is developed and issues can be filed against packaging
in /opt.
