# revision 32228
# category Package
# catalog-ctan /support/latexindent
# catalog-date 2013-11-18 13:22:51 +0100
# catalog-license gpl3
# catalog-version 1.1R
Name:		texlive-latexindent
Version:	1.1R
Release:	7
Summary:	Indent a LaTeX document, highlighting the programming structure
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/latexindent
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexindent.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexindent.doc.tar.xz
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
%{_texmfdistdir}/scripts/latexindent/defaultSettings.yaml
%{_texmfdistdir}/scripts/latexindent/latexindent.pl
%doc %{_texmfdistdir}/doc/support/latexindent/README
%doc %{_texmfdistdir}/doc/support/latexindent/documentation/manual.pdf
%doc %{_texmfdistdir}/doc/support/latexindent/documentation/manual.tex
%doc %{_texmfdistdir}/doc/support/latexindent/indent.yaml
%doc %{_texmfdistdir}/doc/support/latexindent/success/bigTest.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/braceTest.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/braceTestsmall.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/environments.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/filecontents.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/matrix.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/nestedalignment.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/nestedalignment1.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/outputfile.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/preamble.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/pstricks1.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/pstricks2.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/pstricks3.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/sampleAFTER.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/sampleBEFORE.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/stylefile.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/table1.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/table2.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/table3.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/testHeadings.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/testHeadings1.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/theorem.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/tikz1.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/tikz2.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/tikz3.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/tikz4.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/tikz5.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/torusPGF.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/torusPSTricks.tex
%doc %{_texmfdistdir}/doc/support/latexindent/success/trailingComments.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/latexindent/latexindent.pl latexindent
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
