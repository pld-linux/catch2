Summary:	A modern, C++-native, test framework for unit-tests, TDD and BDD
Summary(pl.UTF-8):	Nowoczesny, natywny dla C++ szkielet dla testów jednostkowych, TDD i BDD
Name:		catch2
Version:	3.16.1
Release:	1
License:	Boost v1.0
Group:		Libraries
#Source0Download: https://github.com/catchorg/Catch2/releases
Source0:	https://github.com/catchorg/Catch2/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	aadd412b6277071a804cdde7a7dea244
URL:		https://github.com/catchorg/Catch2
BuildRequires:	cmake >= 3.16
# C++14
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catch2 is mainly a unit testing framework for C++, but it also
provides basic micro-benchmarking features, and simple BDD macros.

%description -l pl.UTF-8
Catch2 to przeznaczony dla C++ szkielet testów przede wszystkim
jednostkowych, ale zapewniający też funkcjonalność mikro-benchmarków i
proste makra BDD.

%package devel
Summary:	Header files for catch2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki catch2
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:5

%description devel
Header files for catch2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki catch2.

%prep
%setup -q -n Catch2-%{version}

%build
# .pc files generation expects relative CMAKE_INSTALL_{INCLUDE,LIB}DIR
%cmake -B build \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	-DPKGCONFIG_INSTALL_DIR:PATH="%{_lib}/pkgconfig" \
	-DCATCH_INSTALL_DOCS:BOOL=OFF \
	-DCATCH_ENABLE_REPRODUCIBLE_BUILD:BOOL=OFF

%{__make} -C build

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
%doc LICENSE.txt README.md extras/{gdbinit,lldbinit}
%{_libdir}/libCatch2.so.%{version}
%{_libdir}/libCatch2Main.so.%{version}

%files devel
%defattr(644,root,root,755)
%{_libdir}/libCatch2.so
%{_libdir}/libCatch2Main.so
%{_libdir}/cmake/Catch2
%{_includedir}/catch2
%{_pkgconfigdir}/catch2.pc
%{_pkgconfigdir}/catch2-with-main.pc
