Summary:	GTK program to rip CD audio and encode mp3s
Summary(pl):	Program pod GTK do ripowania p³yt CD i kodowania mp3
Name:		ripperX
Version:	2.5
Release:	1
License:	GPL
Group:		X11/Applications
Requires:	cdparanoia
Source0:	http://dl.sourceforge.net/ripperx/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/ripperx/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK program to rip CD audio and encode mp3s. Supports parallel
ripping/encoding, has plugins for cdparanoia, BladeEnc, Lame, GoGo,
FHG (l3enc and mp3enc), XingMp3enc, 8hz-mp3, and the ISO encoder. Also
has support for CDDB and ID3 tags.

%description -l pl
Program GTK do ripowania p³yt CD-Audio i kodowania mp3. Obs³uguje
równoleg³e ripowanie/kodowanie, ma wtyczki dla cdparanoia, BladeEnc,
Lame, GoGo, FHG (l3enc i mp3enc), XingMp3enc, 8hz-mp3 oraz koder ISO.
Ma tak¿e obs³ugê CDDB i tagów ID3.

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
%{_pixmapsdir}/ripperX-icon.xpm
%{_applnkdir}/Multimedia/ripperX.desktop
