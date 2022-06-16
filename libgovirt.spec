Name:           libgovirt
Version:        0.3.8
Release:        1
Summary:        A GObject-based library to access oVirt REST API
License:        LGPLv2+
URL:            http://people.freedesktop.org/~teuf/govirt/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgovirt/0.3/%{name}-%{version}.tar.xz

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
* Thu Jun 16 2022 SimpleUpdate Robot <tc@openeuler.org> - 0.3.8-1
- Upgrade to version 0.3.8

* Fri May 22 2020 huanghaitao<huanghaitao8@huawei.com> - 0.3.4-11
- Update tests certificates to fix test error

* Fri Jan 10 2020 yangjian<yangjian79@huawei.com> - 0.3.4-10
- Change the Source to valid address

* Thu Dec 12 2019 Jiangping Hu <hujiangping@huawei.com> - 0.3.4-9
- Package init
