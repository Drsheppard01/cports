pkgname = "kde-cli-tools"
pkgver = "6.1.0"
pkgrel = 0
build_style = "cmake"
# FIXME: only test fails on initTestCase() 'fakeApplicationService' returned FALSE
make_check_args = ["-E", "filetypestest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kconfig-devel",
    "kdesu-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kparts-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE command line tools to interact with Plasma"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kde-cli-tools"
source = f"$(KDE_SITE)/plasma/{pkgver}/kde-cli-tools-{pkgver}.tar.xz"
sha256 = "bc4e2262b8b3e18dec010ec1bea4f6ddcd5f36a1275f84d12b6f6e863b365dbe"
# CFI: check
hardening = ["vis", "!cfi"]
