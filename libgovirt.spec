Name:           libgovirt
Version:        0.3.9
Release:        2
Summary:        A GObject-based library to access oVirt REST API
License:        LGPLv2+
URL:            https://gitlab.gnome.org/GNOME/libgovirt
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgovirt/0.3/%{name}-%{version}.tar.xz
Patch1:         0001-Fix-i18n-generation.patch

BuildRequires:  glib2-devel intltool rest-devel >= 0.9.1
BuildRequires:  gobject-introspection-devel glib-networking dconf gnupg2
BuildRequires:  meson

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
%if "%toolchain" == "clang"
	export CFLAGS="$CFLAGS -Wno-error=unknown-warning-option -Wno-error=typedef-redefinition -Wno-error=missing-field-initializers -Wno-error=cast-align"
	export CXXFLAGS="$CXXFLAGS -Wno-error=unknown-warning-option -Wno-error=typedef-redefinition -Wno-error=missing-field-initializers -Wno-error=cast-align"
%endif
%meson
%meson_build

%install
%meson_install
%delete_la_and_a
%find_lang %{name} --with-gnome

%check
%meson_test

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
* Wed Jun 28 2023 yoo <sunyuechi@iscas.ac.cn> - 0.3.9-2
- fix clang build error

* Fri Dec 2 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 0.3.9-1
- Upgrade to version 0.3.9

* Thu Jun 16 2022 SimpleUpdate Robot <tc@openeuler.org> - 0.3.8-1
- Upgrade to version 0.3.8

* Fri May 22 2020 huanghaitao<huanghaitao8@huawei.com> - 0.3.4-11
- Update tests certificates to fix test error

* Fri Jan 10 2020 yangjian<yangjian79@huawei.com> - 0.3.4-10
- Change the Source to valid address

* Thu Dec 12 2019 Jiangping Hu <hujiangping@huawei.com> - 0.3.4-9
- Package init
