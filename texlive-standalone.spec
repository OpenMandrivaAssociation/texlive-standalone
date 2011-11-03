# revision 22017
# category Package
# catalog-ctan /macros/latex/contrib/standalone
# catalog-date 2011-04-07 23:51:14 +0200
# catalog-license lppl1.3
# catalog-version 0.4a
Name:		texlive-standalone
Version:	0.4a
Release:	1
Summary:	Compile TeX pictures stand-alone or as part of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/standalone
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/standalone.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/standalone.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/standalone.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A class and package is provided which allows TeX pictures or
other TeX code to be compiled standalone or as part of a main
document. Special support for pictures with beamer overlays is
also provided. The package is used in the main document and
skips extra preambles in sub-files. The class may be used to
simplify the preamble in sub-files. By default the preview
package is used to display the code without margins. The
behaviour in standalone mode may adjusted using a configuration
file standalone.cfg to redefine the standalone environment.

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
%{_texmfdistdir}/tex/latex/standalone/standalone.cfg
%{_texmfdistdir}/tex/latex/standalone/standalone.cls
%{_texmfdistdir}/tex/latex/standalone/standalone.sty
%{_texmfdistdir}/tex/latex/standalone/standalone.tex
%doc %{_texmfdistdir}/doc/latex/standalone/standalone.pdf
#- source
%doc %{_texmfdistdir}/source/latex/standalone/Makefile
%doc %{_texmfdistdir}/source/latex/standalone/README
%doc %{_texmfdistdir}/source/latex/standalone/standalone.dtx
%doc %{_texmfdistdir}/source/latex/standalone/standalone.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
