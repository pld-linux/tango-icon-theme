#
# TODO:
# - better summary and descriptions
# - check why 24x24 and scalable icon sets don't build correctly
# - add license
#
Summary:	freedesktop.org standard compliant icons
Summary(pl):	Ikony implementuj±ce standard freedesktop.org
Name:		tango-icon-theme
Version:	0.7.1
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://tango-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	78cee771a96eb1615df92350048a77f8
URL:		http://tango-project.org/Tango_Desktop_Project
BuildRequires:	ImageMagick-devel
BuildRequires:	icon-naming-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		tangodir	%{_iconsdir}/Tango

%description
freedesktop.org standard compliant icons.

%description -l pl
Ikony implementuj±ce standard freedesktop.org.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %{tangodir}
%{tangodir}/index.theme

%dir %{tangodir}/16x16
%dir %{tangodir}/16x16/actions
%{tangodir}/16x16/actions/*.png
%dir %{tangodir}/16x16/animations
%{tangodir}/16x16/animations/*.png
%dir %{tangodir}/16x16/apps
%{tangodir}/16x16/apps/*.png
%dir %{tangodir}/16x16/categories
%{tangodir}/16x16/categories/*.png
%dir %{tangodir}/16x16/devices
%{tangodir}/16x16/devices/*.png
%dir %{tangodir}/16x16/emblems
%{tangodir}/16x16/emblems/*.png
%dir %{tangodir}/16x16/emotes
%{tangodir}/16x16/emotes/*.png
%dir %{tangodir}/16x16/mimetypes
%{tangodir}/16x16/mimetypes/*.png
%dir %{tangodir}/16x16/places
%{tangodir}/16x16/places/*.png
%dir %{tangodir}/16x16/status
%{tangodir}/16x16/status/*.png

%dir %{tangodir}/22x22
%dir %{tangodir}/22x22/actions
%{tangodir}/22x22/actions/*.png
%dir %{tangodir}/22x22/animations
%{tangodir}/22x22/animations/*.png
%dir %{tangodir}/22x22/apps
%{tangodir}/22x22/apps/*.png
%dir %{tangodir}/22x22/categories
%{tangodir}/22x22/categories/*.png
%dir %{tangodir}/22x22/devices
%{tangodir}/22x22/devices/*.png
%dir %{tangodir}/22x22/emblems
%{tangodir}/22x22/emblems/*.png
%dir %{tangodir}/22x22/emotes
%{tangodir}/22x22/emotes/*.png
%dir %{tangodir}/22x22/mimetypes
%{tangodir}/22x22/mimetypes/*.png
%dir %{tangodir}/22x22/places
%{tangodir}/22x22/places/*.png
%dir %{tangodir}/22x22/status
%{tangodir}/22x22/status/*.png

#%dir %{tangodir}/24x24
#%dir %{tangodir}/24x24/actions
#%{tangodir}/24x24/actions/*.png
#%dir %{tangodir}/24x24/animations
#%{tangodir}/24x24/animations/*.png
#%dir %{tangodir}/24x24/apps
#%{tangodir}/24x24/apps/*.png
#%dir %{tangodir}/24x24/categories
#%{tangodir}/24x24/categories/*.png
#%dir %{tangodir}/24x24/devices
#%{tangodir}/24x24/devices/*.png
#%dir %{tangodir}/24x24/emblems
#%{tangodir}/24x24/emblems/*.png
#%dir %{tangodir}/24x24/emotes
#%{tangodir}/24x24/emotes/*.png
#%dir %{tangodir}/24x24/mimetypes
#%{tangodir}/24x24/mimetypes/*.png
#%dir %{tangodir}/24x24/places
#%{tangodir}/24x24/places/*.png
#%dir %{tangodir}/24x24/status
#%{tangodir}/24x24/status/*.png

%dir %{tangodir}/scalable
%dir %{tangodir}/scalable/actions
%{tangodir}/scalable/actions/*.svg
#%dir %{tangodir}/scalable/animations
#%{tangodir}/scalable/animations/*.svg
%dir %{tangodir}/scalable/apps
%{tangodir}/scalable/apps/*.svg
%dir %{tangodir}/scalable/categories
%{tangodir}/scalable/categories/*.svg
%dir %{tangodir}/scalable/devices
%{tangodir}/scalable/devices/*.svg
%dir %{tangodir}/scalable/emblems
%{tangodir}/scalable/emblems/*.svg
%dir %{tangodir}/scalable/emotes
%{tangodir}/scalable/emotes/*.svg
%dir %{tangodir}/scalable/mimetypes
%{tangodir}/scalable/mimetypes/*.svg
%dir %{tangodir}/scalable/places
%{tangodir}/scalable/places/*.svg
%{tangodir}/scalable/places/*.icon
%dir %{tangodir}/scalable/status
%{tangodir}/scalable/status/*.svg
%{tangodir}/scalable/status/*.icon
