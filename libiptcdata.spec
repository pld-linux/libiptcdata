Summary:	Library for IPTC metadata manipulation
Summary(pl.UTF-8):	Biblioteka do manipulacji metadanymi IPTC
Name:		libiptcdata
Version:	1.0.4
Release:	5
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libiptcdata/%{name}-%{version}.tar.gz
# Source0-md5:	af886556ecb129b694f2d365d03d95a8
URL:		http://libiptcdata.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools >= 0.13.1
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libiptcdata is a library, written in C, for manipulating the
International Press Telecommunications Council (IPTC) metadata stored
within multimedia files such as images. This metadata can include
captions and keywords, often used by popular photo management
applications. The library provides routines for parsing, viewing,
modifying, and saving this metadata.

%description -l pl.UTF-8
libiptcdata jest biblioteką napisaną w C pozwalająca na manipulowanie
metadanymi International Press Telecommunications Council (IPTC),
zapisanymi w plikach multimedialnych jak np. obrazy. Metadane te mogą
zawierać tytuł i słowa kluczowe, często używane przez popularne
programy zarządzające kolekcjami zdjęć. Biblioteka dostarcza procedury
do analizy, oglądania, modyfikowania i zapisywania metadanych.

%package devel
Summary:	Header files for libiptcdata library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libiptcdata
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libiptcdata library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libiptcdata.

%package static
Summary:	Static libiptcdata library
Summary(pl.UTF-8):	Statyczna biblioteka libiptcdata
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libiptcdata library.

%description static -l pl.UTF-8
Statyczna biblioteka libiptcdata.

%package -n python-iptcdata
Summary:	Python wrapper for libiptcdata
Summary(pl.UTF-8):	Wiązanie Pythona do libiptcdata
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-iptcdata
Python wrapper for libiptcdata.

%description -n python-iptcdata -l pl.UTF-8
Wiązanie Pythona do libiptcdata.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-python \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# libiptcdata and iptc domains (no translations yet)
%find_lang %{name} --all-name

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/iptcdata.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/iptc
%attr(755,root,root) %{_libdir}/libiptcdata.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libiptcdata.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiptcdata.so
%{_libdir}/libiptcdata.la
%{_includedir}/libiptcdata
%{_pkgconfigdir}/libiptcdata.pc
%{_gtkdocdir}/libiptcdata

%files static
%defattr(644,root,root,755)
%{_libdir}/libiptcdata.a

%files -n python-iptcdata
%defattr(644,root,root,755)
%doc python/README
%attr(755,root,root) %{py_sitedir}/iptcdata.so
