%define name 	hypervm-core-php
%define packagename php
%define version 5.5.38
%define release 1%{?dist}
%define brand   lxlabs

Name: %{name}       
Version: %{version}  
Release: %{release}
Summary: HyperVM-NG - Core package for the GUI
Group: HyperVM-NG
License: PHP License   
URL: http://www.hypervm-ng.org

SOURCE0: %{packagename}-%{version}.tar.bz2
SOURCE1: hypervm-core-php.ini

%if 0%{?fedora} < 18 && 0%{?rhel} < 7
BuildRequires: rpmlib
%endif
BuildRequires: bzip2-devel, curl-devel >= 7.9, db4-devel, expat-devel
BuildRequires: libcurl-devel
BuildRequires: gmp-devel, aspell-devel >= 0.50.0
BuildRequires: httpd-devel >= 2.2.15, libjpeg-devel, libpng-devel, pam-devel
BuildRequires: libstdc++-devel, openssl-devel, sqlite-devel >= 3.0.0
BuildRequires: zlib-devel, pcre-devel >= 6.6, smtpdaemon, readline-devel
BuildRequires: bzip2, perl, libtool >= 1.4.3, gcc-c++
BuildRequires: libxml2-devel, openssl-devel, libcurl-devel, gdbm-devel
BuildRequires: libjpeg-turbo-devel, gmp-devel, libc-client-devel
BuildRequires: libmcrypt-devel, mhash-devel, mysql-devel, postgresql-devel
%if 0%{?fedora} < 18 && 0%{?rhel} < 7
BuildRequires: libdb4-devel
%else
BuildRequires: libdb-devel
%endif
BuildRequires: libpng-devel

Obsoletes: php-dbg, php3, phpfi, stronghold-php, lxphp <= 5.2.1
Requires: libmhash

BuildRoot: %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
PHP is a server-side scripting language designed for web development
but also used as a general-purpose programming language.

%pre
echo "Info: Starting HyperVM-NG checks..."
    if [ -f /script/version ]; then
        echo "Info: Script dir found."
        if [ -d /usr/local/%{brand}/hypervm ]; then
                echo "Info: HyperVM-NG found, checking for the version."
                versioncheck=`/script/version`
                echo "Info: Found HyperVM version: $versioncheck"
                        if [ $versioncheck == "2.0.7993" ]; then
                                echo "Error: This package only works with HyperVM 2.1.0+"
                                exit 1
                        fi
                        if [ $versioncheck == "2.0.7994" ]; then
                                echo "Error: This package only works with HyperVM-NG 2.2.0+"
                                exit 1
                        fi
        fi
    else
        echo "Info: First time installation of this package."
    fi


%prep

%setup -q -n %{packagename}-%{version}

%build

./configure \
	--prefix=/usr/local/%{brand}/ext/php \
	--with-config-file-path=/usr/local/%{brand}/ext/php/etc \
	--with-libdir=%{_lib} \
	--with-jpeg-dir=%{_prefix} \
	--with-gd=shared \
	--with-imap=shared --with-imap-ssl=shared \
	--with-kerberos \
	--with-gdbm \
	--with-zlib \
	--with-gmp=shared \
	--with-mysqli=shared,/usr/bin/mysql_config \
	--with-mysql=shared,/usr \
	--with-iconv=shared \
	--with-curl=/usr \
	--with-kerberos \
	--with-mhash \
	--with-mcrypt \
	--with-layout=GNU \
	--with-pcre-regex \
	--with-dom-exslt=/usr \
	--with-dom-xslt=/usr \
	--with-dom=shared,/usr \
	--with-expat-dir=/usr \
	--with-regex=system \
	--with-openssl \
	--with-pdo-sqlite \
	--with-pdo \
	--with-sqlite \
	--with-gettext \
	--with-db4=shared,/usr \
	--with-pgsql=shared,/usr \
	--without-oci8 \
	--disable-rpath \
	--disable-debug \
	--enable-force-cgi-redirect \
	--enable-fastcgi \
	--enable-mbstring=shared --enable-mbstr-enc-trans \
	--enable-pic \
	--enable-inline-optimization \
	--enable-posix \
	--enable-simplexml \
	--enable-track-vars \
        --enable-discard-path \
	--enable-sysvshm \
	--enable-soap=/usr \
	--enable-sysvsem \
	--enable-sockets \
	--enable-safe-mode \
	--enable-magic-quotes \
	--enable-ftp \
	--enable-exif \
	--enable-bcmath \
	--enable-trans-sid \
	--enable-pcntl \
	--enable-mbregex=shared \
	--enable-dio \
	--enable-shmop \
	--enable-bcmath \
	--enable-memory-limit

make %{_smp_mflags}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

