#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grpcio
Version  : 1.17.1
Release  : 22
URL      : https://files.pythonhosted.org/packages/98/df/e181e36dc54fc0166d59cf2cb25991e33df52090922495175b2e2abc1381/grpcio-1.17.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/98/df/e181e36dc54fc0166d59cf2cb25991e33df52090922495175b2e2abc1381/grpcio-1.17.1.tar.gz
Summary  : HTTP/2-based RPC framework
Group    : Development/Tools
License  : Apache-2.0
Requires: grpcio-python = %{version}-%{release}
Requires: grpcio-python3 = %{version}-%{release}
Requires: coverage
Requires: enum34
Requires: futures
Requires: protobuf
Requires: six
Requires: wheel
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
===========
        
        Package for gRPC Python.
        
        Installation
        ------------
        
        gRPC Python is available for Linux, macOS, and Windows.
        
        From PyPI
        ~~~~~~~~~
        
        If you are installing locally...

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
%setup -q -n grpcio-1.17.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544885399
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
