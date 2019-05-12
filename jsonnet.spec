%global _hardened_build 1
%define debug_package %{nil}

Name:     jsonnet
Version:  0.12.1
Release:  1
Summary:  The data templating language
License:  Apache-2.0
URL:      https://github.com/google/jsonnet
Source0:  https://github.com/google/jsonnet/archive/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++

%description
A data templating language for app and tool developers

%prep
%autosetup

%build
make

%install
install -D jsonnet %{buildroot}/%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/%{name}

%changelog
* Sun May 12 2019 Pawel Krupa <pawel@krupa.net.pl> - 0.12.1-1
- Initial release of version 0.12.1

