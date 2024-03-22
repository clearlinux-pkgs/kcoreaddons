#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: f4bef72
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kcoreaddons
Version  : 6.0.0
Release  : 83
URL      : https://download.kde.org/stable/frameworks/6.0/kcoreaddons-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.0/kcoreaddons-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.0/kcoreaddons-6.0.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MPL-1.1
Requires: kcoreaddons-data = %{version}-%{release}
Requires: kcoreaddons-lib = %{version}-%{release}
Requires: kcoreaddons-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : glibc-dev
BuildRequires : qt6base-dev
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KCoreAddons
Qt addon library with a collection of non-GUI utilities
## Introduction

%package data
Summary: data components for the kcoreaddons package.
Group: Data

%description data
data components for the kcoreaddons package.


%package dev
Summary: dev components for the kcoreaddons package.
Group: Development
Requires: kcoreaddons-lib = %{version}-%{release}
Requires: kcoreaddons-data = %{version}-%{release}
Provides: kcoreaddons-devel = %{version}-%{release}
Requires: kcoreaddons = %{version}-%{release}

%description dev
dev components for the kcoreaddons package.


%package lib
Summary: lib components for the kcoreaddons package.
Group: Libraries
Requires: kcoreaddons-data = %{version}-%{release}
Requires: kcoreaddons-license = %{version}-%{release}

%description lib
lib components for the kcoreaddons package.


%package license
Summary: license components for the kcoreaddons package.
Group: Default

%description license
license components for the kcoreaddons package.


%prep
%setup -q -n kcoreaddons-6.0.0
cd %{_builddir}/kcoreaddons-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711125240
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
export SOURCE_DATE_EPOCH=1711125240
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcoreaddons
cp %{_builddir}/kcoreaddons-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/kcoreaddons-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kcoreaddons-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kcoreaddons-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kcoreaddons-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kcoreaddons-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kcoreaddons-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kcoreaddons-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kcoreaddons-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kcoreaddons-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kcoreaddons-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kcoreaddons-%{version}/LICENSES/MPL-1.1.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/b40d491259fdd8faefb41c11fda11d9be6c0bdb1 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/qml/org/kde/coreaddons/kcoreaddonsplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/coreaddons/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/coreaddons/qmldir

