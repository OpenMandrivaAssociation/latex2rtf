%define name	latex2rtf
%define version 2.0.0
%define release %mkrel 1

Summary:	LaTeX to RTF converter
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Publishing
Url:		http://latex2rtf.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	tetex-latex, tetex-dvips, imagemagick

%description
LaTeX2rtf is a translator program which is intended to translate a
LaTeX document (precisely: the text and a limited subset of LaTeX
tags) into the RTF format which can be imported by several
textprocessors (including Microsoft Word for Windows and Word for
Macintosh).

%prep
%setup -q

%build
%make PREFIX=/usr INFO_INSTALL=%{_infodir} MAN_INSTALL=%{_mandir}/man1 CFG_INSTALL=%{_sysconfdir}/%{name} SUPPORT_INSTALL=%{_datadir}/doc/%{name} 

%install
%__rm -rf %{buildroot}
%__install -d -m 755 %{buildroot}%{_datadir}/doc/%{name}
%__make PREFIX=%{buildroot}/usr \
	 MAN_INSTALL=%{buildroot}%{_mandir}/man1 \
     	 CFG_INSTALL=%{buildroot}%{_sysconfdir}/%{name} \
	 SUPPORT_INSTALL=%{buildroot}%{_datadir}/doc/%{name} install
%__install -d -m 755 %{buildroot}%{_infodir}
%__install -m 644 doc/%{name}.info %{buildroot}%{_infodir}

%post
%_install_info %{name}.info

%postun
%_remove_install_info %{name}.info

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog Copyright README
%{_bindir}/*
%{_sysconfdir}/%{name}
%{_infodir}/*
%{_mandir}/man1/*
