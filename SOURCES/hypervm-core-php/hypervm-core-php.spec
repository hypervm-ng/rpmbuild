%define name 	hypervm-core-php
%define packagename php
%define version 5.4.16
%define release 12%{?dist}
%define brand   lxlabs

%if 0%{?fedora} < 17 && 0%{?rhel} < 7
%global with_zip     0
%global with_libzip  0
%else
%global with_zip     1
%global with_libzip  1
%endif

%global mysql_sock %(mysql_config --socket 2>/dev/null || echo /var/lib/mysql/mysql.sock)

Epoch: 1
Name: %{name}       
Version: %{version}  
Release: %{release}
Summary: HyperVM-NG - Core package for the GUI
Group: HyperVM-NG
# All files licensed under PHP version 3.01, except
# Zend is licensed under Zend
# TSRM is licensed under BSD
License: PHP and Zend and BSD
URL: http://www.hypervm-ng.org

SOURCE0: %{packagename}-%{version}.tar.bz2
SOURCE1: hypervm-core-php.ini

# Build fixes
Patch5: php-5.2.0-includedir.patch
Patch6: php-5.2.4-embed.patch
Patch7: php-5.3.0-recode.patch
Patch8: php-5.4.7-libdb.patch

# Fixes for extension modules
# https://bugs.php.net/63171 no odbc call during timeout
Patch21: php-5.4.7-odbctimer.patch
# Fixed Bug #64949 (Buffer overflow in _pdo_pgsql_error)
Patch22: php-5.4.16-pdopgsql.patch
# Fixed bug #64960 (Segfault in gc_zval_possible_root)
Patch23: php-5.4.16-gc.patch
# Fixed Bug #64915 (error_log ignored when daemonize=0)
Patch24: php-5.4.16-fpm.patch
# https://bugs.php.net/65143 php-cgi man page
# https://bugs.php.net/65142 phar man page
Patch25: php-5.4.16-man.patch
# https://bugs.php.net/66987 fileinfo / bigendian
Patch26: php-5.4.16-bug66987.patch
# https://bugs.php.net/50444 pdo_odbc / x86_64
Patch27: php-5.4.16-bug50444.patch
# https://bugs.php.net/63595 gmp memory allocator
Patch28: php-5.4.16-bug63595.patch
# https://bugs.php.net/62129 session rfc1867
Patch29: php-5.4.16-bug62129.patch
# https://bugs.php.net/66762 mysqli segfault
Patch30: php-5.4.16-bug66762.patch
# https://bugs.php.net/65641 fpm script name
Patch31: php-5.4.6-bug65641.patch
# https://bugs.php.net/71089 duplicate ext
Patch32: php-5.4.16-bug71089.patch
# https://bugs.php.net/66833 default digest algo
Patch33: php-5.4.16-bug66833.patch
# fixed variable corruption
Patch34: php-5.4.16-wddx.patch
# bad logic in sapi header callback routine
Patch35: php-5.4.16-bug66375.patch

# Functional changes
Patch40: php-5.4.0-dlopen.patch
Patch41: php-5.4.0-easter.patch
Patch42: php-5.3.1-systzdata-v10.patch
# See http://bugs.php.net/53436
Patch43: php-5.4.0-phpize.patch
# Use system libzip instead of bundled one
Patch44: php-5.4.15-system-libzip.patch
# Use -lldap_r for OpenLDAP
Patch45: php-5.4.8-ldap_r.patch
# Make php_config.h constant across builds
Patch46: php-5.4.9-fixheader.patch
# drop "Configure command" from phpinfo output
Patch47: php-5.4.9-phpinfo.patch
# Fix php_select on aarch64 (http://bugs.php.net/67406)
Patch48: php-5.4.16-aarch64-select.patch
Patch49: php-5.4.16-curltls.patch
# add clear_env option to FPM config
Patch50: php-5.4.16-fpmclearenv.patch
# fix default_socket_timeout does not work with SSL
Patch51: php-5.4.16-openssl-timeout.patch
# load openssl configuration file
Patch52: php-5.4.16-openssl-config.patch

# Fixes for tests
Patch60: php-5.4.16-pdotests.patch

