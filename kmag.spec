#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmag
Version  : 23.04.3
Release  : 55
URL      : https://download.kde.org/stable/release-service/23.04.3/src/kmag-23.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.3/src/kmag-23.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.3/src/kmag-23.04.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: kmag-bin = %{version}-%{release}
Requires: kmag-data = %{version}-%{release}
Requires: kmag-license = %{version}-%{release}
Requires: kmag-locales = %{version}-%{release}
Requires: kmag-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
kmag is a screen magnifier.
In any case, check the website
https://kde.org/applications/utilities/org.kde.kmag

%package bin
Summary: bin components for the kmag package.
Group: Binaries
Requires: kmag-data = %{version}-%{release}
Requires: kmag-license = %{version}-%{release}

%description bin
bin components for the kmag package.


%package data
Summary: data components for the kmag package.
Group: Data

%description data
data components for the kmag package.


%package doc
Summary: doc components for the kmag package.
Group: Documentation
Requires: kmag-man = %{version}-%{release}

%description doc
doc components for the kmag package.


%package license
Summary: license components for the kmag package.
Group: Default

%description license
license components for the kmag package.


%package locales
Summary: locales components for the kmag package.
Group: Default

%description locales
locales components for the kmag package.


%package man
Summary: man components for the kmag package.
Group: Default

%description man
man components for the kmag package.


%prep
%setup -q -n kmag-23.04.3
cd %{_builddir}/kmag-23.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688853285
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1688853285
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmag
cp %{_builddir}/kmag-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kmag/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kmag-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kmag/b1c25bcf0e44653a0ab61b5e3a5b2841414d0033 || :
cp %{_builddir}/kmag-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/kmag/1bd373e4851a93027ba70064bd7dbdc6827147e1 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kmag
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kmag
/usr/bin/kmag

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kmag.desktop
/usr/share/icons/hicolor/16x16/apps/kmag.png
/usr/share/icons/hicolor/32x32/apps/kmag.png
/usr/share/kmag/icons/hicolor/16x16/actions/followmouse.png
/usr/share/kmag/icons/hicolor/16x16/actions/hidemouse.png
/usr/share/kmag/icons/hicolor/16x16/actions/window.png
/usr/share/metainfo/org.kde.kmag.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kmag/index.cache.bz2
/usr/share/doc/HTML/ca/kmag/index.docbook
/usr/share/doc/HTML/ca/kmag/screenshot.png
/usr/share/doc/HTML/de/kmag/index.cache.bz2
/usr/share/doc/HTML/de/kmag/index.docbook
/usr/share/doc/HTML/de/kmag/screenshot.png
/usr/share/doc/HTML/en/kmag/index.cache.bz2
/usr/share/doc/HTML/en/kmag/index.docbook
/usr/share/doc/HTML/en/kmag/screenshot.png
/usr/share/doc/HTML/es/kmag/index.cache.bz2
/usr/share/doc/HTML/es/kmag/index.docbook
/usr/share/doc/HTML/fr/kmag/index.cache.bz2
/usr/share/doc/HTML/fr/kmag/index.docbook
/usr/share/doc/HTML/fr/kmag/screenshot.png
/usr/share/doc/HTML/it/kmag/index.cache.bz2
/usr/share/doc/HTML/it/kmag/index.docbook
/usr/share/doc/HTML/it/kmag/screenshot.png
/usr/share/doc/HTML/ko/kmag/index.cache.bz2
/usr/share/doc/HTML/ko/kmag/index.docbook
/usr/share/doc/HTML/nl/kmag/index.cache.bz2
/usr/share/doc/HTML/nl/kmag/index.docbook
/usr/share/doc/HTML/nl/kmag/screenshot.png
/usr/share/doc/HTML/pt/kmag/index.cache.bz2
/usr/share/doc/HTML/pt/kmag/index.docbook
/usr/share/doc/HTML/pt_BR/kmag/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kmag/index.docbook
/usr/share/doc/HTML/pt_BR/kmag/screenshot.png
/usr/share/doc/HTML/ru/kmag/index.cache.bz2
/usr/share/doc/HTML/ru/kmag/index.docbook
/usr/share/doc/HTML/sv/kmag/index.cache.bz2
/usr/share/doc/HTML/sv/kmag/index.docbook
/usr/share/doc/HTML/sv/kmag/screenshot.png
/usr/share/doc/HTML/uk/kmag/index.cache.bz2
/usr/share/doc/HTML/uk/kmag/index.docbook
/usr/share/doc/HTML/uk/kmag/screenshot.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmag/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/kmag/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kmag/b1c25bcf0e44653a0ab61b5e3a5b2841414d0033

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kmag.1
/usr/share/man/de/man1/kmag.1
/usr/share/man/es/man1/kmag.1
/usr/share/man/et/man1/kmag.1
/usr/share/man/fr/man1/kmag.1
/usr/share/man/it/man1/kmag.1
/usr/share/man/man1/kmag.1
/usr/share/man/nl/man1/kmag.1
/usr/share/man/pt/man1/kmag.1
/usr/share/man/pt_BR/man1/kmag.1
/usr/share/man/ru/man1/kmag.1
/usr/share/man/sv/man1/kmag.1
/usr/share/man/uk/man1/kmag.1

%files locales -f kmag.lang
%defattr(-,root,root,-)