%files data
%defattr(-,root,root,-)
/usr/share/kf6/jsonschema/kpluginmetadata.schema.json
/usr/share/kf6/licenses/ARTISTIC
/usr/share/kf6/licenses/BSD
/usr/share/kf6/licenses/GPL_V2
/usr/share/kf6/licenses/GPL_V3
/usr/share/kf6/licenses/LGPL_V2
/usr/share/kf6/licenses/LGPL_V21
/usr/share/kf6/licenses/LGPL_V3
/usr/share/kf6/licenses/MIT
/usr/share/locale/af/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/as/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/az/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/be/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/br/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/da/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/de/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/el/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/en/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/es/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/et/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/he/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/id/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ie/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/is/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/it/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/kab/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/km/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/my/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/or/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/sa/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/se/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/si/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/sw/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/te/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/th/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/tok/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kcoreaddons6_qt.qm
/usr/share/mime-packages/kde6.xml
/usr/share/qlogging-categories6/kcoreaddons.categories
/usr/share/qlogging-categories6/kcoreaddons.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KCoreAddons/KAboutComponent
/usr/include/KF6/KCoreAddons/KAboutData
/usr/include/KF6/KCoreAddons/KAboutLicense
/usr/include/KF6/KCoreAddons/KAboutPerson
/usr/include/KF6/KCoreAddons/KAutoSaveFile
/usr/include/KF6/KCoreAddons/KBackup
/usr/include/KF6/KCoreAddons/KCompositeJob
/usr/include/KF6/KCoreAddons/KCoreAddons
/usr/include/KF6/KCoreAddons/KDirWatch
/usr/include/KF6/KCoreAddons/KFileSystemType
/usr/include/KF6/KCoreAddons/KFileUtils
/usr/include/KF6/KCoreAddons/KFormat
/usr/include/KF6/KCoreAddons/KFuzzyMatcher
/usr/include/KF6/KCoreAddons/KJob
/usr/include/KF6/KCoreAddons/KJobTrackerInterface
/usr/include/KF6/KCoreAddons/KJobUiDelegate
/usr/include/KF6/KCoreAddons/KJsonUtils
/usr/include/KF6/KCoreAddons/KLibexec
/usr/include/KF6/KCoreAddons/KListOpenFilesJob
/usr/include/KF6/KCoreAddons/KMacroExpander
/usr/include/KF6/KCoreAddons/KMemoryInfo
/usr/include/KF6/KCoreAddons/KNetworkMounts
/usr/include/KF6/KCoreAddons/KOSRelease
/usr/include/KF6/KCoreAddons/KPluginFactory
/usr/include/KF6/KCoreAddons/KPluginMetaData
/usr/include/KF6/KCoreAddons/KProcess
/usr/include/KF6/KCoreAddons/KProcessList
/usr/include/KF6/KCoreAddons/KRandom
/usr/include/KF6/KCoreAddons/KRuntimePlatform
/usr/include/KF6/KCoreAddons/KSandbox
/usr/include/KF6/KCoreAddons/KSharedDataCache
/usr/include/KF6/KCoreAddons/KShell
/usr/include/KF6/KCoreAddons/KSignalHandler
/usr/include/KF6/KCoreAddons/KStringHandler
/usr/include/KF6/KCoreAddons/KTextToHTML
/usr/include/KF6/KCoreAddons/KUrlMimeData
/usr/include/KF6/KCoreAddons/KUser
/usr/include/KF6/KCoreAddons/kaboutdata.h
/usr/include/KF6/KCoreAddons/kautosavefile.h
/usr/include/KF6/KCoreAddons/kbackup.h
/usr/include/KF6/KCoreAddons/kcompositejob.h
/usr/include/KF6/KCoreAddons/kcoreaddons.h
/usr/include/KF6/KCoreAddons/kcoreaddons_export.h
/usr/include/KF6/KCoreAddons/kcoreaddons_version.h
/usr/include/KF6/KCoreAddons/kdirwatch.h
/usr/include/KF6/KCoreAddons/kfilesystemtype.h
/usr/include/KF6/KCoreAddons/kfileutils.h
/usr/include/KF6/KCoreAddons/kformat.h
/usr/include/KF6/KCoreAddons/kfuzzymatcher.h
/usr/include/KF6/KCoreAddons/kjob.h
/usr/include/KF6/KCoreAddons/kjobtrackerinterface.h
/usr/include/KF6/KCoreAddons/kjobuidelegate.h
/usr/include/KF6/KCoreAddons/kjsonutils.h
/usr/include/KF6/KCoreAddons/klibexec.h
/usr/include/KF6/KCoreAddons/klistopenfilesjob.h
/usr/include/KF6/KCoreAddons/kmacroexpander.h
/usr/include/KF6/KCoreAddons/kmemoryinfo.h
/usr/include/KF6/KCoreAddons/knetworkmounts.h
/usr/include/KF6/KCoreAddons/kosrelease.h
/usr/include/KF6/KCoreAddons/kpluginfactory.h
/usr/include/KF6/KCoreAddons/kpluginmetadata.h
/usr/include/KF6/KCoreAddons/kprocess.h
/usr/include/KF6/KCoreAddons/kprocesslist.h
/usr/include/KF6/KCoreAddons/krandom.h
/usr/include/KF6/KCoreAddons/kruntimeplatform.h
/usr/include/KF6/KCoreAddons/ksandbox.h
/usr/include/KF6/KCoreAddons/kshareddatacache.h
/usr/include/KF6/KCoreAddons/kshell.h
/usr/include/KF6/KCoreAddons/ksignalhandler.h
/usr/include/KF6/KCoreAddons/kstringhandler.h
/usr/include/KF6/KCoreAddons/ktexttohtml.h
/usr/include/KF6/KCoreAddons/kurlmimedata.h
/usr/include/KF6/KCoreAddons/kuser.h
/usr/lib64/cmake/KF6CoreAddons/KF6CoreAddonsConfig.cmake
/usr/lib64/cmake/KF6CoreAddons/KF6CoreAddonsConfigVersion.cmake
/usr/lib64/cmake/KF6CoreAddons/KF6CoreAddonsMacros.cmake
/usr/lib64/cmake/KF6CoreAddons/KF6CoreAddonsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6CoreAddons/KF6CoreAddonsTargets.cmake
/usr/lib64/libKF6CoreAddons.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6CoreAddons.so.6.0.0
/V3/usr/lib64/qt6/qml/org/kde/coreaddons/libkcoreaddonsplugin.so
/usr/lib64/libKF6CoreAddons.so.6
/usr/lib64/libKF6CoreAddons.so.6.0.0
/usr/lib64/qt6/qml/org/kde/coreaddons/libkcoreaddonsplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcoreaddons/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcoreaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kcoreaddons/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/kcoreaddons/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kcoreaddons/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kcoreaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kcoreaddons/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kcoreaddons/b40d491259fdd8faefb41c11fda11d9be6c0bdb1
/usr/share/package-licenses/kcoreaddons/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kcoreaddons/e712eadfab0d2357c0f50f599ef35ee0d87534cb
