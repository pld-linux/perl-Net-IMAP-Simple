#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	IMAP-Simple
Summary:	Net::IMAP::Simple Perl module - simple IMAP account handling
Summary(pl.UTF-8):	Moduł Perla Net::IMAP::Simple - prosta obsługa kont IMAP
Name:		perl-Net-IMAP-Simple
Version:	0.95
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CW/CWEST/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8ea3b099c5755237377dbcf13c0513c9
URL:		http://search.cpan.org/dist/Net-IMAP-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a simple way to access IMAP accounts. The API is mostly
equivalent to the Net::POP3 one, with some aditional methods for
mailbox handling.

%description -l pl.UTF-8
Ten moduł pozwala na łatwy dostęp do kont IMAP. API w większości
odpowiada temu z modułu Net::POP3, z paroma dodatkowymi metodami do
obsługi skrzynek.

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
