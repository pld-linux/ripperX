Summary:	GTK program to rip CD audio and encode mp3s
Summary(pl):	Program pod GTK do ripowania p�yt CD i kodowania mp3
Name:		ripperX
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	cdparanoia
Source0:	http://www.digitallabyrinth.com/linux/ripperX/%{name}-%{version}.tar.gz
URL:		http://www.digitallabyrinth.com/linux/ripperX/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GTK program to rip CD audio and encode mp3s. Supports parallel
ripping/encoding, has plugins for cdparanoia, BladeEnc, Lame, GoGo,
FHG (l3enc and mp3enc), XingMp3enc, 8hz-mp3, and the ISO encoder. Also
has support for CDDB and ID3 tags.

%description -l pl
Program GTK do ripowania p�yt CD-Audio i kodowania mp3. Obs�uguje
r�wnoleg�e ripowanie/kodowanie, ma wtyczki dla cdparanoia, BladeEnc,
Lame, GoGo, FHG (l3enc i mp3enc), XingMp3enc, 8hz-mp3 oraz koder ISO.
Ma tak�e obs�ug� CDDB i tag�w ID3.

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
install src/xpms/ripperX-icon.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps
install ripperX.desktop $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

gzip -9nf FAQ README README.plugin README.plugin_spec_v0.1 README_plugin_tester TODO CHANGES BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {FAQ,README,README.plugin,README.plugin_spec_v0.1,README.plugin_tester,TODO,CHANGES,BUGS}.gz
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
%{_pixmapsdir}/ripperX-icon.xpm
%{_applnkdir}/Multimedia/ripperX.desktop
