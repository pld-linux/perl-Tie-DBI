%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	DBI
Summary:	Tie::DBI perl module
Summary(pl):	Modu³ perla Tie::DBI
Name:		perl-Tie-DBI
Version:	0.91
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::DBI allows you to tie Perl associative arrays to SQL databases
using the DBI interface.

%description -l pl
Tie::DBI pozwala na wi±zanie tablic asocjacyjnych perla z bazami SQL
wykorzystuj±c interfejs DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Tie/*.pm
%{_mandir}/man3/*
