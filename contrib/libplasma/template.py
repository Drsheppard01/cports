pkgname = "libplasma"
pkgver = "6.1.0"
pkgrel = 0
build_style = "cmake"
# DialogNativeTest::position() upper_left_y + anchorY is 0 instead of 49
make_check_args = ["-E", "(bug485688test|dialognativetest)"]
make_check_wrapper = ["xwfb-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "karchive-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kpackage-devel",
    "ksvg-devel",
    "plasma-activities-devel",
    "plasma-wayland-protocols",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
]
checkdepends = [
    "xwayland-run",
]
pkgdesc = "Foundational libraries, components, and tools for Plasma workspaces"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://api.kde.org/plasma/libplasma/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/libplasma-{pkgver}.tar.xz"
sha256 = "ed25f04ca68a040964b7bcdb043cb70beebdf8780c63026a5b2cb13c6bbe753b"
# FIXME: cfi kills plasmashell (on launch of startplasma-wayland) in liborg_kde_plasmacomponents3.so
hardening = ["vis", "!cfi"]


@subpackage("libplasma-devel")
def _devel(self):
    self.depends += ["kpackage-devel"]

    return self.default_devel()
