%define debug_package %{nil}

# The web dashboard needs Node.js >= 18. EL8/EL9 only ship that as a
# non-default module stream, so use the upstream Node.js binary there.
%if 0%{?rhel} && 0%{?rhel} < 10
%global bundled_node 1
%global node_version 24.21.0
%ifarch x86_64
%global node_arch x64
%endif
%ifarch aarch64
%global node_arch arm64
%endif
%endif

Name:           gonzo
Version:        0.4.3
Release:        1%{?dist}
Summary:        Gonzo! The Go based TUI log analysis tool
Group:          Applications/System
License:        MIT
URL:            https://gonzo.controltheory.com
Source:         https://github.com/control-theory/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang
%if 0%{?bundled_node}
Source1:        https://nodejs.org/dist/v%{node_version}/node-v%{node_version}-linux-%{node_arch}.tar.xz
%else
BuildRequires:  nodejs
BuildRequires:  npm
%endif

%description
A powerful, real-time log analysis terminal UI inspired by k9s. Analyze log streams
with beautiful charts, AI-powered insights, and advanced filtering - all from your terminal.

%prep
%setup -q -n %{name}-%{version}
%if 0%{?bundled_node}
%setup -q -T -D -a 1 -n %{name}-%{version}
%endif

%build
%if 0%{?bundled_node}
export PATH="$(pwd)/node-v%{node_version}-linux-%{node_arch}/bin:$PATH"
%endif
make build

%install
install -Dm0755 %{_builddir}/%{name}-%{version}/build/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Jul 16 2026 Jamie Curnow <jc@jc21.com> 0.4.3-1
- https://github.com/control-theory/gonzo/releases/tag/v0.4.3

* Mon May 18 2026 Jamie Curnow <jc@jc21.com> 0.4.2-1
- https://github.com/control-theory/gonzo/releases/tag/v0.4.2

* Thu May 7 2026 Jamie Curnow <jc@jc21.com> 0.4.1-1
- https://github.com/control-theory/gonzo/releases/tag/v0.4.1

* Thu May 7 2026 Jamie Curnow <jc@jc21.com> 0.4.0-1
- https://github.com/control-theory/gonzo/releases/tag/v0.4.0

* Thu Apr 23 2026 Jamie Curnow <jc@jc21.com> 0.3.2-1
- https://github.com/control-theory/gonzo/releases/tag/v0.3.2

* Wed Feb 18 2026 Jamie Curnow <jc@jc21.com> 0.3.1-1
- https://github.com/control-theory/gonzo/releases/tag/v0.3.1

* Tue Dec 2 2025 Jamie Curnow <jc@jc21.com> 0.3.0-1
- https://github.com/control-theory/gonzo/releases/tag/v0.3.0

* Tue Nov 25 2025 Jamie Curnow <jc@jc21.com> 0.2.2-1
- https://github.com/control-theory/gonzo/releases/tag/v0.2.2

* Tue Oct 7 2025 Jamie Curnow <jc@jc21.com> 0.2.1-1
- https://github.com/control-theory/gonzo/releases/tag/v0.2.1

* Tue Sep 23 2025 Jamie Curnow <jc@jc21.com> 0.2.0-1
- https://github.com/control-theory/gonzo/releases/tag/v0.2.0

* Fri Sep 5 2025 Jamie Curnow <jc@jc21.com> 0.1.7-1
- https://github.com/control-theory/gonzo/releases/tag/v0.1.7

* Thu Aug 28 2025 Jamie Curnow <jc@jc21.com> 0.1.5-1
- https://github.com/control-theory/gonzo/releases/tag/v0.1.5

