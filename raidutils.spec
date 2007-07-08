Summary:	Utilities to manage Adaptec I2O compliant RAID controllers
Summary(pl.UTF-8):	Narzêdzia do zarz±dzania kontrolerami RAID Adaptec I2O
Name:		raidutils
Version:	0.0.6
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://i2o.shadowconnect.com/raidutils/%{name}-%{version}.tar.bz2
Patch0:		%{name}-suse.patch
# Source0-md5:	d32ed6789a11dca51cbc6d4428e26d8b
URL:		http://i2o.shadowconnect.com/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The raidutils program allow the user to manage the Adaptec I2O
compliant RAID controllers. It can, for example, create/delete an RAID
array, add/remove a hot spare drive to/from a RAID array,
activate/silence the alarm or get information about the status of the
RAID array and disks.

%description -l pl.UTF-8
Program raidutils pozwala zarz±dzaæ kontrolerami RAID zgodnymi z
Adaptec I2O. Potrafi na przyk³ad utworzyæ/usun±æ macierz RAID,
dodaæ/usun±æ dysk hot spare do/z macierzy RAID, uaktywniæ/wy³±czyæ
alarm albo uzyskaæ informacje o stanie macierzy RAID i jej dysków.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/libraidutil.{a,la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/raidutil
%attr(755,root,root) %{_bindir}/raideng
%attr(755,root,root) %{_libdir}/libraidutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libraidutil.so.0
