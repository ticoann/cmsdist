### RPM external oracle 10.2.0.1
## INITENV SET ORACLE_HOME %i

Source0: http://oraclelon1.oracle.com/otn/linux/instantclient/10201/instantclient-basic-linux32-10.2.0.1-20050713.zip
Source1: http://oraclelon1.oracle.com/otn/linux/instantclient/10201/instantclient-sdk-linux32-10.2.0.1-20050713.zip
Source2: http://oraclelon1.oracle.com/otn/linux/instantclient/10201/instantclient-sqlplus-linux32-10.2.0.1-20050713.zip

Source3: http://oraclelon1.oracle.com/otn/linux/instantclient/10201/instantclient-basic-linux-x86-64-10.2.0.2-20060228.zip
Source4: http://oraclelon1.oracle.com/otn/linux/instantclient/10201/instantclient-sdk-linux-x86-64-10.2.0.2-20060228.zip
Source5: http://oraclelon1.oracle.com/otn/linux/instantclient/10201/instantclient-sqlplus-linux-x86-64-10.2.0.2-20060228.zip

## INITENV +PATH SQLPATH %i/bin
%prep
rm -rf instantclient_*
case %cmsos in
  slc*_ia32 )
    yes | unzip %_sourcedir/*-basic-*linux32*.zip
    yes | unzip %_sourcedir/*-sdk-*linux32*.zip
    yes | unzip %_sourcedir/*-sqlplus-*linux32*.zip
    ;;
  slc*_amd64 )
    yes | unzip %_sourcedir/*-basic-*linux-x86-64*.zip
    yes | unzip %_sourcedir/*-sdk-*linux-x86-64*.zip
    yes | unzip %_sourcedir/*-sqlplus-*linux-x86-64*.zip
    ;;
esac

%build
%install
mkdir -p %i/bin %i/etc %i/lib %i/admin %i/java %i/demo %i/include
cp -p instantclient*/lib* %i/lib
cp -p instantclient*/sqlplus %i/bin
cp -p instantclient*/glogin.sql %i/bin
cp -p instantclient*/*.jar %i/java
cp -p instantclient*/sdk/demo/* %i/demo
cp -p instantclient*/sdk/include/* %i/include
(cd %i/lib && ln -s libclntsh.* $(echo libclntsh.* | sed 's/[0-9.]*$//'))
