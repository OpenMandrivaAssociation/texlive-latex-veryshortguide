# revision 29803
# category Package
# catalog-ctan /info/latex-veryshortguide
# catalog-date 2013-01-22 18:02:11 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-latex-veryshortguide
Version:	20130122
Release:	8
Summary:	The Very Short Guide to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex-veryshortguide
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-veryshortguide.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-veryshortguide.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a 4-page reminder of what LaTeX does. It is designed
for printing on A4 paper, double-sided, and folding once to A5.
(Such an 'imposed' version of the document is provided in the
distribution, as PDF.).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/README
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/build
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/index.html
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/menno-a.eps
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/menno-a.jpg
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/veryshortguide-imposed.pdf
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/veryshortguide.pdf
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/veryshortguide.tex
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/vsg-1.jpg
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/vsg-2.jpg
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/vsg-3.jpg
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/vsg-4.jpg

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
