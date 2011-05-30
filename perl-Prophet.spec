%define upstream_name    Prophet
%define upstream_version 0.743

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    A distributed database system
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Any::Moose)
BuildRequires: perl(Config::GitLike)
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBI)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Exporter::Lite)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(HTTP::Date)
BuildRequires: perl(HTTP::Server::Simple)
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(JSON)
BuildRequires: perl(JSON::XS)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MIME::Base64::URLSafe)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Module::Refresh)
BuildRequires: perl(Mouse)
BuildRequires: perl(Net::Bonjour)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Path::Dispatcher)
BuildRequires: perl(Proc::InvokeEditor)
BuildRequires: perl(Template::Declare)
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Term::ReadLine::Perl)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::HTTP::Server::Simple)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::WWW::Mechanize)
BuildRequires: perl(Time::Progress)
BuildRequires: perl(URI)
BuildRequires: perl(UUID::Tiny)
BuildRequires: perl(XML::Atom::SimpleFeed)
BuildRequires: perl(YAML::Syck)
BuildRequires: perl(Path::Dispatcher::Declarative)
# for testing
BuildRequires: rsync

Requires:      perl(Path::Dispatcher::Declarative) 
# for server
Requires:      perl(HTTP::Server::Simple::CGI)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/


