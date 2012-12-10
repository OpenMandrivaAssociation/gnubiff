%define title GNUbiff

Summary:	Mail notification program
Name:		gnubiff
Version:	2.2.15
Release:	1
License:	GPLv3+
Group:		Networking/Mail
URL:		http://gnubiff.sf.net/
Source:		http://prdownloads.sourceforge.net/gnubiff/%{name}-%{version}.tar.gz
Patch0:		gnubiff-2.2.15-linkage.patch
BuildRequires:	pkgconfig(gamin)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libpanelapplet-4.0)
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	openssl-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	popt-devel
Requires:	sox

%description
%{name} is a mail notification program that periodically checks for mail
and displays headers and/or content when new mail has arrived. It relies
on the GNOME and GTK libraries but can be compiled and used with or
without GNOME support. Supported protocols are pop3, apop, imap4, mh,
qmail, mailfile and SSL. Furthermore, gnubiff is fully configurable with
a lot of options like polltime, poptime, sounds, mail reader, mailbox
title, etc.

%package	applet
Summary:	GNOME applet of gnubiff, a mail notification program
Group:		Networking/Mail
Requires:	%{name} = %{version}

%description	applet
%{name} is a mail notification program that periodically checks for mail
and displays headers and/or content when new mail has arrived. It relies
on the GNOME and GTK libraries but can be compiled and used with or
without GNOME support. Supported protocols are pop3, apop, imap4, mh,
qmail, mailfile and SSL. Furthermore, gnubiff is fully configurable with
a lot of options like polltime, poptime, sounds, mail reader, mailbox
title, etc.

This package contains the GNOME applet of %{name}.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --disable-rpath
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# icons
mkdir -p %{buildroot}%{_iconsdir} %{buildroot}%{_miconsdir}
install -m 644 -D       art/gnubiff.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 art/gnubiff.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 art/gnubiff.png %{buildroot}%{_miconsdir}/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%{_infodir}/*
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

%files applet
%doc COPYING
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/gnome-panel/4.0/applets/*.panel-applet


%changelog
* Wed Jun 13 2012 Andrey Bondrov <abondrov@mandriva.org> 2.2.15-1
+ Revision: 805451
- Update file list
- Add patch0 to fix linkage
- Update BuildRequires
- New version 2.2.15, switch to Gnome3 and GTK3
- Update BuildRequires
- Drop some legacy junk

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 2.2.13-2mdv2010.1
+ Revision: 537372
- rebuild

* Sun Feb 07 2010 Funda Wang <fwang@mandriva.org> 2.2.13-1mdv2010.1
+ Revision: 501653
- BR intltool
- New version 2.2.13

* Wed Jul 29 2009 Frederik Himpe <fhimpe@mandriva.org> 2.2.11-1mdv2010.0
+ Revision: 404242
- Update to new version 2.2.11
- Fix license
- Add patch from Fedora to fix build
- Add patch fixing string format

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.2.10-2mdv2009.0
+ Revision: 266941
- rebuild early 2009.0 package (before pixel changes)

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 2.2.10-1mdv2009.0
+ Revision: 213880
- update to new version 2.2.10

* Sun Feb 03 2008 Funda Wang <fwang@mandriva.org> 2.2.9-1mdv2008.1
+ Revision: 161819
- update to new version 2.2.9

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 09 2007 J茅r么me Soyer <saispo@mandriva.org> 2.2.8-1mdv2008.1
+ Revision: 96039
- New release 2.2.8

* Mon Aug 13 2007 J茅r么me Soyer <saispo@mandriva.org> 2.2.7-1mdv2008.0
+ Revision: 62449
- New release 2.2.7

* Wed Apr 25 2007 J茅r么me Soyer <saispo@mandriva.org> 2.2.6-1mdv2008.0
+ Revision: 18141
- New release 2.2.6


* Mon Jan 29 2007 Lenny Cartier <lenny@mandriva.com> 2.2.5-1mdv2007.0
+ Revision: 114836
- Update to 2.2.5

* Mon Dec 11 2006 J茅r么me Soyer <saispo@mandriva.org> 2.2.4-2mdv2007.1
+ Revision: 94690
- Fix BuildRequires for x86_64
- New version 2.2.4
- Import gnubiff

* Wed Aug 09 2006 Jerome Soyer <saispo@mandriva.org> 2.2.2-1mdv2007.0
- 2.2.2
- XDG Menu

* Wed May 24 2006 Lenny Cartier <lenny@mandriva.com> 2.2.1-1mdk
- 2.2.1

* Fri Apr 14 2006 Jerome Soyer <saispo@mandriva.org> 2.2.0-1mdk
- New release 2.2.0

* Tue Jan 31 2006 Jerome Soyer <saispo@mandriva.org> 2.1.9-1mdk
- New release 2.1.9

* Tue Dec 20 2005 Nicolas L閏ureuil <neoclust@mandriva.org> 2.1.8-2mdk
- Fix PreReq
- Add BuildRequires ( gmain-devel )

* Tue Dec 20 2005 Lenny Cartier <lenny@mandriva.com> 2.1.8-1mdk
- 2.1.8

* Thu Jun 30 2005 Lenny Cartier <lenny@mandriva.com> 2.1.4-1mdk
- 2.1.4

* Tue Apr 05 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.1.3-1mdk
- 2.1.3

* Sun Dec 26 2004 Abel Cheung <deaddog@mandrake.org> 2.1.0-1mdk
- 2.1.0, work done by Marc Koschewski <marc@osknowledge.org>

* Thu Dec 02 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.0.3-1mdk
- 2.0.3

* Sun Nov 21 2004 Abel Cheung <deaddog@mandrake.org> 2.0.2-2mdk
- Fix BuildRequires (thx Stefan's bot)

* Thu Oct 21 2004 G枚tz Waschk <waschk@linux-mandrake.com> 2.0.2-1mdk
- update file list
- rediff the patch
- new source URL
- New release 2.0.2

* Tue Jun 29 2004 Abel Cheung <deaddog@deaddog.org> 1.4.0-1mdk
- New version

* Sun Jun 20 2004 Abel Cheung <deaddog@deaddog.org> 1.2.0-2mdk
- Rebuild with new gcc

* Wed May 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.0-1mdk
- 1.2.0

* Mon Feb 16 2004 Abel Cheung <deaddog@deaddog.org> 1.0.9-1mdk
- First Mandrake package
- Patch0: Add missing info entry for info file

