Summary:	A userspace unionfs implementation
Summary(pl.UTF-8):	Implementacja unionfs w przestrzeni użytkownika
Name:		unionfs-fuse
Version:	0.26
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://podgorny.cz/unionfs-fuse/releases/%{name}-%{version}.tar.xz
# Source0-md5:	689c636484756f6f7a728ef354cbeac2
URL:		http://podgorny.cz/moin/UnionFsFuse
BuildRequires:	cmake >= 2.0
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unionfs-fuse overlays several directory into one single mount point.

It first tries to access the file on the top branch and if the file
does not exist there, it continues on lower level branches. If the
user tries to modify a file on a lower level read-only branch the file
is copied to to a higher level read-write branch if the copy-on-write
(cow) mode was enabled.

%description -l pl.UTF-8
unionfs-fuse nakłada kilka katalogów w pojedynczy punkt montowania.

Najpierw próbuje dostępu do pliku na górnej gałęzi, a jeśli tam nie
istnieje - kontynuuje na niższych gałęziach. Jeżeli użytkownik próbuje
zmodyfikować plik na niższej gałęzi tylko do odczytu, plik jest
kopiowany na wyższą gałąź do odczytu i zapisu - o ile jest włączony
tryb COW (copy on write - kopiowania przy zapisie).

%prep
%setup -q

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}
%{__mv} $RPM_BUILD_ROOT%{_sbindir}/{unionfs,unionfs-fuse}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS LICENSE NEWS
%attr(755,root,root) %{_sbindir}/unionfs-fuse
%{_mandir}/man8/unionfs-fuse.8*
