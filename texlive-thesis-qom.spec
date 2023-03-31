Name:		texlive-thesis-qom
Version:	63524
Release:	2
Summary:	Thesis style of the University of Qom, Iran
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thesis-qom
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-qom.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-qom.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a class file for writing theses and
dissertations according to the University of Qom Graduate
Schools's guidelines for the electronic submission of master
theses and PhD dissertations. The class should meet all the
current requirements and is updated whenever the university
guidelines change. The class needs XeLaTeX in conjunction with
the following fonts: XB Niloofar, IranNastaliq, IRlotus, XB
Zar, XB Titre, and Yas.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/thesis-qom
%doc %{_texmfdistdir}/doc/xelatex/thesis-qom

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
