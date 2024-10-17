%define upstream_name    Dist-Zilla-Plugin-Mercurial
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Check for modified/removed/unknown files

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(IPC::System::Simple)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(autodie)
BuildArch:	noarch

%description
This plugin provides Mercurial support for the Dist::Zilla manpage.
Currently, it supports checking that the working copy is clean before
release, tagging, and pushing changes to the remote. The tag plugin also
checks before tagging to make sure that the tag it wants to use is unique.

Currently, this plugin does not support committing, so it won't play nice
with plugins that make changes to the working copy before release. Patches
are welcome.

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
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*



