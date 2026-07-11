%global tl_name latex-veryshortguide
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	The Very Short Guide to LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex-veryshortguide
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-veryshortguide.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-veryshortguide.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a 4-page reminder of what LaTeX does. It is designed for
printing on A4 paper, double-sided, and folding once to A5. Such an
'imposed' version of the document is provided in the distribution, as
PDF. An analogous version is provided in 'legal' format.

