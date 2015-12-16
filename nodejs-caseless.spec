%{?scl:%scl_package nodejs-caseless}
%{!?scl:%global pkg_name %{name}}
%global npm_name caseless

%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-caseless
Version:	0.11.0
Release:	1%{?dist}
Summary:	Caseless object set/get/has, very useful when working with HTTP headers.
Url:		https://github.com/mikeal/caseless
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ASL 2.0

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	npm(tape)
%endif

%description
Caseless object set/get/has, very useful when working with HTTP headers.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
node test.js
%endif

%files
%{nodejs_sitelib}/caseless

%doc README.md LICENSE

%changelog
* Thu Jul 16 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.11.0-1
- Initial build
