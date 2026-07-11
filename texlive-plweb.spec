%global tl_name plweb
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2
Release:	%{tl_revision}.1
Summary:	Literate Programming for Prolog with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gene/pl
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plweb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plweb.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plweb.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Instead of having to transform the common source into program or
documentation, the central idea was to develop a method to have one
common source which can be interpreted by a Prolog system as well as by
LaTeX, whether that Prolog system be C-Prolog, Quintus-Prolog, or
ECLiPSe.

