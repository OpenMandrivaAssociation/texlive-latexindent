%global tl_name latexindent
%global tl_revision 79306

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.0.2
Release:	%{tl_revision}.1
Summary:	Indent a LaTeX document, highlighting the programming structure
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/latexindent
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexindent.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexindent.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(latexindent.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Perl script processes a LaTeX file, indenting parts so as to
highlight the structure for the reader. Included are also binary
(executable) files for Windows, Ubuntu Linux, and macOS.

