# Run optional test
%bcond_without perl_Parse_PMFile_enables_optional_test

Name:           perl-Parse-PMFile
Version:        0.43
Release:        4%{?dist}
Summary:        Parses .pm file as PAUSE does
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Parse-PMFile
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Parse-PMFile-%{version}.tar.gz
# Remove useless dependency on ExtUtils::MakeMaker::CPANfile
Patch0:         Parse-PMFile-0.41-Do-not-use-ExtUtils-MakeMaker-CPANfile.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Dumpvalue)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP) >= 2.00
BuildRequires:  perl(Safe)
BuildRequires:  perl(version) >= 0.83
# Tests
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Opcode)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_Parse_PMFile_enables_optional_test}
# Optional tests
# PAUSE::Permissions 0.08 not yet packaged
BuildRequires:  perl(version::vpp)
# Test::Pod not used
# Test::Pod::Coverage not used
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(JSON::PP) >= 2.00
Requires:       perl(version) >= 0.83

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((JSON::PP|version)\\)$

%description
The most of the code of this module is taken from the PAUSE code as of
April 2013 almost verbatim. Thus, the heart of this module should be quite
stable. However, I made it not to use pipe ("-|") as well as I stripped
database-related code. If you encounter any issue, that's most probably
because of my modification.

%prep
%setup -q -n Parse-PMFile-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset TEST_POD
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.43-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.43-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.43-1
- 0.43 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-1
- 0.42 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-7
- Perl 5.28 rebuild

* Fri Jun 01 2018 Petr Pisar <ppisar@redhat.com> - 0.41-6
- Remove useless dependency on ExtUtils::MakeMaker::CPANfile
- Modernize the spec file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-1
- 0.41 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-2
- Perl 5.24 rebuild

* Mon Feb 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-1
- 0.40 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-1
- 0.39 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-2
- Perl 5.22 rebuild

* Mon Apr 20 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-1
- 0.36 bump

* Tue Feb 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-1
- 0.35 bump

* Mon Dec 15 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-1
- 0.33 bump

* Thu Dec 11 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-1
- 0.31 bump

* Mon Dec 08 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-1
- 0.30 bump

* Mon Oct 13 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-1
- 0.29 bump

* Wed Oct 08 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-1
- 0.28 bump

* Tue Sep 23 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-1
- Specfile autogenerated by cpanspec 1.78.
