Name:           libgovirt
Version:        0.3.4
Release:        9
Summary:        A GObject-based library to access oVirt REST API
License:        LGPLv2+
URL:            http://people.freedesktop.org/~teuf/govirt/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgovirt/0.3/%{name}-%{version}.tar.xz
Source1:        http://ftp.gnome.org/pub/GNOME/sources/libgovirt/0.3/%{name}-%{version}.tar.xz.sign
Source2:        cfergeau-29AC6C82.keyring

BuildRequires:  glib2-devel intltool rest-devel >= 0.7.92
BuildRequires:  gobject-introspection-devel glib-networking dconf gnupg2

%description
GoVirt is a GObject wrapper for the oVirt REST API [1]. It will
only provide very basic functionality as the goal is to
autogenerate a full wrapper as it is already done for the python
bindings.

%package devel
Summary:        Development files for libgovirt

Requires:       %{name} = %{version}-%{release} pkgconfig glib2-devel

%description devel
The libgovirt-devel package contains development files for applications
that use libgovirt.

%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -n %{name}-%{version} -p1

%build
%configure --enable-introspection=yes
%make_build

%install
%make_install
%delete_la_and_a
%find_lang %{name} --with-gnome

%check
make check

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files -f %{name}.lang
%doc AUTHORS COPYING MAINTAINERS README
%{_libdir}/%{name}.so.2*
%{_libdir}/girepository-1.0/GoVirt-1.0.typelib

%files devel
%{_libdir}/%{name}.so
%dir %{_includedir}/govirt-1.0/
%dir %{_includedir}/govirt-1.0/govirt/
%{_includedir}/govirt-1.0/govirt/*.h
%{_libdir}/pkgconfig/govirt-1.0.pc
%{_datadir}/gir-1.0/GoVirt-1.0.gir

%changelog
* Thu Dec 12 2019 Jiangping Hu <hujiangping@huawei.com> - 0.3.4.9
- Package init
