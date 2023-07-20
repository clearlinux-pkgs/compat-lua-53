#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
%define keepstatic 1
Name     : compat-lua-53
Version  : 5.3.6
Release  : 72
URL      : http://www.lua.org/ftp/lua-5.3.6.tar.gz
Source0  : http://www.lua.org/ftp/lua-5.3.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: compat-lua-53-bin = %{version}-%{release}
Requires: compat-lua-53-lib = %{version}-%{release}
Requires: compat-lua-53-man = %{version}-%{release}
BuildRequires : ncurses-dev
BuildRequires : readline-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Build-fixes.patch
Patch2: 0002-Add-scimark-as-PGO-profiling-workload.patch
Patch3: 0003-Add-option-for-pgo-profiling-test-with-scimark.patch

%description
This is Lua 5.3.6, released on 14 Sep 2020.
For installation instructions, license details, and
further information about Lua, see doc/readme.html.

%package bin
Summary: bin components for the compat-lua-53 package.
Group: Binaries

%description bin
bin components for the compat-lua-53 package.


%package dev
Summary: dev components for the compat-lua-53 package.
Group: Development
Requires: compat-lua-53-lib = %{version}-%{release}
Requires: compat-lua-53-bin = %{version}-%{release}
Provides: compat-lua-53-devel = %{version}-%{release}
Requires: compat-lua-53 = %{version}-%{release}

%description dev
dev components for the compat-lua-53 package.


%package lib
Summary: lib components for the compat-lua-53 package.
Group: Libraries

%description lib
lib components for the compat-lua-53 package.


%package man
Summary: man components for the compat-lua-53 package.
Group: Default

%description man
man components for the compat-lua-53 package.


%package staticdev
Summary: staticdev components for the compat-lua-53 package.
Group: Default
Requires: compat-lua-53-dev = %{version}-%{release}

%description staticdev
staticdev components for the compat-lua-53 package.


%prep
%setup -q -n lua-5.3.6
cd %{_builddir}/lua-5.3.6
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689829468
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" LDFLAGS="${LDFLAGS_GENERATE}"
make  %{?_smp_mflags}  linux MYCFLAGS="${CFLAGS} -fpic -DLUA_COMPAT_5_2 -DLUA_COMPAT_5_1" MYLDFLAGS="${CFLAGS}" MYLIBS="-lncurses -lm"

make test_pgo
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" LDFLAGS="${LDFLAGS_USE}"
make  %{?_smp_mflags}  linux MYCFLAGS="${CFLAGS} -fpic -DLUA_COMPAT_5_2 -DLUA_COMPAT_5_1" MYLDFLAGS="${CFLAGS}" MYLIBS="-lncurses -lm"


%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make test

%install
export SOURCE_DATE_EPOCH=1689829468
rm -rf %{buildroot}
%make_install INSTALL_TOP=%{buildroot}/usr/
## install_append content
mkdir -p %{buildroot}/usr/lib64/pkgconfig
cp lua53.pc %{buildroot}/usr/lib64/pkgconfig/lua53.pc
mv %{buildroot}/usr/bin/lua %{buildroot}/usr/bin/lua5.3
mv %{buildroot}/usr/bin/luac %{buildroot}/usr/bin/luac5.3
mv %{buildroot}/usr/share/man/man1/lua.1 %{buildroot}/usr/share/man/man1/lua5.3.1
mv %{buildroot}/usr/share/man/man1/luac.1 %{buildroot}/usr/share/man/man1/luac5.3.1
mv src/liblua.a %{buildroot}/usr/lib64/liblua5.3.a
mkdir -p %{buildroot}/usr/include/lua-5.3/
mv %{buildroot}/usr/include/*.{h,hpp} %{buildroot}/usr/include/lua-5.3/
rm %{buildroot}/usr/lib64/liblua.a
rm -rf %{buildroot}/usr/lib64/liblua.so
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lua5.3
/usr/bin/luac5.3

%files dev
%defattr(-,root,root,-)
/usr/include/lua-5.3/lauxlib.h
/usr/include/lua-5.3/lua.h
/usr/include/lua-5.3/lua.hpp
/usr/include/lua-5.3/luaconf.h
/usr/include/lua-5.3/lualib.h
/usr/lib64/pkgconfig/lua53.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblua.so.5.3
/usr/lib64/liblua.so.5.3.6

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lua5.3.1
/usr/share/man/man1/luac5.3.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/liblua5.3.a