# Security fixes
Patch100: php-5.4.17-CVE-2013-4013.patch
Patch101: php-5.4.16-CVE-2013-4248.patch
Patch102: php-5.4.16-CVE-2013-6420.patch
Patch104: php-5.4.16-CVE-2014-1943.patch
Patch105: php-5.4.16-CVE-2013-6712.patch
Patch107: php-5.4.16-CVE-2014-2270.patch
Patch108: php-5.4.16-CVE-2013-7345.patch
Patch109: php-5.4.16-CVE-2014-0237.patch
Patch110: php-5.4.16-CVE-2014-0238.patch
Patch111: php-5.4.16-CVE-2014-3479.patch
Patch112: php-5.4.16-CVE-2014-3480.patch
Patch113: php-5.4.16-CVE-2014-4721.patch
Patch114: php-5.4.16-CVE-2014-4049.patch
Patch115: php-5.4.16-CVE-2014-3515.patch
Patch116: php-5.4.16-CVE-2014-0207.patch
Patch117: php-5.4.16-CVE-2014-3487.patch
Patch118: php-5.4.16-CVE-2014-2497.patch
Patch119: php-5.4.16-CVE-2014-3478.patch
Patch120: php-5.4.16-CVE-2014-3538.patch
Patch121: php-5.4.16-CVE-2014-3587.patch
Patch122: php-5.4.16-CVE-2014-5120.patch
Patch123: php-5.4.16-CVE-2014-4698.patch
Patch124: php-5.4.16-CVE-2014-4670.patch
Patch125: php-5.4.16-CVE-2014-3597.patch
Patch126: php-5.4.16-CVE-2014-3668.patch
Patch127: php-5.4.16-CVE-2014-3669.patch
Patch128: php-5.4.16-CVE-2014-3670.patch
Patch129: php-5.4.16-CVE-2014-3710.patch
Patch130: php-5.4.16-CVE-2014-8142.patch
Patch131: php-5.4.16-CVE-2015-0231.patch
Patch132: php-5.4.16-CVE-2015-0232.patch
Patch133: php-5.4.16-CVE-2014-9652.patch
Patch134: php-5.4.16-CVE-2014-9709.patch
Patch135: php-5.4.16-CVE-2015-0273.patch
Patch136: php-5.4.16-CVE-2014-9705.patch
Patch137: php-5.4.16-CVE-2015-2301.patch
Patch138: php-5.4.16-bug69085.patch
Patch139: php-5.4.16-CVE-2015-2787.patch
Patch140: php-5.4.16-CVE-2015-2348.patch
Patch145: php-5.4.16-CVE-2015-4022.patch
Patch146: php-5.4.16-CVE-2015-4021.patch
Patch147: php-5.4.16-CVE-2015-4024.patch
Patch148: php-5.4.16-CVE-2015-4025.patch
Patch149: php-5.4.16-CVE-2015-3330.patch
Patch150: php-5.4.16-bug69353.patch
Patch151: php-5.4.16-CVE-2015-2783.patch
Patch152: php-5.4.16-CVE-2015-3329.patch
Patch153: php-5.4.16-bug68819.patch
Patch154: php-5.4.16-bug69152.patch
Patch155: php-5.4.16-CVE-2016-5385.patch
Patch156: php-5.4.16-CVE-2016-5766.patch
Patch157: php-5.4.16-CVE-2016-5767.patch
Patch158: php-5.4.16-CVE-2016-5768.patch
Patch159: php-5.4.16-CVE-2016-5399.patch
Patch160: php-5.4.16-CVE-2016-10167.patch
Patch161: php-5.4.16-CVE-2016-10168.patch
Patch162: php-5.4.16-CVE-2017-7890.patch
Patch163: php-5.4.16-CVE-2018-5784.patch
Patch164: php-5.4.16-CVE-2019-9024.patch
Patch165: php-5.4.16-CVE-2018-5712.patch
Patch166: php-5.4.16-CVE-2018-10547.patch
Patch167: php-5.4.16-CVE-2019-11043.patch


%if 0%{?fedora} < 18 && 0%{?rhel} < 7
BuildRequires: rpmlib
%endif
BuildRequires: bzip2-devel, curl-devel >= 7.9, gmp-devel
BuildRequires: httpd-devel >= 2.0.46-1, pam-devel
BuildRequires: libstdc++-devel, openssl-devel
BuildRequires: sqlite-devel >= 3.6.0
BuildRequires: zlib-devel, smtpdaemon, libedit-devel
BuildRequires: pcre-devel >= 6.6
BuildRequires: bzip2, perl, libtool >= 1.4.3, gcc-c++
BuildRequires: libtool-ltdl-devel, make
%if %{with_libzip}
BuildRequires: libzip-devel >= 0.10
%endif

# because the hypervm-core-php is a copy of the maintained RHEL PHP version, 
# we need to have below BuildRequires as well:

# for ldap
BuildRequires: cyrus-sasl-devel, openldap-devel, openssl-devel

