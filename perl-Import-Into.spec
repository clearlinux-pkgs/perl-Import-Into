#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Import-Into
Version  : 1.002005
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Import-Into-1.002005.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Import-Into-1.002005.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libimport-into-perl/libimport-into-perl_1.002005-1.debian.tar.xz
Summary  : 'Import packages into other packages'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Import-Into-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Runtime)

%description
NAME
Import::Into - Import packages into other packages
SYNOPSIS
package My::MultiExporter;

%package dev
Summary: dev components for the perl-Import-Into package.
Group: Development
Provides: perl-Import-Into-devel = %{version}-%{release}

%description dev
dev components for the perl-Import-Into package.


%package license
Summary: license components for the perl-Import-Into package.
Group: Default

%description license
license components for the perl-Import-Into package.


%prep
%setup -q -n Import-Into-1.002005
cd ..
%setup -q -T -D -n Import-Into-1.002005 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Import-Into-1.002005/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Import-Into
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Import-Into/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Import/Into.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Import::Into.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Import-Into/deblicense_copyright
