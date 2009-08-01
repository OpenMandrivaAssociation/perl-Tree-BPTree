%define upstream_name    Tree-BPTree
%define upstream_version 1.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl implementation of B+ trees
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Tree/%{upstream_name}-%{upstream_version}.tar.bz2

Buildrequires:	perl(Module::Build)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Tree
%{_mandir}/*/*
