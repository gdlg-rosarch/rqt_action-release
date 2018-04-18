# Script generated with Bloom
pkgdesc="ROS - rqt_action provides a feature to introspect all available ROS action (from actionlib) types. By utilizing rqt_msg, the output format is unified with it and rqt_srv. Note that the actions shown on this plugin is the ones that are stored on your machine, not on the ROS core your rqt instance connects to."
url='http://wiki.ros.org/rqt_action'

pkgname='ros-lunar-rqt-action'
pkgver='0.4.9_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-rospy'
'ros-lunar-rqt-msg'
'ros-lunar-rqt-py-common'
)

conflicts=()
replaces=()

_dir=rqt_action
source=()
md5sums=()

prepare() {
    cp -R $startdir/rqt_action $srcdir/rqt_action
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

