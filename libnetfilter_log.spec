Summary:	netfilter userspace packet logging library
Summary(pl.UTF-8):	Biblioteka logowania w przestrzeni użytkownika dla netfiltra
Name:		libnetfilter_log
Version:	1.0.2
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	https://netfilter.org/projects/libnetfilter_log/files/%{name}-%{version}.tar.bz2
# Source0-md5:	12825abf68cfcc150a31ccb88ae9f42d
URL:		https://netfilter.org/projects/libnetfilter_log/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	doxygen
BuildRequires:	libmnl-devel >= 1.0.3
# for tests only
#BuildRequires:	libnetfilter_conntrack-devel >= 1.0.2
BuildRequires:	libnfnetlink-devel >= 0.0.41
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	libmnl >= 1.0.3
Requires:	libnfnetlink >= 0.0.41
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnetfilter_log is a userspace library providing interface to packets
that have been logged by the kernel packet filter. It is part of a
system that deprecates the old syslog/dmesg based packet logging.

%description -l pl.UTF-8
libnetfilter_log to biblioteka przestrzeni użytkownika udostępniająca
interfejs do pakietów logowanych przez filtr pakietów w jądrze. Jest
częścią systemu zastępującego stare logowanie pakietów oparte na
syslogu/dmesgu.

%package devel
Summary:	Header files for libnetfilter_log library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnetfilter_log
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libmnl-devel >= 1.0.3
Requires:	libnfnetlink-devel >= 0.0.41

%description devel
Header files for libnetfilter_log library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnetfilter_log.

%package static
Summary:	Static libnetfilter_log library
Summary(pl.UTF-8):	Statyczna biblioteka libnetfilter_log
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnetfilter_log library.

%description static -l pl.UTF-8
Statyczna biblioteka libnetfilter_log.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libnetfilter_log*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetfilter_log.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetfilter_log.so.1
%attr(755,root,root) %{_libdir}/libnetfilter_log_libipulog.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetfilter_log_libipulog.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetfilter_log.so
%attr(755,root,root) %{_libdir}/libnetfilter_log_libipulog.so
%{_includedir}/libnetfilter_log
%{_pkgconfigdir}/libnetfilter_log.pc
%{_pkgconfigdir}/libnetfilter_log_libipulog.pc
%{_mandir}/man3/nflog_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetfilter_log.a
%{_libdir}/libnetfilter_log_libipulog.a
