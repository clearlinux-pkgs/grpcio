#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grpcio
Version  : 1.16.0
Release  : 19
URL      : https://files.pythonhosted.org/packages/be/84/9afa550ae7bfc65a7150f66ecdbf267617a2d584d9f845b4ef7d026a24ad/grpcio-1.16.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/be/84/9afa550ae7bfc65a7150f66ecdbf267617a2d584d9f845b4ef7d026a24ad/grpcio-1.16.0.tar.gz
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
%setup -q -n grpcio-1.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540461356
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
