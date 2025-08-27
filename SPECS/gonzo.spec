%define debug_package %{nil}

Name:           gonzo
Version:        0.1.5
Release:        1%{?dist}
Summary:        Gonzo! The Go based TUI log analysis tool
Group:          Applications/System
License:        MIT
URL:            https://gonzo.controltheory.com
Source:         https://github.com/control-theory/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang

%description
A powerful, real-time log analysis terminal UI inspired by k9s. Analyze log streams
with beautiful charts, AI-powered insights, and advanced filtering - all from your terminal.

%prep
%setup -q -n %{name}-%{version}

%build
make build

%install
install -Dm0755 %{_builddir}/%{name}-%{version}/build/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Aug 28 2025 Jamie Curnow <jc@jc21.com> 0.1.5-1
- https://github.com/control-theory/gonzo/releases/tag/v0.1.5
