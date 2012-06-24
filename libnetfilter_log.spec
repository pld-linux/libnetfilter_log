Summary:	netfilter userspace packet logging library
Summary(pl):	Biblioteka logowania w przestrzeni u�ytkownika dla netfiltra
Name:		libnetfilter_log
Version:	0.0.13
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.netfilter.org/pub/libnetfilter_log/%{name}-%{version}.tar.bz2
# Source0-md5:	168e4f46f6ad5549ddbaddf675e54552
URL:		http://www.netfilter.org/projects/libnetfilter_log/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnfnetlink-devel >= 0.0.16
BuildRequires:	libtool
Requires:	libnfnetlink >= 0.0.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnetfilter_log is a userspace library providing interface to packets
that have been logged by the kernel packet filter. It is part of a
system that deprecates the old syslog/dmesg based packet logging.

%description -l pl
libnetfilter_log to biblioteka przestrzeni u�ytkownika udost�pniaj�ca
interfejs do pakiet�w logowanych przez filtr pakiet�w w j�drze. Jest
cz�ci� systemu zast�puj�cego stare logowanie pakiet�w oparte na
syslogu/dmesgu.

%package devel
Summary:	Header files for libnetfilter_log library
Summary(pl):	Pliki nag��wkowe biblioteki libnetfilter_log
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libnfnetlink-devel >= 0.0.16

%description devel
Header files for libnetfilter_log library.

%description devel -l pl
Pliki nag��wkowe biblioteki libnetfilter_log.

%package static
Summary:	Static libnetfilter_log library
Summary(pl):	Statyczna biblioteka libnetfilter_log
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnetfilter_log library.

%description static -l pl
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
%attr(755,root,root) %{_libdir}/libnetfilter_log_libipulog.so.*.*.*

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
