%define ver 2.0
%define prefix /usr
%define rel 1

Summary: GTK program to rip CD audio and encode mp3s
Name: ripperX
Prefix: %prefix
Version: %ver
Release: %rel
Copyright: GPL
Group: X11/Applications
Requires: cdparanoia
Source: http://www.digitallabyrinth.com/linux/ripperX/ripperX-%{ver}.tar.gz
URL: http://www.digitallabyrinth.com/linux/ripperX/index.html
Packager: Scott Sams <sbsams@digitallabyrinth.com>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Docdir: %{prefix}/doc

%description
GTK program to rip CD audio and encode mp3s. Supports parallel
ripping/encoding, has plugins for cdparanoia, BladeEnc, Lame, 
GoGo, FHG (l3enc and mp3enc), XingMp3enc, 8hz-mp3, and the 
ISO encoder.  Also has support for CDDB and ID3 tags.

%prep
%setup

%build
./configure --prefix=%{prefix}
make

%install
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/share/pixmaps
mkdir -p $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Multimedia
make prefix=$RPM_BUILD_ROOT%{prefix} install
strip $RPM_BUILD_ROOT%{prefix}/bin/* ||:
cp src/xpms/ripperX-icon.xpm $RPM_BUILD_ROOT%{prefix}/share/pixmaps
cp ripperX.desktop $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Multimedia

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc FAQ README README.plugin README.plugin_spec_v0.1 README.plugin_tester TODO CHANGES COPYING BUGS
%{prefix}/bin/ripperX
%{prefix}/bin/ripperX_plugin-cdparanoia
%{prefix}/bin/ripperX_plugin-encode
%{prefix}/bin/ripperX_plugin-8hz-mp3
%{prefix}/bin/ripperX_plugin-lame
%{prefix}/bin/ripperX_plugin-gogo
%{prefix}/bin/ripperX_plugin-bladeenc
%{prefix}/bin/ripperX_plugin-xingmp3enc
%{prefix}/bin/ripperX_plugin-l3enc
%{prefix}/bin/ripperX_plugin-mp3enc
%{prefix}/share/pixmaps/ripperX-icon.xpm
%{prefix}/share/gnome/apps/Multimedia/ripperX.desktop

%changelog
* Mon Jan 03 2000 Dax Kelson <dax@gurulabs.com>
- Version 1.9
- Updated SPEC to use a $RPM_BUILD_ROOT, changelog, docs, and the strip binaries
- Created GNOME ".desktop" file so ripperX shows up on the menu
- Patch so cdparanoia fills files that are group writable, enabling shared directory ripping
