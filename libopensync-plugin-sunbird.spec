%define name	libopensync-plugin-sunbird
%define version	0.22
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Mozilla Calendar / Sunbird Synchronization Plug-In for OpenSync
License:	LGPL
Group:		Office
URL:		http://www.opensync.org
Source:		svn://svn.opensync.org/plugins/sunbird/%{name}-%{version}.tar.bz2
BuildRequires:	opensync-devel >= 0.20
BuildRequires:  libneon-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plug-in allows applications using OpenSync to synchronize to and
from Mozilla Calendar / Sunbird.

Additionally install the libopensync package.

%prep
%setup -q
autoreconf -sfi

%build
%configure2_5x
make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
