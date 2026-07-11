%global tl_name standalone
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5a
Release:	%{tl_revision}.1
Summary:	Compile TeX pictures stand-alone or as part of a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/standalone
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/standalone.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/standalone.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/standalone.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(adjustbox)
Requires:	texlive(currfile)
Requires:	texlive(filemod)
Requires:	texlive(gincltex)
Requires:	texlive(xkeyval)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A class and package is provided which allows TeX pictures or other TeX
code to be compiled standalone or as part of a main document. Special
support for pictures with beamer overlays is also provided. The package
is used in the main document and skips extra preambles in sub-files. The
class may be used to simplify the preamble in sub-files. By default the
preview package is used to display the typeset code without margins. The
behaviour in standalone mode may adjusted using a configuration file
standalone.cfg to redefine the standalone environment.

