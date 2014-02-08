# revision 26511
# category Package
# catalog-ctan /macros/latex/contrib/standalone
# catalog-date 2012-05-20 20:33:03 +0200
# catalog-license lppl1.3
# catalog-version 1.1a
Name:		texlive-standalone
Version:	1.1a
Release:	2
Summary:	Compile TeX pictures stand-alone or as part of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/standalone
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/standalone.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/standalone.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/standalone.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/standalone/standalone.cfg
%{_texmfdistdir}/tex/latex/standalone/standalone.cls
%{_texmfdistdir}/tex/latex/standalone/standalone.sty
%{_texmfdistdir}/tex/plain/standalone/standalone.tex
%doc %{_texmfdistdir}/doc/latex/standalone/README
%doc %{_texmfdistdir}/doc/latex/standalone/standalone.pdf
#- source
%doc %{_texmfdistdir}/source/latex/standalone/standalone.dtx
%doc %{_texmfdistdir}/source/latex/standalone/standalone.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-1
+ Revision: 812881
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 805078
- Update to latest release.

* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-1
+ Revision: 790738
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 756167
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 745308
- texlive-standalone

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4a-1
+ Revision: 719577
- texlive-standalone
- texlive-standalone
- texlive-standalone
- texlive-standalone

