%define		_splash		gears_white

Summary:	KDE splash screens
Summary(pl):	Ekrany startowe KDE
Name:		kde-splash-%{_splash}
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Amusements
# http://www.kde-look.org/content/download.php?content=33071&id=1
Source0:	http://wotan.wo.funpic.de/files/%{_splash}_ksplash-oil.tar.bz2
# Source0-md5:	bc4a3300fdaa8c37db781620e73c3edd
# http://www.kde-look.org/content/download.php?content=33071&id=2
Source1:	http://wotan.wo.funpic.de/files/%{_splash}_ksplash-alu.tar.bz2
# Source1-md5:	610234c49a7b32b1a31310a01add1070
# http://www.kde-look.org/content/download.php?content=33071&id=3
Source2:	http://wotan.wo.funpic.de/files/%{_splash}_ksplash-blue.tar.bz2
# Source2-md5:	06ee446cd4ec4c722e0e0249190c85e1
# http://www.kde-look.org/content/download.php?content=33071&id=4
Source3:	http://wotan.wo.funpic.de/files/%{_splash}_ksplash-green.tar.bz2
# Source3-md5:	1d1b2614f054ab137d5964bd4aa126cb
# http://www.kde-look.org/content/download.php?content=33071&id=5
Source4:	http://wotan.wo.funpic.de/files/%{_splash}_ksplash-rusty.tar.bz2
# Source4-md5:	814f6a2d13591412bfc5b21b167898a8
# http://www.kde-look.org/content/download.php?content=33071&id=6
Source5:	http://wotan.wo.funpic.de/files/%{_splash}_ksplash-metal.tar.bz2
# Source5-md5:	390b3c1355f710d7f7d62ca0ab414663
URL:		http://www.kde-look.org/content/show.php?content=33071
Requires:	kdebase-desktop >= 9:3.2.0
Provides:	kde-splash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"White background" edition of "Gears" splash screen collection.
Contains six different versions.

%description -l pl
Kolekcja ekranów startowych "Gears", edycja z bia³ym t³em. Zawiera
sze¶æ ró¿nych wersji.

%prep
%setup -q -c %{_splash} -n %{_splash} -a1 -a2 -a3 -a4 -a5

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes
mv * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/*
