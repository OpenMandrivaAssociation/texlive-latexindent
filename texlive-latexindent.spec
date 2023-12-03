Name:		texlive-latexindent
Version:	68909
Release:	1
Summary:	Indent a LaTeX document, highlighting the programming structure
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/latexindent
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexindent.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexindent.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-latexindent.bin = %{EVRD}

%description
The Perl script (also available as a windows executable)
processes a LaTeX file, indenting parts so as to highlight the
structure for the reader.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/latexindent
%{_texmfdistdir}/scripts/latexindent
%doc %{_texmfdistdir}/doc/support/latexindent

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/latexindent/latexindent.pl latexindent
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
