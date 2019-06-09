#!/usr/bin/env bash

j="`docker run -i -v/var/lib/coreos-install/user_data:/config.yml:ro  -v/etc/passwd:/passwd:ro kyokuheki/diffusers`"
echo $j | jq
invalid=(`echo $j | jq -r .invalid[]`)

for u in ${invalid[@]}
do
  sudo userdel -r $u
  echo The user $u has been deleted.
done
