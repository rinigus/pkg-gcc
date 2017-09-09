Summary: Various compilers (C, C++, Objective-C, Java, ...)
Name: opt-gcc6
Version: 6.4.0
Release: 1%{?dist}
License: GPLv3+, GPLv3+ with exceptions and GPLv2+ with exceptions
Group: Development/Languages
Source0: gcc-6.4.0.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++ tar gmp-devel mpfr-devel mpc-devel libstdc++-devel
#Requires:

%define debug_package %{nil}

%description
The gcc package contains the GNU Compiler Collection. This package installs
all compilers in /opt/gcc6 directory.

%prep
%setup -q -n gcc-6.4.0

%build

mkdir obj
cd obj
$PWD/../configure --prefix=/opt/gcc6 --enable-languages=c,c++ --enable-cxx-flags="-fabi-version=8" --with-default-libstdcxx-abi=gcc4-compatible \
--enable-linker-build-id --enable-threads=posix --enable-shared \
%ifarch i486
--with-arch=i686 --with-fpmath=sse  \
%endif
%ifarch armv7hl
--disable-lto --with-float=hard --with-fpu=neon --with-arch=armv7-a --with-mode=thumb \
%endif

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd obj
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre

%post

%postun

%files
%defattr(-, root, root, 0755)
/opt/gcc6

%changelog
* Mon Sep 4 2017 rinigus <rinigus.git@gmail.com> - 6.4.0-1
- testing packaging for SFOS
