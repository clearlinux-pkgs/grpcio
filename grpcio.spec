#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grpcio
Version  : 1.32.0
Release  : 48
URL      : https://files.pythonhosted.org/packages/0e/5f/eeb402746a65839acdec78b7e757635f5e446138cc1d68589dfa32cba593/grpcio-1.32.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/0e/5f/eeb402746a65839acdec78b7e757635f5e446138cc1d68589dfa32cba593/grpcio-1.32.0.tar.gz
Summary  : HTTP/2-based RPC framework
Group    : Development/Tools
License  : Apache-2.0
Requires: grpcio-license = %{version}-%{release}
Requires: grpcio-python = %{version}-%{release}
Requires: grpcio-python3 = %{version}-%{release}
Requires: Cython
Requires: coverage
Requires: protobuf
Requires: six
Requires: wheel
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : protobuf
BuildRequires : python3-dev
BuildRequires : six
BuildRequires : wheel

%description
===========
        
        |compat_check_pypi|
        
        Package for gRPC Python.

%package license
Summary: license components for the grpcio package.
Group: Default

%description license
license components for the grpcio package.


%package python
Summary: python components for the grpcio package.
Group: Default
Requires: grpcio-python3 = %{version}-%{release}

%description python
python components for the grpcio package.


%package python3
Summary: python3 components for the grpcio package.
Group: Default
Requires: python3-core
Provides: pypi(grpcio)
Requires: pypi(six)

%description python3
python3 components for the grpcio package.


%prep
%setup -q -n grpcio-1.32.0
cd %{_builddir}/grpcio-1.32.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599762139
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/grpcio
cp %{_builddir}/grpcio-1.32.0/LICENSE %{buildroot}/usr/share/package-licenses/grpcio/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grpcio/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
