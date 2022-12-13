#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6DE2E9078E1F50C1 (william.c.roberts@intel.com)
#
Name     : tpm2-abrmd
Version  : 3.0.0
Release  : 13
URL      : https://github.com/tpm2-software/tpm2-abrmd/releases/download/3.0.0/tpm2-abrmd-3.0.0.tar.gz
Source0  : https://github.com/tpm2-software/tpm2-abrmd/releases/download/3.0.0/tpm2-abrmd-3.0.0.tar.gz
Source1  : https://github.com/tpm2-software/tpm2-abrmd/releases/download/3.0.0/tpm2-abrmd-3.0.0.tar.gz.asc
Summary  : TCTI library for communicating with the TPM2 access broker / resource manager daemon (tabrmd).
Group    : Development/Tools
License  : BSD-2-Clause
Requires: tpm2-abrmd-bin = %{version}-%{release}
Requires: tpm2-abrmd-data = %{version}-%{release}
Requires: tpm2-abrmd-lib = %{version}-%{release}
Requires: tpm2-abrmd-license = %{version}-%{release}
Requires: tpm2-abrmd-man = %{version}-%{release}
Requires: tpm2-abrmd-services = %{version}-%{release}
BuildRequires : pkgconfig(cmocka)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(tss2-mu)
BuildRequires : pkgconfig(tss2-rc)
BuildRequires : pkgconfig(tss2-sys)
BuildRequires : pkgconfig(tss2-tctildr)

%description
![Linux Build Status](https://github.com/tpm2-software/tpm2-abrmd/workflows/Linux%20Build%20Status/badge.svg)
[![FreeBSD Build Status](https://api.cirrus-ci.com/github/tpm2-software/tpm2-abrmd.svg?branch=master)](https://cirrus-ci.com/github/tpm2-software/tpm2-abrmd)
[![Coverity Scan](https://img.shields.io/coverity/scan/3997.svg)](https://scan.coverity.com/projects/01org-tpm2-abrmd)
[![codecov](https://codecov.io/gh/tpm2-software/tpm2-abrmd/branch/master/graph/badge.svg)](https://codecov.io/gh/tpm2-software/tpm2-abrmd)
[![Language grade: C/C++](https://img.shields.io/lgtm/grade/cpp/g/tpm2-software/tpm2-abrmd.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tpm2-software/tpm2-abrmd/context:cpp)

%package bin
Summary: bin components for the tpm2-abrmd package.
Group: Binaries
Requires: tpm2-abrmd-data = %{version}-%{release}
Requires: tpm2-abrmd-license = %{version}-%{release}
Requires: tpm2-abrmd-services = %{version}-%{release}

%description bin
bin components for the tpm2-abrmd package.


%package data
Summary: data components for the tpm2-abrmd package.
Group: Data

%description data
data components for the tpm2-abrmd package.


%package dev
Summary: dev components for the tpm2-abrmd package.
Group: Development
Requires: tpm2-abrmd-lib = %{version}-%{release}
Requires: tpm2-abrmd-bin = %{version}-%{release}
Requires: tpm2-abrmd-data = %{version}-%{release}
Provides: tpm2-abrmd-devel = %{version}-%{release}
Requires: tpm2-abrmd = %{version}-%{release}

%description dev
dev components for the tpm2-abrmd package.


%package lib
Summary: lib components for the tpm2-abrmd package.
Group: Libraries
Requires: tpm2-abrmd-data = %{version}-%{release}
Requires: tpm2-abrmd-license = %{version}-%{release}

%description lib
lib components for the tpm2-abrmd package.


%package license
Summary: license components for the tpm2-abrmd package.
Group: Default

%description license
license components for the tpm2-abrmd package.


%package man
Summary: man components for the tpm2-abrmd package.
Group: Default

%description man
man components for the tpm2-abrmd package.


%package services
Summary: services components for the tpm2-abrmd package.
Group: Systemd services

%description services
services components for the tpm2-abrmd package.


%prep
%setup -q -n tpm2-abrmd-3.0.0
cd %{_builddir}/tpm2-abrmd-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670951480
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --with-dbuspolicydir=/usr/share/dbus-1/system.d \
--with-systemdsystemunitdir=/usr/lib/systemd/system \
--with-systemdpresetdir=/usr/lib/systemd/system-preset \
--datarootdir=/usr/share
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1670951480
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tpm2-abrmd
cp %{_builddir}/tpm2-abrmd-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/tpm2-abrmd/af62924ad3089277c413ea767486f404ac159ce1 || :
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system-preset/tpm2-abrmd.preset

%files bin
%defattr(-,root,root,-)
/usr/bin/tpm2-abrmd

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/com.intel.tss2.Tabrmd.service
/usr/share/dbus-1/system.d/tpm2-abrmd.conf

%files dev
%defattr(-,root,root,-)
/usr/include/tss2/tss2-tcti-tabrmd.h
/usr/lib64/libtss2-tcti-tabrmd.so
/usr/lib64/pkgconfig/tss2-tcti-tabrmd.pc
/usr/share/man/man3/Tss2_Tcti_Tabrmd_Init.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtss2-tcti-tabrmd.so.0
/usr/lib64/libtss2-tcti-tabrmd.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tpm2-abrmd/af62924ad3089277c413ea767486f404ac159ce1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man7/tss2-tcti-tabrmd.7
/usr/share/man/man8/tpm2-abrmd.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/tpm2-abrmd.service
