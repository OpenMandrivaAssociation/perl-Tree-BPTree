%define upstream_name    Tree-BPTree
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl implementation of B+ trees
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Tree/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
This is a Perl implementation of B+ trees. I have based this
implementation on a couple of sources. See the documentation of
Tree::BPTree for those details. A B+ tree is essentially an order
map from keys to values. Keys are multivalued so that there may be
more than one value per key. This implementation will enforce
uniqueness of keys, if requested.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Tree
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 405768
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.08-4mdv2009.0
+ Revision: 258694
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.08-3mdv2009.0
+ Revision: 246661
- rebuild

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2008.1
+ Revision: 138073
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.07-3mdv2008.1
+ Revision: 123857
- kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-3mdv2008.0
+ Revision: 87061
- rebuild


* Fri Aug 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-2mdv2007.0
- spec cleanup
- fix directory ownership
- %%mkrel

* Tue Aug 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdk
- New release 1.07
- use Module::Build instead of MakeMaker

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.06-1mdk
- initial Mandriva package

