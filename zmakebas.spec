Summary:	Convert text into ZX Spectrum Basic programs
Summary(pl.UTF-8):	Konwerter plików tekstowych na Basic ZX Spectrum
Name:		zmakebas
Version:	1.2
Release:	1
License:	Public domain
Group:		Development/Tools
Source0:	http://ftp.debian.org/debian/pool/main/z/zmakebas/%{name}_%{version}.orig.tar.gz
# Source0-md5:	c141846817cfa779c460d38b535b11cd
URL:		http://www.svgalib.org/rus/zmakebas.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zmakebas converts a Spectrum Basic program written as a text file into
an actual speccy Basic file (as a .TAP file, or optionally a raw
headerless file).

Using zmakebas rather than (say) writing the Basic in an emulator
means you can write using a nicer editor, and can use tools which work
on text files, etc. Also, with the `-l' option you can write without
line numbers, using labels in their place where necessary.

The program was originally intended to be used simply to make little
loader programs, so they wouldn't have to be sourceless binaries.
However, I went to a fair amount of effort to make sure it'd work for
bigger, more serious programs too, so you can also use it for that
kind of thing.

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o zmakebas zmakebas.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_bindir},%{_mandir}/man1}

install zmakebas $RPM_BUILD_ROOT%{_bindir}
install zmakebas.1 $RPM_BUILD_ROOT%{_mandir}/man1
install *.bas $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/zmakebas
%{_mandir}/man1/zmakebas.1*
%{_examplesdir}/%{name}-%{version}
