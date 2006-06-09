Summary:	GTK+ program to rip CD audio and encode MP3s, Ogg, FLAC
Summary(pl):	Program pod GTK+ do ripowania p³yt CD i kodowania MP3, Ogg, FLAC
Name:		ripperX
Version:	2.7.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/ripperx/%{name}-%{version}.tar.gz
# Source0-md5:	bf69f2cbfb52551ac18e713e9894f306
Patch0:		%{name}-desktop.patch
URL:		http://ripperx.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.1.13
BuildRequires:	id3lib-devel
Requires:	cdparanoia-III
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ program to rip CD audio and encode MP3s, Ogg, FLAC. Supports
parallel ripping/encoding, has plugins for cdparanoia, BladeEnc,
Lame, GoGo, FHG (l3enc and mp3enc), XingMp3enc, 8hz-MP3, and the
ISO encoder. Also has support for CDDB and ID3 tags.

%description -l pl
Program GTK+ do ripowania p³yt CD-Audio i kodowania MP3, Ogg, Flac.
Obs³uguje równoleg³e ripowanie/kodowanie, ma wtyczki dla cdparanoia,
BladeEnc, Lame, GoGo, FHG (l3enc i mp3enc), XingMp3enc, 8hz-MP3
oraz koder ISO. Ma tak¿e obs³ugê CDDB i znaczników ID3.

%prep
%setup -q
%patch0 -p1

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_mandir}/man1}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir}

install src/xpms/ripperX-icon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install ripperX.desktop $RPM_BUILD_ROOT%{_desktopdir}
install ripperX.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ README README.plugin README.plugin_spec_v0.1 TODO CHANGES BUGS
%attr(755,root,root) %{_bindir}/ripperX
%attr(755,root,root) %{_bindir}/ripperX_plugin-cdparanoia
%attr(755,root,root) %{_bindir}/ripperX_plugin-encode
%attr(755,root,root) %{_bindir}/ripperX_plugin-8hz-mp3
%attr(755,root,root) %{_bindir}/ripperX_plugin-lame
%attr(755,root,root) %{_bindir}/ripperX_plugin-gogo
%attr(755,root,root) %{_bindir}/ripperX_plugin-oggenc
%attr(755,root,root) %{_bindir}/ripperX_plugin-bladeenc
%attr(755,root,root) %{_bindir}/ripperX_plugin-xingmp3enc
%attr(755,root,root) %{_bindir}/ripperX_plugin-l3enc
%attr(755,root,root) %{_bindir}/ripperX_plugin-mp3enc
%attr(755,root,root) %{_bindir}/ripperX_plugin-flac
%attr(755,root,root) %{_bindir}/ripperX_plugin-toolame
%{_pixmapsdir}/ripperX-icon.xpm
%{_desktopdir}/ripperX.desktop
%{_mandir}/man1/ripperX.1*
