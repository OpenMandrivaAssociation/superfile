%global debug_package %{nil}

Name:		superfile
Version:	1.6.1
Release:	1
Source0:	https://github.com/yorukot/superfile/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    	%{name}-%{version}-vendor.tar.xz
Summary:	Pretty fancy and modern terminal file manager
URL:		https://github.com/yorukot/superfile
License:	MIT
Group:		Application/File Manager

BuildRequires:	go


%description
%summary.

%prep
%autosetup -p1
tar -xf %{S:1}

%build
install -dm0755 %{buildroot}%{_bindir}
go build --buildmode=pie -ldflags "-s -w" -o %{buildroot}%{_bindir}/spf

%files
%doc README.md
%license LICENSE
%{_bindir}/spf
