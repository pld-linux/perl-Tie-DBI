%include	/usr/lib/rpm/macros.perl
Summary:	Tie-DBI perl module
Summary(pl):	Modu³ perla Tie-DBI
Name:		perl-Tie-DBI
Version:	0.85
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/Tie-DBI-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-DBI
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-DBI allows you to tie Perl associative arrays to SQL databases
using the DBI interface.

%description -l pl
Tie-DBI pozwala na wi±zanie tablic asocjacyjnych perla z bazamu SQL
wykorzystuj±c interfejs DBI.

%prep
%setup -q -n Tie-DBI-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tie/DBI
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Tie/*.pm
%{perl_sitearch}/auto/Tie/DBI

%{_mandir}/man3/*
