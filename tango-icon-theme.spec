#
# TODO:
# - better summary and descriptions
#
Summary:	freedesktop.org standard compliant icons
Summary(pl.UTF-8):	Ikony implementujące standard freedesktop.org
Name:		tango-icon-theme
Version:	0.8.90
Release:	2
License:	Creative Commons License (see COPYING)
Group:		Themes
Source0:	http://tango.freedesktop.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	b7b9b16480afb781a4c13f8bceb8688b
Patch0:		%{name}-transparency.patch
URL:		http://tango.freedesktop.org/Tango_Desktop_Project
BuildRequires:	ImageMagick-coder-png
BuildRequires:	ImageMagick-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	icon-naming-utils >= 0.8.90
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
freedesktop.org standard compliant icons.

%description -l pl.UTF-8
Ikony implementujące standard freedesktop.org.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-png-creation
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%{_iconsdir}/Tango
