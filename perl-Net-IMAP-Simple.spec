#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	IMAP-Simple
Summary:	Net::IMAP::Simple Perl module - simple IMAP account handling
Summary(pl):	Modu³ Perla Net::IMAP::Simple - prosta obs³uga kont IMAP
Name:		perl-Net-IMAP-Simple
Version:	0.93
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a simple way to access IMAP accounts. The API is mostly
equivalent to the Net::POP3 one, with some aditional methods for
mailbox handling.

%description -l pl
Ten modu³ pozwala na ³atwy dostêp do kont IMAP. API w wiêkszo¶ci
odpowiada temu z modu³u Net::POP3, z paroma dodatkowymi metodami do
obs³ugi skrzynek.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_sitelib}/Net/IMAP
%{perl_sitelib}/Net/IMAP/Simple.pm
%{_mandir}/man3/*
