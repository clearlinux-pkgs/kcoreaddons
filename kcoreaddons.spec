#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kcoreaddons
Version  : 5.53.1
Release  : 11
URL      : https://download.kde.org/stable/frameworks/5.53/kcoreaddons-5.53.1.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.53/kcoreaddons-5.53.1.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.53/kcoreaddons-5.53.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.0 LGPL-2.1
Requires: kcoreaddons-bin = %{version}-%{release}
Requires: kcoreaddons-data = %{version}-%{release}
Requires: kcoreaddons-lib = %{version}-%{release}
Requires: kcoreaddons-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : glibc-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kcoreaddons-5.53.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544486170
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1544486170
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcoreaddons
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/kcoreaddons/COPYING-CMAKE-SCRIPTS
cp COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/kcoreaddons/COPYING.LGPL-2
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kcoreaddons/COPYING.LIB
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
/usr/share/locale/as/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/be/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/br/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/en/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/he/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/is/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/km/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/or/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/si/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/te/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/th/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kcoreaddons5_qt.qm
/usr/share/mime-packages/kde5.xml
/usr/share/xdg/kcoreaddons.categories

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
/usr/include/KF5/KCoreAddons/KFormat
/usr/include/KF5/KCoreAddons/KJob
/usr/include/KF5/KCoreAddons/KJobTrackerInterface
/usr/include/KF5/KCoreAddons/KJobUiDelegate
/usr/include/KF5/KCoreAddons/KMacroExpander
/usr/include/KF5/KCoreAddons/KMessage
/usr/include/KF5/KCoreAddons/KPluginFactory
/usr/include/KF5/KCoreAddons/KPluginLoader
/usr/include/KF5/KCoreAddons/KPluginMetaData
/usr/include/KF5/KCoreAddons/KProcess
/usr/include/KF5/KCoreAddons/KRandom
/usr/include/KF5/KCoreAddons/KRandomSequence
/usr/include/KF5/KCoreAddons/KSharedDataCache
/usr/include/KF5/KCoreAddons/KShell
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
/usr/include/KF5/KCoreAddons/kdelibs4configmigrator.h
/usr/include/KF5/KCoreAddons/kdelibs4migration.h
/usr/include/KF5/KCoreAddons/kdirwatch.h
/usr/include/KF5/KCoreAddons/kexportplugin.h
/usr/include/KF5/KCoreAddons/kfilesystemtype.h
/usr/include/KF5/KCoreAddons/kformat.h
/usr/include/KF5/KCoreAddons/kjob.h
/usr/include/KF5/KCoreAddons/kjobtrackerinterface.h
/usr/include/KF5/KCoreAddons/kjobuidelegate.h
/usr/include/KF5/KCoreAddons/kmacroexpander.h
/usr/include/KF5/KCoreAddons/kmessage.h
/usr/include/KF5/KCoreAddons/kpluginfactory.h
/usr/include/KF5/KCoreAddons/kpluginloader.h
/usr/include/KF5/KCoreAddons/kpluginmetadata.h
/usr/include/KF5/KCoreAddons/kprocess.h
/usr/include/KF5/KCoreAddons/krandom.h
/usr/include/KF5/KCoreAddons/krandomsequence.h
/usr/include/KF5/KCoreAddons/kshareddatacache.h
/usr/include/KF5/KCoreAddons/kshell.h
/usr/include/KF5/KCoreAddons/kstringhandler.h
/usr/include/KF5/KCoreAddons/ktexttohtml.h
/usr/include/KF5/KCoreAddons/ktexttohtmlemoticonsinterface.h
/usr/include/KF5/KCoreAddons/kurlmimedata.h
/usr/include/KF5/KCoreAddons/kuser.h
/usr/include/KF5/kcoreaddons_version.h
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
/usr/lib64/libKF5CoreAddons.so.5.53.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcoreaddons/COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/kcoreaddons/COPYING.LGPL-2
/usr/share/package-licenses/kcoreaddons/COPYING.LIB
