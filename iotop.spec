%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
Name: iotop
Version: 0.6
Release: 1%{?dist}
Summary: Top like utility for I/O       

Group: Applications/System          
License: GPLv2+
URL: http://guichaz.free.fr/iotop/            
Source0: http://guichaz.free.fr/iotop/files/%{name}-%{version}.tar.bz2 

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
BuildRequires: python-devel
Requires: python
      
%prep
%setup

%build
%{__python} setup.py build

%description
Linux has always been able to show how much I/O was going on
(the bi and bo columns of the vmstat 1 command).
iotop is a Python program with a top like UI used to
show of behalf of which process is the I/O going on.


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root=${RPM_BUILD_ROOT}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING NEWS THANKS
%{_sbindir}/iotop
%{_mandir}/man8/iotop.*
%{python_sitelib}/*

%changelog
* Wed Mar 29 2013 Michal Hlavinka <mhlavink@redhat.com> - 0.6-1
- iotop updated to 0.6

* Tue Feb 05 2013 Michal Hlavinka <mhlavink@redhat.com> - 0.5-1
- iotop updated to 0.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Michal Hlavinka <mhlavink@redhat.com> - 0.4.4-1
- iotop updated to 0.4.4

* Fri Oct 14 2011 Michal Hlavinka <mhlavink@redhat.com> 0.4.3-3
- fix typo in last patch

* Thu Oct 13 2011 Michal Hlavinka <mhlavink@redhat.com> 0.4.3-2
- after CVE-2011-2494 fix, iotop needs root privileges

* Sun Sep 18 2011 Adel Gadllah <adel.gadllah@gmail.com> 0.4.3-1
- New upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jan 12 2010 Adel Gadllah <adel.gadllah@gmail.com> 0.4-1
- New upstream version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.3-1
- New upstream version
- fixes RH #475917

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.2.1-2
- Rebuild for Python 2.6

* Wed Jul 09 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.2.1-1
- Update to 0.2.1

* Mon Jul 07 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.2-2
- New upstream tarball..

* Mon May 26 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.2-1
- Update to new upstream version

* Fri Dec 28 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.1-3
- Fix build issue

* Fri Dec 28 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.1-2
- Fix traceback on xterm-color RH #400071

* Sun Nov 3 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.1-1
- Fix version

* Sun Nov 3 2007 Adel Gadllah <adel.gadllah@gmail.com> 20070930-1
- Initial Build
