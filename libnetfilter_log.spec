Summary:	netfilter userspace packet logging library
Summary(pl.UTF-8):	Biblioteka logowania w przestrzeni użytkownika dla netfiltra
Name:		libnetfilter_log
Version:	0.0.16
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.netfilter.org/pub/libnetfilter_log/%{name}-%{version}.tar.bz2
# Source0-md5:	4ffcf46dad9d0c81f6611dd185639694
URL:		http://www.netfilter.org/projects/libnetfilter_log/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnfnetlink-devel >= 0.0.39
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	libnfnetlink >= 0.0.39
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
Requires:	libnfnetlink-devel >= 0.0.39

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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_libdir}/libnetfilter_log.la
%{_libdir}/libnetfilter_log_libipulog.la
%{_includedir}/libnetfilter_log
%{_pkgconfigdir}/libnetfilter_log.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetfilter_log.a
%{_libdir}/libnetfilter_log_libipulog.a
