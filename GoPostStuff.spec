# The MIT License (MIT)
#
# Copyright (c) 2020  David King (dave@daveking.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

%define  debug_package %{nil}

Name:		GoPostStuff
Version:	0.3.0
Release:	5%{?dist}
Summary:	UseNet binary poster

License:	MIT
URL:		https://github.com/madcowfred/GoPostStuff
Source0:	%{name}-%{version}.tar.gz
Patch0:		gcfg-repo.patch
BuildArch:	x86_64

%if 0%{?fedora}
BuildRequires:	gcc-go
%endif
%if 0%{?rhel}
BuildRequires:	golang
%endif


%description
GoPostStuff is a simple command-line utility for posting binary files to UseNet
newsgroups.


%prep
%setup
%patch0


%build
export GOPATH="$(pwd)/go"
go install github.com/madcowfred/GoPostStuff
go install github.com/madcowfred/gopoststuff
cp ${GOPATH}/src/github.com/madcowfred/GoPostStuff/LICENSE .
cp ${GOPATH}/src/github.com/madcowfred/GoPostStuff/README.md .
cp ${GOPATH}/src/github.com/madcowfred/GoPostStuff/sample.conf .


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} go/bin/GoPostStuff
install -m 755 -t %{buildroot}%{_bindir} go/bin/gopoststuff


%files
%doc README.md
%doc sample.conf
%license LICENSE
%{_bindir}/GoPostStuff
%{_bindir}/gopoststuff


%post
if [ $1 == 1 ]; then
	echo -e "\n  ******************************************************************************"
	echo "  *  Before running GoPostStuff for the first time you must copy the           *"
	echo -e "  *  /usr/share/doc/GoPostStuff/sample.conf file to \${HOME}/.gopoststuff.conf  *"
	echo "  *  and modify it to suit your requirements.                                  *"
	echo "  ******************************************************************************"
fi
exit 0

%changelog
* Fri Mar 27 2020 David King <dave@daveking.com> - 0.3.0-5
	Modify post scriptlet so it only displays message on install, not upgrade
* Fri Mar 27 2020 David King <dave@daveking.com> - 0.3.0-4
	Add sample.conf file to package
* Thu Mar 26 2020 David King <dave@daveking.com> - 0.3.0-3
	Enable building for CentOS
* Thu Mar 26 2020 David King <dave@daveking.com> - 0.3.0-2
	Add build for "gopoststuff" binary in addition to "GoPostStuff"
* Wed Mar 25 2020 David King <dave@daveking.com> - 0.3.0-1
	Initial Version
