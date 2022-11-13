Name:		texlive-standalone
Version:	64677
Release:	1
Summary:	Compile TeX pictures stand-alone or as part of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/standalone
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/standalone.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/standalone.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/standalone.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/standalone
%doc %{_texmfdistdir}/doc/latex/standalone
#- source
%doc %{_texmfdistdir}/source/latex/standalone

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
