%define name linky
%define version 1.0
%define unmangled_version 1.0
%define unmangled_version 1.0
%define release 1

Summary: aplicativo para generar inventarios con Ansible
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: DXC-SRE-Middleware <UNKNOWN>
Url: https://github.com/renatogermanib/linky-rpm

%description
Archivo de especificaciones para la generación de empaquetado rpm

%pre
echo python3 /usr/lib/python3.6/site-packages/aplicativo/linky.py > /usr/bin/linky
chmod 755 /usr/bin/linky

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
