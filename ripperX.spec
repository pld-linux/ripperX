%define ver 2.0
%define prefix /usr
%define rel 1

Summary:	GTK program to rip CD audio and encode mp3s
Name:		ripperX
Version:	%{ver}
Release:	%{rel}
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	cdparanoia
Source0:	http://www.digitallabyrinth.com/linux/ripperX/%{name}-%{ver}.tar.gz
URL:		http://www.digitallabyrinth.com/linux/ripperX/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GTK program to rip CD audio and encode mp3s. Supports parallel
ripping/encoding, has plugins for cdparanoia, BladeEnc, Lame, GoGo,
FHG (l3enc and mp3enc), XingMp3enc, 8hz-mp3, and the ISO encoder. Also
has support for CDDB and ID3 tags.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -d $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install
strip $RPM_BUILD_ROOT%{_bindir}/* ||:
cp src/xpms/ripperX-icon.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp ripperX.desktop $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ README README.plugin README.plugin_spec_v0.1 README.plugin_tester TODO CHANGES COPYING BUGS
%attr(755,root,root) %{_bindir}/ripperX
%attr(755,root,root) %{_bindir}/ripperX_plugin-cdparanoia
%attr(755,root,root) %{_bindir}/ripperX_plugin-encode
%attr(755,root,root) %{_bindir}/ripperX_plugin-8hz-mp3
%attr(755,root,root) %{_bindir}/ripperX_plugin-lame
%attr(755,root,root) %{_bindir}/ripperX_plugin-gogo
%attr(755,root,root) %{_bindir}/ripperX_plugin-bladeenc
%attr(755,root,root) %{_bindir}/ripperX_plugin-xingmp3enc
%attr(755,root,root) %{_bindir}/ripperX_plugin-l3enc
%attr(755,root,root) %{_bindir}/ripperX_plugin-mp3enc
%{_datadir}/pixmaps/ripperX-icon.xpm
%{_applnkdir}/Multimedia/ripperX.desktop
