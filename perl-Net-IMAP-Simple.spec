#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	IMAP-Simple
Summary:	Net::IMAP::Simple Perl module - simple IMAP account handling
Summary(pl):	Modu³ Perla Net::IMAP::Simple - prosta obs³uga kont IMAP
Name:		perl-Net-IMAP-Simple
Version:	0.93
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	992e41946ff7cbd7f7545757bc140471
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Net/IMAP
%{perl_vendorlib}/Net/IMAP/Simple.pm
%{_mandir}/man3/*
