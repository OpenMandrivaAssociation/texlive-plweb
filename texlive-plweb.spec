Name:		texlive-plweb
Version:	3.0
Release:	1
Summary:	Literate Programming for Prolog with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gene/pl
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plweb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plweb.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plweb.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Instead of having to transform the common source into program
or documentation, the central idea was to develop a method to
have one common source which can be interpreted by a Prolog
system as well as by LaTeX, whether that Prolog system be C-
Prolog, Quintus-Prolog, or ECLiPSe.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/plweb/pcode.sty
%{_texmfdistdir}/tex/latex/plweb/pl.cfg
%{_texmfdistdir}/tex/latex/plweb/pl.sty
%doc %{_texmfdistdir}/doc/latex/plweb/README
%doc %{_texmfdistdir}/doc/latex/plweb/pl.pdf
%doc %{_texmfdistdir}/doc/latex/plweb/pl.tex
%doc %{_texmfdistdir}/doc/latex/plweb/sample.pl
#- source
%doc %{_texmfdistdir}/source/latex/plweb/Makefile
%doc %{_texmfdistdir}/source/latex/plweb/pl.dtx
%doc %{_texmfdistdir}/source/latex/plweb/pl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
