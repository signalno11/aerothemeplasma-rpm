%global debug_package %{nil}

%global commit 96950b8028a5d960cb683280fe5f1d9e33e6b8a2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           aerothemeplasma-icons
Version:        6.7.0
Release:        1.git%{shortcommit}%{?dist}
Summary:        Icon theme designed for AeroThemePlasma

License:        AGPLv3
URL:            https://gitgud.io/aeroshell/atp/aerothemeplasma-icons
Source:         https://gitgud.io/aeroshell/atp/%{name}/-/archive/%{commit}/%{name}-%{shortcommit}.zip

BuildRequires:  cmake make gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  git

%description
Icon theme designed for AeroThemePlasma

%prep
%autosetup -n %{name}-%{commit}
rm LICENSE
rm README.md

%build
%cmake

%install
%cmake_install


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :
kbuildsycoca6 &> /dev/null || :

%files
%{_datadir}/icons/*

%changelog
%autochangelog