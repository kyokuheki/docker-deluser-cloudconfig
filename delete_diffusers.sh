#!/usr/bin/env bash

function yesno () {
  echo "Are you sure you want to $1?"
  select yn in "Yes" "No"
  do
    case $yn in
      Yes ) return 0;;
      No ) return 1;;
    esac
  done
}

docker build -t okd/getusers update_users
j="`docker run -i -v/var/lib/coreos-install/user_data:/config.yml:ro  -v/etc/passwd:/passwd:ro okd/getusers`"
echo $j | jq
invalid=(`echo $j | jq -r .invalid[]`)

for u in ${invalid[@]}
do
  if ! yesno "delete user $u"
  then
    #echo The user $u was not deleted.
    continue
  fi
  sudo userdel -r $u
  echo The user $u has been deleted.
done
