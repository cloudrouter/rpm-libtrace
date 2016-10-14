%define name libtrace
%define version 4.0.0

Summary: libtrace is a library for trace processing
License: GPL
URL: http://research.wand.net.nz/software/libtrace.php
Name: %{name}
Version: %{version}
Release: 1%{?dist}
Source: http://research.wand.net.nz/software/libtrace/libtrace-4.0.0.tar.bz2
Prefix: /usr
Group: System/Libraries
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libpcap-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: libwandio-devel

%description
libtrace is a library for trace processing. It supports multiple input methods, including device capture, raw and gz-compressed trace, and sockets; and mulitple input formats, including pcap and DAG.

%package devel
Summary: libtrace development headers
Group: System/Libraries
Provides: libtrace-devel

%description devel
This package contains necessary header files for libtrace development.

%package tools
Summary: libtrace tools
Group: System Environment/Tools
Provides: libtrace-tools

%description tools
Helper utilities for use with the libtrace process library.

%prep
%setup -q

%build
./configure --prefix %{_prefix} --libdir=%{_libdir}

# https://fedoraproject.org/wiki/RPath_Packaging_Draft
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc COPYING
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/libpacketdump/*.so
%{_libdir}/libpacketdump/*.protocol
%{_libdir}/*.so
%{_libdir}/*.a
%exclude %{_libdir}/*.la

%files tools
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Fri Oct 14 2016 John Siegrist <john@complects.com> - 4.0.0-1
- Update package version to 4.0.0.

* Thu Dec 24 2015 John Siegrist <john@complects.com> - 3.0.22-3
- Added missing BuildRequires dependencies.

* Sat Aug 29 2015 John Siegrist <jsiegrist@iix.net> - 3.0.22-2
- Added the dist macro to the Release version.

* Tue Jun 02 2015 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 3.0.22-1
- Initial specfile derrived from
  http://software.opensuse.org/download.html?project=home:cdwertmann:oml&package=libtrace

