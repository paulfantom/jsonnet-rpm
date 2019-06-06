%global _hardened_build 1
%define debug_package %{nil}

Name:     jsonnet
Version:  0.13.0
Release:  2
Summary:  The data templating language
License:  Apache-2.0
URL:      https://github.com/google/jsonnet
Source0:  https://github.com/google/jsonnet/archive/v%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
%{?el7:BuildRequires: devtoolset-7-gcc}
%{?el7:BuildRequires: devtoolset-7-gcc-c++}

%description
A data templating language for app and tool developers

%prep
%autosetup

%build
%{?el7:scl enable devtoolset-7 --} make

%install
install -D jsonnet %{buildroot}/%{_bindir}/%{name}
install -D jsonnetfmt %{buildroot}/%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/%{name}

#%check
#make test # currently tests are written in python2 which is not available in F30

%changelog
* Tue Jun 05 2019 Pawel Krupa <pawel@krupa.net.pl> - 0.13.0-2
- Add jsonnetfmt binary

* Tue Jun 04 2019 Pawel Krupa <pawel@krupa.net.pl> - 0.13.0-1
- Automated release of jsonnet version 0.13.0

* Sun May 12 2019 Pawel Krupa <pawel@krupa.net.pl> - 0.12.1-1
- Initial release of version 0.12.1

