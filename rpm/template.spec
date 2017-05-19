Name:           ros-lunar-rqt-action
Version:        0.4.9
Release:        0%{?dist}
Summary:        ROS rqt_action package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_action
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-rospy
Requires:       ros-lunar-rqt-msg
Requires:       ros-lunar-rqt-py-common
BuildRequires:  ros-lunar-catkin

%description
rqt_action provides a feature to introspect all available ROS action (from
actionlib) types. By utilizing rqt_msg, the output format is unified with it and
rqt_srv. Note that the actions shown on this plugin is the ones that are stored
on your machine, not on the ROS core your rqt instance connects to.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri May 19 2017 Mikael Arguedas <mikael@osrfoundation.org> - 0.4.9-0
- Autogenerated by Bloom

* Thu Apr 27 2017 Mikael Arguedas <mikael@osrfoundation.org> - 0.4.8-0
- Autogenerated by Bloom

