Summary:	Library for IPTC metadata manipulation
Summary(pl.UTF-8):   Biblioteka do manipulacji metadanymi IPTC
Name:		libiptcdata
Version:	0.2.1
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/libiptcdata/%{name}-%{version}.tar.gz
# Source0-md5:	2df9620f8c08aba4ccbe434032ff320d
URL:		http://libiptcdata.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	libtool
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
do parsowania, oglądania, modyfikowania i zapisywania metadanych.

%package devel
Summary:	Header files for libiptcdata library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libiptcdata
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libiptcdata library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libiptcdata.

%package static
Summary:	Static libiptcdata library
Summary(pl.UTF-8):   Statyczna biblioteka libiptcdata
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libiptcdata library.

%description static -l pl.UTF-8
Statyczna biblioteka libiptcdata.

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
	--with-html-dir=%{_gtkdocdir}
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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libiptcdata
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/libiptcdata

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
