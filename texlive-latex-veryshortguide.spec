Name:		texlive-latex-veryshortguide
Version:	55228
Release:	1
Summary:	The Very Short Guide to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex-veryshortguide
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-veryshortguide.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-veryshortguide.doc.r%{version}.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/latex-veryshortguide

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
