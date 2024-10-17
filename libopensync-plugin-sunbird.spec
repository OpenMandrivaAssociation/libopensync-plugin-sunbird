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
URL:		https://www.opensync.org
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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.22.1-0.3218.3mdv2011.0
+ Revision: 620205
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1:0.22.1-0.3218.2mdv2010.0
+ Revision: 429821
- rebuild

* Thu Mar 13 2008 Adam Williamson <awilliamson@mandriva.org> 1:0.22.1-0.3218.1mdv2008.1
+ Revision: 187323
- some cleanups
- revert to 0.22 based on latest 0.22 spec in SVN (use snapshot from upstream 0.2 SVN branch as it includes useful stable fixes since 0.22)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Apr 24 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2008.0
+ Revision: 18004
- new version


* Mon Jan 08 2007 Jérôme Soyer <saispo@mandriva.org> 0.20-1mdv2007.0
+ Revision: 105924
- Add BR
- Rebuild
- Import libopensync-plugin-sunbird

