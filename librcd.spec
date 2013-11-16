Name:           librcd
Version:        0.1.14
Release:        2%{?dist}
Summary:        Library for autodetection charset of Russian and Ukrainian text

License:        LGPLv2+
URL:            http://rusxmms.sourceforge.net
Source0:        http://dside.dyndns.org/files/rusxmms/%{name}-%{version}.tar.bz2

%description
LibRCD is used by RusXMMS project for encoding auto-detection. It is optimized
to handle very short titles, like ID3 tags, file names and etc, and provides
very high accuracy even for short 3-4 letter words. Current version supports
Russian and Ukrainian languages and able to distinguish UTF-8, KOI8-R, CP1251,
CP866, ISO8859-1. If compared with Enca, LibRCC provides better detection
accuracy on short titles and is able to detect ISO8859-1 (non-cyrillic)
encoding what allows to properly display correct ID3 v.1 titles.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
LibRCD is used by RusXMMS project for encoding auto-detection. It is optimized
to handle very short titles, like ID3 tags, file names and etc, and provides
very high accuracy even for short 3-4 letter words. Current version supports
Russian and Ukrainian languages and able to distinguish UTF-8, KOI8-R, CP1251,
CP866, ISO8859-1. If compared with Enca, LibRCC provides better detection
accuracy on short titles and is able to detect ISO8859-1 (non-cyrillic)
encoding what allows to properly display correct ID3 v.1 titles.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -delete


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING AUTHORS README
%{_libdir}/librcd.so.*

%files devel
%doc ChangeLog
%{_includedir}/librcd.h
%{_libdir}/librcd.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sat Nov 16 2013 Ivan Romanov <drizt@land.ru> - 0.1.14-2
- added ChangeLog to devel subpackage
- fixed typo in Summary

* Sat Nov 16 2013 Ivan Romanov <drizt@land.ru> - 0.1.14-1
- initial version of package
