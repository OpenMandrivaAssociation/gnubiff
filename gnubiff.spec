%define version 2.2.8
%define release %mkrel 1
%define title GNUbiff

Summary:	Mail notification program
Name:		gnubiff
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Mail
URL:		http://gnubiff.sf.net/

Source:		http://prdownloads.sourceforge.net/gnubiff/%{name}-%{version}.tar.bz2

BuildRequires:	gnome-panel-devel
BuildRequires:	gtk2-devel >= 2.4.0
BuildRequires:	libglade2.0-devel >= 2.3.0
BuildRequires:	openssl-devel
BuildRequires:	ImageMagick
BuildRequires:	perl-XML-Parser
BuildRequires:  gamin-devel
BuildRequires: desktop-file-utils
Requires(post):	info-install
Requires(preun): info-install

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

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

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{title}
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;Network;Email;X-MandrivaLinux-Internet-Mail;
EOF

desktop-file-install --vendor="" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# icons
mkdir -p %{buildroot}%{_iconsdir} %{buildroot}%{_miconsdir}
install -m 644 -D       art/gnubiff.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 art/gnubiff.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 art/gnubiff.png %{buildroot}%{_miconsdir}/%{name}.png

%find_lang %{name}

%post
%{update_desktop_database}
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%postun
%{clean_desktop_database}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%{_infodir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

%files applet
%defattr(-, root, root)
%doc COPYING
%{_datadir}/gnome-2.0/ui/*.xml
%{_libdir}/bonobo/servers/*.server


