# docker-delete-diffusers
get diff users between `cloud-config.yml` and `/etc/passwd`

## build

```shell
docker build -t kyokuheki/diffusers
```

## run

```shell
docker run -i -v/var/lib/coreos-install/user_data:/config.yml:ro -v/etc/passwd:/passwd:ro kyokuheki/diffusers
```

## delete users that are present in /etc/passwd but don't exist in cloud-config.yml

```shell
j="`docker run -i -v/var/lib/coreos-install/user_data:/config.yml:ro -v/etc/passwd:/passwd:ro kyokuheki/diffusers`"
echo $j | jq
invalid=(`echo $j | jq -r .invalid[]`)

for u in ${invalid[@]}
do
  sudo userdel -r $u
done
```
