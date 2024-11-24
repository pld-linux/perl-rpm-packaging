Summary:	Additional utilities for checking Perl provides/requires in RPM packages
Summary(de.UTF-8):	Zusatzwerkzeuge fürs Nachsehen Perl-Abhängigkeiten in RPM-Paketen
Summary(pl.UTF-8):	Dodatkowe narzędzia do sprawdzenia zależności skryptów Perla w pakietach RPM
Name:		perl-rpm-packaging
Version:	1.1
Release:	0.1
License:	GPL v2
Group:		Base
Source0:	https://github.com/rpm-software-management/perl-rpm-packaging/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7dfd1670fd1c3c002719b604bd2801e3
URL:		https://github.com/rpm-software-management/perl-rpm-packaging
BuildRequires:	rpm-build >= 4.6
Requires:	perl-Encode
Requires:	perl-devel
Requires:	perl-modules
Requires:	rpm
Provides:	rpm-perlprov = 1:4.20
Obsoletes:	rpm-perlprov < 1:4.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_rpmlibdir /usr/lib/rpm

%description
Additional utilities for checking Perl provides/requires in RPM
packages.

%description -l de.UTF-8
Zusatzwerkzeuge fürs Nachsehen Perl-Abhängigkeiten in RPM-Paketen.

%description -l pl.UTF-8
Dodatkowe narzędzia do sprawdzenia zależności skryptów Perla w
pakietach RPM.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_rpmlibdir}/fileattrs

cp -p fileattrs/*.attr $RPM_BUILD_ROOT%{_rpmlibdir}/fileattrs
cp -p scripts/perl.prov $RPM_BUILD_ROOT%{_rpmlibdir}
cp -p scripts/perl.req $RPM_BUILD_ROOT%{_rpmlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_rpmlibdir}/perl.prov
%attr(755,root,root) %{_rpmlibdir}/perl.req
%{_rpmlibdir}/fileattrs/perl.attr
%{_rpmlibdir}/fileattrs/perllib.attr