# for mysql
BuildRequires: mysql-devel >= 4.1.0

# for pgsql
BuildRequires: krb5-devel, openssl-devel, postgresql-devel

# for odbc
BuildRequires: unixODBC-devel

# for soap
BuildRequires: libxml2-devel

# for snmp
BuildRequires: net-snmp-devel
# Workaround, see https://bugzilla.redhat.com/1486733
BuildRequires: net-snmp

# for xml
BuildRequires: libxslt-devel >= 1.0.18-1, libxml2-devel >= 2.4.14-1

# for gd
BuildRequires: libjpeg-devel, libpng-devel, freetype-devel
BuildRequires: libXpm-devel, t1lib-devel

# for dba
%if 0%{?fedora} < 18 && 0%{?rhel} < 7
BuildRequires: libdb4-devel, tokyocabinet-devel
%else
BuildRequires: libdb-devel, tokyocabinet-devel
%endif

# for pspell
BuildRequires: aspell-devel >= 0.50.0

# for recode
BuildRequires: recode-devel

# for intl
BuildRequires: libicu-devel >= 3.6

# for enchant
BuildRequires: enchant-devel >= 1.2.4


Obsoletes: php-dbg, php3, phpfi, stronghold-php, lxphp <= 5.2.1

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

%patch5 -p1 -b .includedir
%patch6 -p1 -b .embed
%patch7 -p1 -b .recode
%patch8 -p1 -b .libdb

%patch21 -p1 -b .odbctimer
%patch22 -p1 -b .pdopgsql
%patch23 -p1 -b .gc
%patch24 -p1 -b .fpm
%patch25 -p1 -b .manpages
%patch26 -p1 -b .bug66987
%patch27 -p1 -b .bug50444
%patch28 -p1 -b .bug63595
%patch29 -p1 -b .bug62129
%patch30 -p1 -b .bug66762
%patch31 -p1 -b .bug65641
%patch32 -p1 -b .bug71089
%patch33 -p1 -b .bug66833
%patch34 -p1 -b .fix
%patch35 -p1 -b .bug66375

%patch40 -p1 -b .dlopen
%patch41 -p1 -b .easter
%patch42 -p1 -b .systzdata
%patch43 -p1 -b .headers
%if %{with_libzip}
%patch44 -p1 -b .systzip
%endif
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%patch45 -p1 -b .ldap_r
%endif
%patch46 -p1 -b .fixheader
%patch47 -p1 -b .phpinfo
%patch48 -p1 -b .aarch64select
%patch49 -p1 -b .curltls
%patch50 -p1 -b .clearenv
%patch51 -p1 -b .ssl_timeout
%patch52 -p1 -b .config

%patch60 -p1 -b .pdotests

%patch100 -p1 -b .cve4113
%patch101 -p1 -b .cve4248
%patch102 -p1 -b .cve6420
%patch104 -p1 -b .cve1943
%patch105 -p1 -b .cve6712
%patch107 -p1 -b .cve2270
%patch108 -p1 -b .cve7345
%patch109 -p1 -b .cve0237
%patch110 -p1 -b .cve0238
%patch111 -p1 -b .cve3479
%patch112 -p1 -b .cve3480
%patch113 -p1 -b .cve4721
%patch114 -p1 -b .cve4049
%patch115 -p1 -b .cve3515
%patch116 -p1 -b .cve0207
%patch117 -p1 -b .cve3487
%patch118 -p1 -b .cve2497
%patch119 -p1 -b .cve3478
%patch120 -p1 -b .cve3538
%patch121 -p1 -b .cve3587
%patch122 -p1 -b .cve5120
%patch123 -p1 -b .cve4698
%patch124 -p1 -b .cve4670
%patch125 -p1 -b .cve3597
%patch126 -p1 -b .cve3668
%patch127 -p1 -b .cve3669
%patch128 -p1 -b .cve3670
%patch129 -p1 -b .cve3710
%patch130 -p1 -b .cve8142
%patch131 -p1 -b .cve0231
%patch132 -p1 -b .cve0232
%patch133 -p1 -b .cve9652
%patch134 -p1 -b .cve9709
%patch135 -p1 -b .cve0273
%patch136 -p1 -b .cve9705
%patch137 -p1 -b .cve2301
%patch138 -p1 -b .bug68095
%patch139 -p1 -b .cve2787
%patch140 -p1 -b .cve2348
%patch145 -p1 -b .cve4022
%patch146 -p1 -b .cve4021
%patch147 -p1 -b .cve4024
%patch148 -p1 -b .cve4025
%patch149 -p1 -b .cve3330
%patch150 -p1 -b .bug69353
%patch151 -p1 -b .cve2783
%patch152 -p1 -b .cve3329
%patch153 -p1 -b .bug68819
%patch154 -p1 -b .bug69152
%patch155 -p1 -b .cve5385
%patch156 -p1 -b .cve5766
%patch157 -p1 -b .cve5767
%patch158 -p1 -b .cve5768
%patch159 -p1 -b .cve5399
%patch160 -p1 -b .cve10167
%patch161 -p1 -b .cve10168
%patch162 -p1 -b .cve7890
%patch163 -p1 -b .cve7584
%patch164 -p1 -b .cve9024
%patch165 -p1 -b .cve5712
%patch166 -p1 -b .cve10547
%patch167 -p1 -b .cve11043

