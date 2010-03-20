Summary:	A userspace unionfs implementation
Name:		unionfs-fuse
Version:	0.23
Release:	1
License:	BSD
Group:		Applications
Source0:	http://podgorny.cz/unionfs-fuse/releases/%{name}-%{version}.tar.bz2
URL:		http://podgorny.cz/moin/UnionFsFuse
BuildRequires:	libfuse-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unionfs−fuse overlays several directory into one single mount point.

It first tries to access the file on the top branch and if the file
does not exist there, it continues on lower level branches. If the
user tries to modify a file on a lower level read−only branch the file
is copied to to a higher level read−write branch if the copy−on−write
(cow) mode was enabled.

%prep
%setup -q

%build
%{__make} CFLAGS="-Wall %{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install src/unionfs $RPM_BUILD_ROOT%{_sbindir}/%{name}
install man/unionfs-fuse.8 $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS NEWS
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
