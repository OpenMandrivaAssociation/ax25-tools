%define name	ax25-tools
%define version	0.0.10
%define prerel	rc2
%define rel	1

Name:           %{name}
Version:        %{version}
Release:        %mkrel -c %{prerel} %{rel}
Summary:        Tools used to configure an ax.25 enabled computer
Group:          Applications/Communications
License:        GPLv2+
URL:            http://www.linux-ax25.org/wiki/LinuxAX25
Source0:        http://www.linux-ax25.org/pub/%{name}/%{name}-%{version}-%{prerel}.tar.gz
Patch0:		ax25-tools-0.0.10-rc2-fix_str_fmt.patch
Patch1:		ax25-tools-0.0.10-rc2-fix_linking.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  libax25-devel
BuildRequires:  ncurses-devel
BuildRequires:  libxt-devel
BuildRequires:	fltk-devel

%description
ax25-tools is a collection of tools that are used to configure an ax.25 enabled
computer. They will configure interfaces and assign callsigns to ports as well
as Net/ROM and ROSE configuration.

%prep
%setup -qn %{name}-%{version}-%{prerel}
%patch0 -p1
%patch1 -p1

%build
%configure2_5x --with-x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}%{_docdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README
%doc yamdrv/README.yamdrv user_call/README.user_call tcpip/ttylinkd.README dmascc/README.dmascc
%doc ax25/axgetput/README
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man*/*
