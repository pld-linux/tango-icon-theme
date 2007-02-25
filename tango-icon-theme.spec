#
# TODO:
# - better summary and descriptions
#
Summary:	freedesktop.org standard compliant icons
Summary(pl.UTF-8):	Ikony implementujące standard freedesktop.org
Name:		tango-icon-theme
Version:	0.8.0
Release:	1
License:	Creative Commons License (see COPYING)
Group:		Themes
Source0:	http://tango-project.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	0bb6a808b514a530adb6fe54e9e3b004
URL:		http://tango-project.org/Tango_Desktop_Project
BuildRequires:	ImageMagick-coder-png
BuildRequires:	ImageMagick-devel
BuildRequires:	icon-naming-utils >= 0.8.2
BuildRequires:	pkgconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
freedesktop.org standard compliant icons.

%description -l pl.UTF-8
Ikony implementujące standard freedesktop.org.

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
%doc AUTHORS COPYING ChangeLog README
%{_iconsdir}/Tango
