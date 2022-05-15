#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kcoreaddons
Version  : 5.94.0
Release  : 54
URL      : https://download.kde.org/stable/frameworks/5.94/kcoreaddons-5.94.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.94/kcoreaddons-5.94.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.94/kcoreaddons-5.94.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MPL-1.1
Requires: kcoreaddons-bin = %{version}-%{release}
Requires: kcoreaddons-data = %{version}-%{release}
Requires: kcoreaddons-lib = %{version}-%{release}
Requires: kcoreaddons-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : glibc-dev

%description
# KCoreAddons
Qt addon library with a collection of non-GUI utilities
## Introduction

%package bin
Summary: bin components for the kcoreaddons package.
Group: Binaries
Requires: kcoreaddons-data = %{version}-%{release}
Requires: kcoreaddons-license = %{version}-%{release}

%description bin
bin components for the kcoreaddons package.


%package data
Summary: data components for the kcoreaddons package.
Group: Data

%description data
data components for the kcoreaddons package.


%package dev
Summary: dev components for the kcoreaddons package.
Group: Development
Requires: kcoreaddons-lib = %{version}-%{release}
Requires: kcoreaddons-bin = %{version}-%{release}
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
%setup -q -n kcoreaddons-5.94.0
cd %{_builddir}/kcoreaddons-5.94.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652654245
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1652654245
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcoreaddons
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kcoreaddons-5.94.0/LICENSES/MPL-1.1.txt %{buildroot}/usr/share/package-licenses/kcoreaddons/b40d491259fdd8faefb41c11fda11d9be6c0bdb1
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/desktoptojson

