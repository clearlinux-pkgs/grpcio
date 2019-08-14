#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grpcio
Version  : 1.22.0
Release  : 29
URL      : https://files.pythonhosted.org/packages/19/c1/bee35b6efcace3c77cb275c6465ba9e574d01acf9abf785253fdeed526f3/grpcio-1.22.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/19/c1/bee35b6efcace3c77cb275c6465ba9e574d01acf9abf785253fdeed526f3/grpcio-1.22.0.tar.gz
Summary  : HTTP/2-based RPC framework
Group    : Development/Tools
License  : Apache-2.0
Requires: grpcio-license = %{version}-%{release}
Requires: grpcio-python = %{version}-%{release}
Requires: grpcio-python3 = %{version}-%{release}
Requires: Cython
Requires: coverage
Requires: enum34
Requires: protobuf
Requires: six
Requires: wheel
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : enum34
BuildRequires : protobuf
BuildRequires : python3-dev
BuildRequires : six
BuildRequires : wheel
Patch1: Rename-gettid-functions.patch

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

%description python3
python3 components for the grpcio package.


%prep
%setup -q -n grpcio-1.22.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565813762
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/grpcio
cp LICENSE %{buildroot}/usr/share/package-licenses/grpcio/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grpcio/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
