#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v8
# autospec commit: 658bd0d
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmag
Version  : 24.02.2
Release  : 65
URL      : https://download.kde.org/stable/release-service/24.02.2/src/kmag-24.02.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.2/src/kmag-24.02.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.2/src/kmag-24.02.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kmag-bin = %{version}-%{release}
Requires: kmag-data = %{version}-%{release}
Requires: kmag-license = %{version}-%{release}
Requires: kmag-locales = %{version}-%{release}
Requires: kmag-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# <img src="logo.png" width="40"/> KMag
Kmag is a screen magnifier.
Website: https://kde.org/applications/utilities/org.kde.kmag

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep '^\[GNUPG:\] GOODSIG BB463350D6EF31EF' gpg.status
%setup -q -n kmag-24.02.2
cd %{_builddir}/kmag-24.02.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1712883176
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1712883176
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmag
cp %{_builddir}/kmag-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kmag/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kmag-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kmag/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/kmag-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmag/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kmag-%{version}/LICENSES/GFDL-1.2-only.txt %{buildroot}/usr/share/package-licenses/kmag/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc || :
cp %{_builddir}/kmag-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmag/3cb34cfc72e87654683f2894299adf912d14b284 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
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
/usr/share/icons/hicolor/scalable/apps/kmag.svg
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
/usr/share/package-licenses/kmag/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kmag/3630f1ffcec0e075bf446b88c7b507b1287b571d
/usr/share/package-licenses/kmag/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/kmag/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kmag/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc

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

