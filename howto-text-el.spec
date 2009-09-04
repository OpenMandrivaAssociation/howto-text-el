%define format	text-el
%define format2	TEXT/el
%define	format3 text

%define version 2006
%define release %mkrel 5

Summary:	HOWTO documents (%{format3} format) from the Linux Documentation Project
Name:		howto-%{format}
Version: 	%version
Release: 	%release
Group:		Books/Howtos
Source0:	howto-%{format}.tar.bz2
Url:		http://www.linuxdoc.org/docs.html#howto
License:	GPL
BuildRoot:	%{_tmppath}/howto-%{format}-root
BuildArchitectures: noarch
Requires:   locales-el howto-utils
BuildRequires:  howto-utils


%description
Linux HOWTOs are detailed documents which describe a specific aspect of 
configuring or using Linux.  Linux HOWTOs are a great source of
practical information about your system.  The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

Install this package if you'd like to be able to access the Linux
HOWTO documentation from your own system.

%description -l fr
Les HOWTO Linux sont des documents décrivant de façon exhaustive un aspect de
la configuration ou de l'utilisation d'un système Linux. Les HOWTO Linux sont
l'une des meilleures sources d'information sur la pratique de votre système. La
dernière version de chacun de ces documents peut être touvée à cette adresse :
http://www.linuxdoc.org/docs.html#howto

%prep 
rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
cd $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
bzcat %{SOURCE0} | tar xv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_docdir}/HOWTO/%{format2}


