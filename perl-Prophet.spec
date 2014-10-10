%define upstream_name    Prophet
%define upstream_version 0.743

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A distributed database system
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Config::GitLike)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Exporter::Lite)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(HTTP::Server::Simple)
BuildRequires:	perl(HTTP::Server::Simple::CGI)
BuildRequires:	perl(IPC::Run3)
BuildRequires:	perl(JSON)
BuildRequires:	perl(JSON::XS)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(MIME::Base64::URLSafe)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Module::Refresh)
BuildRequires:	perl(Mouse)
BuildRequires:	perl(Net::Bonjour)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Path::Dispatcher)
BuildRequires:	perl(Proc::InvokeEditor)
BuildRequires:	perl(Template::Declare)
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(Term::ReadLine::Perl)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::HTTP::Server::Simple)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Test::WWW::Mechanize)
BuildRequires:	perl(Time::Progress)
BuildRequires:	perl(URI)
BuildRequires:	perl(UUID::Tiny)
BuildRequires:	perl(XML::Atom::SimpleFeed)
BuildRequires:	perl(YAML::Syck)
BuildRequires:	perl(Path::Dispatcher::Declarative)
# for testing
BuildRequires:	rsync

Requires:		perl(Path::Dispatcher::Declarative)
# for server
Requires:		perl(HTTP::Server::Simple::CGI)

BuildArch: noarch

%description
Prophet is a distributed database system designed for small to medium scale
social database applications. Our early targets include things such as bug
tracking.

Design goals
    * Arbitrary record schema

    * Replication

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/

%changelog
* Mon May 30 2011 Funda Wang <fwang@mandriva.org> 0.743.0-3mdv2011.0
+ Revision: 681767
- rebuild
- rebuild for updated spec-helper

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.743.0-1mdv2011.0
+ Revision: 553137
- update to 0.743

* Fri May 07 2010 Michael Scherer <misc@mandriva.org> 0.741.0-3mdv2010.1
+ Revision: 543208
- fix Requires again, and summary too

* Fri May 07 2010 Michael Scherer <misc@mandriva.org> 0.741.0-2mdv2010.1
+ Revision: 543197
- fix requires

* Wed May 05 2010 Michael Scherer <misc@mandriva.org> 0.741.0-1mdv2010.1
+ Revision: 542611
- import perl-Prophet


* Fri Apr 30 2010 cpan2dist 0.741-1mdv
- initial mdv release, generated with cpan2dist
