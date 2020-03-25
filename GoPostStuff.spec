#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

%define  debug_package %{nil}

Name:		GoPostStuff
Version:	0.3.0
Release:	1%{?dist}
Summary:	UseNet binary poster

License:	MIT
URL:		https://github.com/madcowfred/GoPostStuff
Source0:	GoPostStuff-0.3.0.tar.gz
Patch0:		gcfg-repo.patch
BuildArch:	x86_64

BuildRequires:	gcc-go


%description
GoPostStuff is a simple client for posting binaries to Usenet.


%prep
%setup
%patch0


%build
export GOPATH="$(pwd)/go"
go install github.com/madcowfred/GoPostStuff
cp ${GOPATH}/src/github.com/madcowfred/GoPostStuff/LICENSE .
cp ${GOPATH}/src/github.com/madcowfred/GoPostStuff/README.md .


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} go/bin/GoPostStuff


%files
%doc README.md
%license LICENSE
%{_bindir}/GoPostStuff


%changelog
* Wed Mar 25 2020 David King <dave@daveking.com> - 0.3.0-1
	Initial Version