# create directory for hypervm-core-php build
mkdir core-php

%build
# aclocal workaround - to be improved
cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >>aclocal.m4

# Force use of system libtool:
libtoolize --force --copy
cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >build/libtool.m4

# Regenerate configure scripts (patches change config.m4's)
touch configure.in
./buildconf --force

CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-pointer-sign"
export CFLAGS

# Shell function to configure and build a PHP tree.
build() {
# Old/recent bison version seems to produce a broken parser;
# upstream uses GNU Bison 2.3. Workaround:
mkdir Zend && cp ../Zend/zend_{language,ini}_{parser,scanner}.[ch] Zend
ln -sf ../configure
%configure \
        --cache-file=../config.cache \
        --with-libdir=%{_lib} \
        --disable-debug \
        --with-pic \
        --disable-rpath \
        --without-pear \
        --with-bz2 \
        --with-exec-dir=%{_bindir} \
        --with-freetype-dir=%{_prefix} \
        --with-png-dir=%{_prefix} \
        --with-xpm-dir=%{_prefix} \
        --enable-gd-native-ttf \
        --with-t1lib=%{_prefix} \
        --without-gdbm \
        --with-gettext \
        --with-gmp \
        --with-iconv \
        --with-jpeg-dir=%{_prefix} \
        --with-openssl \
        --with-pcre-regex=%{_prefix} \
        --with-zlib \
        --with-layout=GNU \
        --enable-exif \
        --enable-ftp \
        --enable-sockets \
        --with-kerberos \
        --enable-shmop \
        --enable-calendar \
        --with-libxml-dir=%{_prefix} \
        --enable-xml \
        --with-system-tzdata \
        --with-mhash \
        $* 
if test $? != 0; then 
  tail -500 config.log
  : configure failed
  exit 1
fi

make %{?_smp_mflags}
}

# Build /usr/local/lxlabs/ext/php with the CGI SAPI, and all the shared extensions
pushd core-php

build --prefix=/usr/local/%{brand}/ext/php \
      --with-config-file-path=/usr/local/%{brand}/ext/php/etc \
      --enable-pcntl \
      --enable-mbstring=shared \
      --enable-mbregex \
      --with-gd=shared \
      --enable-bcmath=shared \
      --enable-dba=shared --with-db4=%{_prefix} \
                          --with-tcadb=%{_prefix} \
      --with-xmlrpc=shared \
      --with-ldap=shared --with-ldap-sasl \
      --enable-mysqlnd=shared \
      --with-mysql=shared,mysqlnd \
      --with-mysqli=shared,mysqlnd \
      --with-mysql-sock=%{mysql_sock} \
      --enable-dom=shared \
      --with-pgsql=shared \
      --enable-wddx=shared \
      --with-snmp=shared,%{_prefix} \
      --enable-soap=shared \
      --with-xsl=shared,%{_prefix} \
      --enable-xmlreader=shared --enable-xmlwriter=shared \
      --with-curl=shared,%{_prefix} \
      --enable-pdo=shared \
      --with-pdo-odbc=shared,unixODBC,%{_prefix} \
      --with-pdo-mysql=shared,mysqlnd \
      --with-pdo-pgsql=shared,%{_prefix} \
      --with-pdo-sqlite=shared,%{_prefix} \
      --with-sqlite3=shared,%{_prefix} \
      --enable-json=shared \
%if %{with_zip}
      --enable-zip=shared \
%endif
%if %{with_libzip}
      --with-libzip \
%endif
      --without-readline \
      --with-libedit \
      --with-pspell=shared \
      --enable-phar=shared \
      --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
      --enable-posix=shared \
      --with-unixODBC=shared,%{_prefix} \
      --enable-fileinfo=shared \
      --enable-intl=shared \
      --with-icu-dir=%{_prefix} \
      --with-enchant=shared,%{_prefix} \
      --with-recode=shared,%{_prefix}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

