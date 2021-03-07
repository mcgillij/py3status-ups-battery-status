# Maintainer: Jason McGillivray < mcgillivray dot jason at gmail dot com>


pkgname=py3status-ups-battery-status
pkgdesc="Monitor the status of your UPS battery in py3status bar"
pkgver=0.1.0
pkgrel=1
arch=('any')
license=('GPL2')
depends=('python' 'py3status')
makedepends=('python-setuptools')
url="https://github.com/mcgillij/py3status-ups-battery-status"
source=("py3status-ups-battery-status-0.1.0.tar.gz")
md5sums=('656fb7df0d0285a0118a0e0a46420de8')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --prefix=/usr --root="$pkgdir"
} 