install -D -m 755 modules/gd.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/gd.so
install -D -m 755 modules/imap.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/imap.so
install -D -m 755 modules/mbstring.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/mbstring.so
install -D -m 755 modules/gmp.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/gmp.so
install -D -m 755 modules/iconv.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/iconv.so
install -D -m 755 modules/mysqli.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/mysqli.so
install -D -m 755 modules/pgsql.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/pgsql.so
install -D -m 755 modules/mysql.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/mysql.so

# Doc
install -D -m 755 sapi/cli/php.1 $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/man/man1/php.1

# Binary
install -D -m 755 sapi/cli/php $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/php
install -D -m 755 sapi/cli/php $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/bin/php
install -D -m 755 sapi/cgi/php-cgi $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/bin/php_cgi

# php.ini
install -D -m 755 %{SOURCE1} $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/etc/php.ini

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

# Modules
/usr/local/%{brand}/ext/php/lib/
/usr/local/%{brand}/ext/php/lib/gd.so
/usr/local/%{brand}/ext/php/lib/imap.so
/usr/local/%{brand}/ext/php/lib/mbstring.so
/usr/local/%{brand}/ext/php/lib/mysqli.so
/usr/local/%{brand}/ext/php/lib/iconv.so
/usr/local/%{brand}/ext/php/lib/gmp.so
/usr/local/%{brand}/ext/php/lib/pgsql.so
/usr/local/%{brand}/ext/php/lib/mysql.so

# Doc
/usr/local/lxlabs/ext/php/man/
/usr/local/lxlabs/ext/php/man/man1/
/usr/local/lxlabs/ext/php/man/man1/php.1
%config /usr/local/lxlabs/ext/php/man/man1/php.1

# Binary
/usr/local/lxlabs/ext/php/php
/usr/local/lxlabs/ext/php/bin/
/usr/local/lxlabs/ext/php/bin/php
/usr/local/lxlabs/ext/php/bin/php_cgi

# Conf
/usr/local/lxlabs/ext/php/etc
%config /usr/local/lxlabs/ext/php/etc/php.ini

%defattr(-, root, root)
%doc CODING_STANDARDS CREDITS INSTALL LICENSE NEWS
%doc Zend/ZEND_* 

%defattr(-, root, root)
%doc

%changelog
* Sun Oct 16 2016 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.5.38-1
- Upstream 5.5.38
- Removed LxCenter references
- RHEL7 ready

* Thu Apr 2 2015 Danny Terweij <d.terweij@lxcenter.org> 5.5.23-1
- Upstream 5.5.23

* Fri Jul 25 2014 Danny Terweij <d.terweij@lxcenter.org> 5.5.15-1
- Upstream 5.5.15

* Sun Feb 16 2014 Danny Terweij <d.terweij@lxcenter.org> 5.5.9-1
- Upstream 5.5.9

* Fri Jan 10 2014 Danny Terweij <d.terweij@lxcenter.org> 5.5.8-1
- Upstream 5.5.8

* Tue Dec 24 2013 Danny Terweij <d.terweij@lxcenter.org> 5.5.7-1
- Upstream 5.5.7

* Mon Sep 30 2013 Danny Terweij <d.terweij@lxcenter.org> 5.5.4-2
- Make mysql module shared object
- Renamed package to the future rpm standard
- Changed lxphp.ini to hypervm-core-php.ini

* Wed Sep 18 2013 Danny Terweij <d.terweij@lxcenter.org> 5.5.3-4
- Add mysql support so we have both mysqli and mysql

* Mon Sep 16 2013 Danny Terweij <d.terweij@lxcenter.org> 5.5.3-3
- Add mysqli support for mysql connections
- Upgrade to PHP 5.5.3
- Use lxphp.ini
- Remove mysql support deprecated (test)
- Big PHP version jump

* Fri Feb 11 2011 Danny Terweij <d.terweij@lxcenter.org> 5.2.17-0.lxcenter.4
- Obsolete lxphp-5.2.1-400 i386 package

* Fri Feb 11 2011 Danny Terweij <d.terweij@lxcenter.org> 5.2.17-0.lxcenter.3
- Replace php.ini
- Replace php.1

* Fri Feb 11 2011 Danny Terweij <d.terweij@lxcenter.org> 5.2.17-0.lxcenter.2
- Fix php.ini
- Upgrade to PHP 5.2.17

* Tue Jan 04 2011 Danny Terweij <d.terweij@lxcenter.org> 5.2.16-0.lxcenter.1
- Repackaged at build system
- Upgrade to PHP 5.2.16

* Thu Nov 25 2010 Angel Guzman <angel.guzman@lxcenter.org> 5.2.14-0lxcenter3
- Upgrade to PHP 5.2.14 