install -D -m 755 core-php/modules/bcmath.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/bcmath.so
install -D -m 755 core-php/modules/curl.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/curl.so
install -D -m 755 core-php/modules/dba.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/dba.so
install -D -m 755 core-php/modules/dom.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/dom.so
install -D -m 755 core-php/modules/enchant.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/enchant.so
install -D -m 755 core-php/modules/fileinfo.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/fileinfo.so
install -D -m 755 core-php/modules/gd.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/gd.so
install -D -m 755 core-php/modules/intl.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/intl.so
install -D -m 755 core-php/modules/json.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/json.so
install -D -m 755 core-php/modules/ldap.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/ldap.so
install -D -m 755 core-php/modules/mbstring.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/mbstring.so
install -D -m 755 core-php/modules/mysql.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/mysql.so
install -D -m 755 core-php/modules/mysqli.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/mysqli.so
install -D -m 755 core-php/modules/mysqlnd.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/mysqlnd.so
install -D -m 755 core-php/modules/odbc.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/odbc.so
install -D -m 755 core-php/modules/pdo.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/pdo.so
install -D -m 755 core-php/modules/pdo_mysql.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/pdo_mysql.so
install -D -m 755 core-php/modules/pdo_odbc.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/pdo_odbc.so
install -D -m 755 core-php/modules/pdo_pgsql.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/pdo_pgsql.so
install -D -m 755 core-php/modules/pdo_sqlite.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/pdo_sqlite.so
install -D -m 755 core-php/modules/pgsql.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/pgsql.so
install -D -m 755 core-php/modules/phar.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/phar.so
install -D -m 755 core-php/modules/posix.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/posix.so
install -D -m 755 core-php/modules/pspell.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/pspell.so
install -D -m 755 core-php/modules/recode.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/recode.so
install -D -m 755 core-php/modules/snmp.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/snmp.so
install -D -m 755 core-php/modules/soap.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/soap.so
install -D -m 755 core-php/modules/sqlite3.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/sqlite3.so
install -D -m 755 core-php/modules/sysvmsg.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/sysvmsg.so
install -D -m 755 core-php/modules/sysvsem.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/sysvsem.so
install -D -m 755 core-php/modules/sysvshm.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/sysvshm.so
install -D -m 755 core-php/modules/wddx.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/wddx.so
install -D -m 755 core-php/modules/xmlreader.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/xmlreader.so
install -D -m 755 core-php/modules/xmlrpc.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/xmlrpc.so
install -D -m 755 core-php/modules/xmlwriter.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/xmlwriter.so
install -D -m 755 core-php/modules/xsl.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/xsl.so
install -D -m 755 core-php/modules/zip.so $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/lib/zip.so


# Doc
install -D -m 755 sapi/cli/php.1.in.manpages $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/man/man1/php.1

# Binary
# install -D -m 755 msapi/cli/php $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/php
install -D -m 755 core-php/sapi/cli/php $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/php
install -D -m 755 core-php/sapi/cli/php $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/bin/php
install -D -m 755 core-php/sapi/cgi/php-cgi $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/bin/php_cgi

# php.ini
install -D -m 755 %{SOURCE1} $RPM_BUILD_ROOT/usr/local/%{brand}/ext/php/etc/php.ini

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

# Modules
/usr/local/%{brand}/ext/php/lib/

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
* Sat Mar 14 2021 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.4.16-12
- Bump version

* Sat Mar 13 2021 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.4.16-11
- Bump version

* Sat Mar 13 2021 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.4.16-10
- Bump version

* Wed Mar 10 2021 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.4.16-9
- Added BuildRequires required by docker rpm builder

* Tue Mar 2 2021 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.4.16-8
- Set memory_limit = 32M

* Tue Mar 2 2021 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.4.16-7
- Enable mysqli.reconnect

* Mon Mar 1 2021 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.4.16-6
- Set short_open_tag back to On

* Mon Mar 1 2021 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.4.16-5
- Added missing BuildRequires
- Adjusted php.ini

* Mon Mar 1 2021 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.4.16-4
- Missing mysql_sock definition

* Mon Mar 1 2021 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.4.16-3
- Repaired %pre script

* Mon Mar 1 2021 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.4.16-2
- Added Epoch to let yum downgrade from 5.5.x to 5.4.16

* Mon Mar 1 2021 Krzysztof Taraszka <krzysztof.taraszka@hypervm-ng.org> 5.4.16-1
- Based on RedHat php-5.4.16-48

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
