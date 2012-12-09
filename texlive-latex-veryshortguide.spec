# revision 25084
# category Package
# catalog-ctan /info/latex-veryshortguide
# catalog-date 2012-01-12 15:07:54 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-latex-veryshortguide
Version:	20120112
Release:	1
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
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/README.pdf
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/menno-a.eps
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/menno-a.jpg
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/veryshortguide-imposed.pdf
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/veryshortguide.pdf
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide/veryshortguide.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120112-1
+ Revision: 762660
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091109-2
+ Revision: 753203
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091109-1
+ Revision: 718830
- texlive-latex-veryshortguide
- texlive-latex-veryshortguide
- texlive-latex-veryshortguide
- texlive-latex-veryshortguide

