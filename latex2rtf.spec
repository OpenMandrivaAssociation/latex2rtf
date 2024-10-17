Summary:	LaTeX to RTF converter
Name:		latex2rtf
Version:	2.1.0
Release:	3
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Publishing
Url:		https://latex2rtf.sourceforge.net/
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
%__install -d -m 755 %{buildroot}%{_datadir}/doc/%{name}
%__make PREFIX=%{buildroot}/usr \
	 MAN_INSTALL=%{buildroot}%{_mandir}/man1 \
     	 CFG_INSTALL=%{buildroot}%{_sysconfdir}/%{name} \
	 SUPPORT_INSTALL=%{buildroot}%{_datadir}/doc/%{name} install
%__install -d -m 755 %{buildroot}%{_infodir}
%__install -m 644 doc/%{name}.info %{buildroot}%{_infodir}



%files
%doc ChangeLog Copyright README
%{_bindir}/*
%{_sysconfdir}/%{name}
%{_infodir}/*
%{_mandir}/man1/*


%changelog
* Fri May 28 2010 Lev Givon <lev@mandriva.org> 2.1.0-1mdv2011.0
+ Revision: 546541
- Update to 2.1.0.

* Fri Feb 19 2010 Lev Givon <lev@mandriva.org> 2.0.0-1mdv2010.1
+ Revision: 508335
- import latex2rtf

