%define		plugin		smblink
Summary:	Plugin to make Windows Share Links globally accessible
Name:		dokuwiki-plugin-%{plugin}
Version:	20090209
Release:	0.2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://doku-smblink.googlecode.com/files/smblink.zip
# Source0-md5:	b880e7d257904050c97396ffbd7a9d5e
URL:		http://wiki.splitbrain.org/plugin:smblink
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir	/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
A replacement for DokuWiki's default Windows Share Link feature which
supports Firefox-like browsers.

This plugin replaces the default action of Windows Share Links (WSL)
to better support the Firefox browser.

%prep
%setup -qc
mv %{plugin}/* .
%undos *.php

version=$(awk -F"'" '/date/{print $4}' syntax.php)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
