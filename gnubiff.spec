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
%{_libdir}/bonobo/servers/*.server
