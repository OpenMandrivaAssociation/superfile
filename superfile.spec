Name:		superfile
Version:	1.3.3
Release:	1
Source0:	https://github.com/yorukot/superfile/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}-%{version}-vendor.tar.gz
Summary:	Pretty fancy and modern terminal file manager
URL:		https://github.com/yorukot/superfile
License:	MIT
Group:		Application/File Manager

BuildRequires:	go


%description
%summary.

%prep
%autosetup -p1
tar -xvf %{S:1}

%build
install -dm0755 %{buildroot}%{_bindir}
go build -o %{buildroot}%{_bindir}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
