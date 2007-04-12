%define name	libopensync-plugin-sunbird
%define version	0.20
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Mozilla Calendar / Sunbird Synchronization Plug-In for OpenSync
Version: 	%{version}
Release: 	%{release}

Source:		svn://svn.opensync.org/plugins/sunbird/%{name}-%{version}.tar.bz2
URL:		http://www.opensync.org
License:	LGPL
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires:	opensync-devel >= 0.20
BuildRequires:  libneon-devel

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*


