# docker-delete-diffusers
delete users which is absent from cloud-config.yml

## build

```shell
docker build -t kyokuheki/diffusers
```

## run

```shell
docker run -i -v/var/lib/coreos-install/user_data:/config.yml:ro -v/etc/passwd:/passwd:ro kyokuheki/diffusers
```

## run on CoreOS

```shell
j="`docker run -i -v/var/lib/coreos-install/user_data:/config.yml:ro -v/etc/passwd:/passwd:ro kyokuheki/diffusers`"
echo $j | jq
invalid=(`echo $j | jq -r .invalid[]`)

for u in ${invalid[@]}
do
  sudo userdel -r $u
done
```
