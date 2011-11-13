Summary:	Frame Buffer Video Sink display component for Bellagio OpenMAX IL
Summary(pl.UTF-8):	Komponent wyświetlający Frame Buffer Video Sink dla implementacji Bellagio OpenMAX IL
Name:		omxil-fbdevsink
Version:	0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/omxil/libomxfbdevsink-%{version}.tar.gz
# Source0-md5:	6a6a452bd8c9c4fb64f7913ba0884732
URL:		http://omxil.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libomxil-bellagio-devel >= 0.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libomxil-bellagio >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/usr/%{_lib}/bellagio

%description
Frame Buffer Video Sink component is a video display component for
Bellagio OpenMAX IL that uses the Linux Frame Buffer (/dev/fb0) for
visualization.

%description -l pl.UTF-8
Komponent Frabe Buffer Video Sink to komponent wyświetlający obraz dla
implementacji Bellagio OpenMAX IL, wykorzystujący do wizualizacji
linuksowy framebuffer (/dev/fb0).

%prep
%setup -q -n libomxfbdevsink-%{version}

%build
# rebuild for as-needed to work
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libomxfbdev.so*
