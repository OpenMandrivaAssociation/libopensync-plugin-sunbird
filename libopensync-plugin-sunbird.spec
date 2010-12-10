%define svn	3218
%define rel	3
%if %svn
%define release		%mkrel 0.%svn.%rel
%define distname	%name-%svn.tar.lzma
%define dirname		%name
%else
%define release		%mkrel %rel
%define distname	%name-%version.tar.bz2
%define dirname		%name-%version
%endif

Name: 	 	libopensync-plugin-sunbird
Version: 	0.22.1
Epoch:		1
Release: 	%{release}
Summary: 	Sunbird synchronization plug-in for OpenSync
License:	LGPLv2+
Group:		Office
URL:		http://www.opensync.org
# For SVN:
# svn co http://svn.opensync.org/branches/branch-0.2X/plugins/sunbird libopensync-plugin-sunbird
Source0:	http://www.opensync.org/download/releases/%{distname}
# Don't add -Wall and -Werror to compiler flags, I'm not a fucking
# masochist - AdamW 2008/03
Patch0:		libopensync-plugin-sunbird-0.22.1-warning.patch
BuildRequires:	libopensync-devel < 0.30
BuildRequires:  libneon-devel
Requires:	libopensync >= %{epoch}:0.22
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plug-in allows applications using OpenSync to synchronize to and
from Mozilla Calendar / Sunbird.

%prep
%setup -q -n %{dirname}
%patch0 -p1 -b .warning
autoreconf -sfi

%build
%configure2_5x
make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*

