# revision 15878
# category Package
# catalog-ctan /info/latex-veryshortguide
# catalog-date 2009-11-09 22:53:30 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-latex-veryshortguide
Version:	20091109
Release:	1
Summary:	The Very Short Guide to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex-veryshortguide
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-veryshortguide.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-veryshortguide.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a 4-page reminder of what LaTeX does. It is designed
for printing on A4 paper, double-sided, and folding once to A5.
(Such an 'imposed' version of the document is provided in the
distribution, as PDF.).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/README
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/README.pdf
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/menno-a.eps
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/menno-a.jpg
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/veryshortguide-imposed.pdf
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/veryshortguide.pdf
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/veryshortguide.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
