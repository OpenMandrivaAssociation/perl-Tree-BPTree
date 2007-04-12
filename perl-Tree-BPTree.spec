%define module Tree-BPTree
%define name	perl-%{module}
%define version 1.07
%define release %mkrel 2

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Perl implementation of B+ trees
License:	    GPL or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{module}/
Source:		    http://www.cpan.org/modules/by-module/Tree/%{module}-%{version}.tar.bz2
Buildrequires:	perl(Module::Build)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This is a Perl implementation of B+ trees. I have based this
implementation on a couple of sources. See the documentation of
Tree::BPTree for those details. A B+ tree is essentially an order
map from keys to values. Keys are multivalued so that there may be
more than one value per key. This implementation will enforce
uniqueness of keys, if requested.


%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Tree
%{_mandir}/*/*

