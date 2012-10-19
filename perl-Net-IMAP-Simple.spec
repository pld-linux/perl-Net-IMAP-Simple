#
# Conditional build:
%bcond_with	tests		# do not perform "make test"
#
%define		pdir	Net
%define		pnam	IMAP-Simple
%include	/usr/lib/rpm/macros.perl
Summary:	Net::IMAP::Simple - Perl extension for simple IMAP account handling.
Summary(pl.UTF-8):     Moduł Perla Net::IMAP::Simple - prosta obsługa kont IMAP
Name:		perl-Net-IMAP-Simple
Version:	1.2034
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	15dda3b14ea13172923ad7914fe64656
URL:		http://search.cpan.org/dist/Net-IMAP-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Parse-RecDescent
%endif
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
%{echo} "n" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Net/IMAP/*.pm
%{perl_vendorlib}/Net/IMAP/Simple
%{_mandir}/man3/*
