%define oname   ReviewBoard

Name:           reviewboard
Version:        1.5
Release:        %mkrel 1
Summary:        Web-based code review tool
Group:          Networking/WWW
License:        MIT
URL:            http://www.review-board.org
Source0:        http://downloads.review-board.org/releases/%{name}/1.5/%{oname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-django >= 1.1.1
Requires:       python-djblets >= 0.6.4
Requires:       python-imaging
Requires:       apache 
Requires:       python-sqlite
Requires:       patchutils
Requires:       python-svn
Requires:       python-flup
Requires:       python-nose
Requires:       python-pytz
Requires:       python-pygments >= 1.1.1
Requires:       python-django-evolution
Requires:       python-recaptcha-client
Requires:       python-paramiko
Requires:       python-memcached
Requires:       python-dateutil

Patch1000: FED01-Disable-ez_setup-when-installing-by-RPM.patch

%description
Review Board is a powerful web-based code review tool that offers
developers an easy way to handle code reviews. It scales well from small
projects to large companies and offers a variety of tools to take much
of the stress and time out of the code review process.

%files
# The rb-site executable has a PyGTK GUI, so would normally
# require us to ship a .desktop file.  However it can only be run when supplied
# a directory as a command-line argument, hence it wouldn't be meaningful to
# create a .desktop file for it.
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL NEWS README
%{_bindir}/rb-site
%{python_sitelib}/reviewboard/
%{python_sitelib}/ReviewBoard*.egg-info/
%{python_sitelib}/webtests/*.py*

#--------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
%patch1000 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

# --skip-build causes bad stuff in siteconfig.py as of 0.8.4
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

# manage.py has a shebang and is meaningful to run; make it executable:
chmod +x $RPM_BUILD_ROOT/%{python_sitelib}/reviewboard/manage.py

%clean
rm -rf $RPM_BUILD_ROOT



%changelog
* Sun Nov 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.5-1mdv2011.0
+ Revision: 594407
- import reviewboard

