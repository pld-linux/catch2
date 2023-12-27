Summary:	A modern, C++-native, test framework for unit-tests, TDD and BDD
Name:		catch2
Version:	3.5.0
Release:	1
License:	Boost v1.0
Group:		Libraries
Source0:	https://github.com/catchorg/Catch2/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8e56bcccbc86e68e916cce0d43450116
URL:		https://github.com/catchorg/Catch2
BuildRequires:	cmake >= 3.10
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catch2 is mainly a unit testing framework for C++, but it also
provides basic micro-benchmarking features, and simple BDD macros.

%package devel
Summary:	Header files for catch2 library
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for catch2 library.

%prep
%setup -q -n Catch2-%{version}

%build
install -d build
cd build
%cmake .. \
	-DPKGCONFIG_INSTALL_DIR:PATH="%{_pkgconfigdir}" \
	-DCATCH_INSTALL_DOCS:BOOL=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%attr(755,root,root) %{_libdir}/libCatch2.so.%{version}
%attr(755,root,root) %{_libdir}/libCatch2Main.so.%{version}

%files devel
%defattr(644,root,root,755)
%{_libdir}/libCatch2.so
%{_libdir}/libCatch2Main.so
%{_libdir}/cmake/Catch2
%{_includedir}/catch2
%{_pkgconfigdir}/catch2.pc
%{_pkgconfigdir}/catch2-with-main.pc