%files data
%defattr(-,root,root,-)
/usr/share/kf5/licenses/ARTISTIC
/usr/share/kf5/licenses/BSD
/usr/share/kf5/licenses/GPL_V2
/usr/share/kf5/licenses/GPL_V3
/usr/share/kf5/licenses/LGPL_V2
/usr/share/kf5/licenses/LGPL_V21
/usr/share/kf5/licenses/LGPL_V3
/usr/share/kf5/licenses/QPL_V1.0
/usr/share/locale/af/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/as/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/az/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/az/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/be/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/be/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/be@latin/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/bn/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/br/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/ca/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/crh/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/csb/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/de/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/el/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/en/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/eo/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/es/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/et/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/eu/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/fa/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/fr/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/fy/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/gd/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/gl/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/gu/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/he/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/hne/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/hsb/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/hy/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/id/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/is/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/is/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/it/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/ja/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/ka/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/kab/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/km/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/km/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/kn/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/ku/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/lv/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/mai/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/mr/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/ms/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/my/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/my/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/nb/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/nds/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/ne/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/nn/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/oc/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/or/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/pl/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/ps/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/ro/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/ru/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/se/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/si/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/sl/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/sq/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/sr/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/sv/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/ta/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/te/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/th/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/th/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/tok/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/tok/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/tr/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/tt/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/uk/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/uz/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/wa/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kde5_xml_mimetypes.qm
/usr/share/mime-packages/kde5.xml
/usr/share/qlogging-categories5/kcoreaddons.categories
/usr/share/qlogging-categories5/kcoreaddons.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KCoreAddons/KAboutData
/usr/include/KF5/KCoreAddons/KAutoSaveFile
/usr/include/KF5/KCoreAddons/KBackup
/usr/include/KF5/KCoreAddons/KCompositeJob
/usr/include/KF5/KCoreAddons/KCoreAddons
/usr/include/KF5/KCoreAddons/KDirWatch
/usr/include/KF5/KCoreAddons/KExportPlugin
/usr/include/KF5/KCoreAddons/KFileSystemType
/usr/include/KF5/KCoreAddons/KFileUtils
/usr/include/KF5/KCoreAddons/KFormat
/usr/include/KF5/KCoreAddons/KFuzzyMatcher
/usr/include/KF5/KCoreAddons/KJob
/usr/include/KF5/KCoreAddons/KJobTrackerInterface
/usr/include/KF5/KCoreAddons/KJobUiDelegate
/usr/include/KF5/KCoreAddons/KJsonUtils
/usr/include/KF5/KCoreAddons/KLibexec
/usr/include/KF5/KCoreAddons/KListOpenFilesJob
/usr/include/KF5/KCoreAddons/KMacroExpander
/usr/include/KF5/KCoreAddons/KMessage
/usr/include/KF5/KCoreAddons/KNetworkMounts
/usr/include/KF5/KCoreAddons/KOSRelease
/usr/include/KF5/KCoreAddons/KPluginFactory
/usr/include/KF5/KCoreAddons/KPluginLoader
/usr/include/KF5/KCoreAddons/KPluginMetaData
/usr/include/KF5/KCoreAddons/KProcess
/usr/include/KF5/KCoreAddons/KProcessList
/usr/include/KF5/KCoreAddons/KRandom
/usr/include/KF5/KCoreAddons/KRandomSequence
/usr/include/KF5/KCoreAddons/KSharedDataCache
/usr/include/KF5/KCoreAddons/KShell
/usr/include/KF5/KCoreAddons/KSignalHandler
/usr/include/KF5/KCoreAddons/KStaticPluginHelpers
/usr/include/KF5/KCoreAddons/KStringHandler
/usr/include/KF5/KCoreAddons/KTextToHTML
/usr/include/KF5/KCoreAddons/KTextToHTMLEmoticonsInterface
/usr/include/KF5/KCoreAddons/KUrlMimeData
/usr/include/KF5/KCoreAddons/KUser
/usr/include/KF5/KCoreAddons/Kdelibs4ConfigMigrator
/usr/include/KF5/KCoreAddons/Kdelibs4Migration
/usr/include/KF5/KCoreAddons/kaboutdata.h
/usr/include/KF5/KCoreAddons/kautosavefile.h
/usr/include/KF5/KCoreAddons/kbackup.h
/usr/include/KF5/KCoreAddons/kcompositejob.h
/usr/include/KF5/KCoreAddons/kcoreaddons.h
/usr/include/KF5/KCoreAddons/kcoreaddons_export.h
/usr/include/KF5/KCoreAddons/kcoreaddons_version.h
/usr/include/KF5/KCoreAddons/kdelibs4configmigrator.h
/usr/include/KF5/KCoreAddons/kdelibs4migration.h
/usr/include/KF5/KCoreAddons/kdirwatch.h
/usr/include/KF5/KCoreAddons/kexportplugin.h
/usr/include/KF5/KCoreAddons/kfilesystemtype.h
/usr/include/KF5/KCoreAddons/kfileutils.h
/usr/include/KF5/KCoreAddons/kformat.h
/usr/include/KF5/KCoreAddons/kfuzzymatcher.h
/usr/include/KF5/KCoreAddons/kjob.h
/usr/include/KF5/KCoreAddons/kjobtrackerinterface.h
/usr/include/KF5/KCoreAddons/kjobuidelegate.h
/usr/include/KF5/KCoreAddons/kjsonutils.h
/usr/include/KF5/KCoreAddons/klibexec.h
/usr/include/KF5/KCoreAddons/klistopenfilesjob.h
/usr/include/KF5/KCoreAddons/kmacroexpander.h
/usr/include/KF5/KCoreAddons/kmessage.h
/usr/include/KF5/KCoreAddons/knetworkmounts.h
/usr/include/KF5/KCoreAddons/kosrelease.h
/usr/include/KF5/KCoreAddons/kpluginfactory.h
/usr/include/KF5/KCoreAddons/kpluginloader.h
/usr/include/KF5/KCoreAddons/kpluginmetadata.h
/usr/include/KF5/KCoreAddons/kprocess.h
/usr/include/KF5/KCoreAddons/kprocesslist.h
/usr/include/KF5/KCoreAddons/krandom.h
/usr/include/KF5/KCoreAddons/krandomsequence.h
/usr/include/KF5/KCoreAddons/kshareddatacache.h
/usr/include/KF5/KCoreAddons/kshell.h
/usr/include/KF5/KCoreAddons/ksignalhandler.h
/usr/include/KF5/KCoreAddons/kstaticpluginhelpers.h
/usr/include/KF5/KCoreAddons/kstringhandler.h
/usr/include/KF5/KCoreAddons/ktexttohtml.h
/usr/include/KF5/KCoreAddons/ktexttohtmlemoticonsinterface.h
/usr/include/KF5/KCoreAddons/kurlmimedata.h
/usr/include/KF5/KCoreAddons/kuser.h
/usr/lib64/cmake/KF5CoreAddons/KF5CoreAddonsConfig.cmake
/usr/lib64/cmake/KF5CoreAddons/KF5CoreAddonsConfigVersion.cmake
/usr/lib64/cmake/KF5CoreAddons/KF5CoreAddonsMacros.cmake
/usr/lib64/cmake/KF5CoreAddons/KF5CoreAddonsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5CoreAddons/KF5CoreAddonsTargets.cmake
/usr/lib64/cmake/KF5CoreAddons/KF5CoreAddonsToolingTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5CoreAddons/KF5CoreAddonsToolingTargets.cmake
/usr/lib64/libKF5CoreAddons.so
/usr/lib64/qt5/mkspecs/modules/qt_KCoreAddons.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5CoreAddons.so.5
/usr/lib64/libKF5CoreAddons.so.5.94.0
/usr/lib64/qt5/plugins/namespace/jsonplugin_cmake_macro.so
/usr/lib64/qt5/plugins/namespace/pluginwithoutmetadata.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcoreaddons/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcoreaddons/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kcoreaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kcoreaddons/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kcoreaddons/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/kcoreaddons/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kcoreaddons/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kcoreaddons/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kcoreaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kcoreaddons/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kcoreaddons/b40d491259fdd8faefb41c11fda11d9be6c0bdb1
/usr/share/package-licenses/kcoreaddons/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kcoreaddons/e712eadfab0d2357c0f50f599ef35ee0d87534cb
