### RPM external tauolapp-toolfile 1.0
Requires: tauolapp
%prep

%build

%install

mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/tauolapp.xml
<tool name="tauolapp" version="@TOOL_VERSION@">
  <lib name="TauolaCxxInterface"/>
  <lib name="TauolaFortran"/>
  <client>
    <environment name="TAUOLAPP_BASE" default="@TOOL_ROOT@"/>
    <environment name="LIBDIR" default="$TAUOLAPP_BASE/lib"/>
    <environment name="INCLUDE" default="$TAUOLAPP_BASE/include"/>
  </client>
  <use name="hepmc"/>
  <use name="f77compiler"/>
</tool>
EOF_TOOLFILE

## IMPORT scram-tools-post


