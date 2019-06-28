#!/usr/bin/env bash

j="`docker run -i -v/var/lib/coreos-install/user_data:/config.yml:ro  -v/etc/passwd:/passwd:ro kyokuheki/diffusers`"
echo "JSON: $j"
#echo "$j" | jq
#invalid=(`echo "$j" | jq -r '.invalid[]'`)
jq -rS '.' <<<"$j" | cat
invalid=(`jq -r '.invalid[]' <<<"$j"`)

for u in ${invalid[@]}
do
  if [[ `id -u $u` -lt 1000 ]]
  then
    echo user $u was skipped.
    continue
  fi
  sudo userdel -r $u
  echo user $u has been deleted.
done
