# docker-delete-diffusers
get diff users between `cloud-config.yml` and `/etc/passwd`

## build

```shell
docker build -t kyokuheki/diffusers
```

## run

```shell
source /etc/os-release
docker run -i -v/var/lib/${ID}-install/user_data:/config.yml:ro -v/etc/passwd:/passwd:ro kyokuheki/diffusers
```

## delete users that are present in /etc/passwd but don't exist in cloud-config.yml

```shell
source /etc/os-release
j="`docker run -i -v/var/lib/${ID}-install/user_data:/config.yml:ro -v/etc/passwd:/passwd:ro kyokuheki/diffusers`"
echo $j | jq
invalid=(`echo $j | jq -r .invalid[]`)

for u in ${invalid[@]}
do
  sudo userdel -r $u
done
```

or

```shell
bash <(curl -fsSL https://raw.githubusercontent.com/kyokuheki/docker-diffusers/master/delete_diffusers.sh)
```

## get user list from passwd

```shell
sudo cat /etc/passwd | docker run -i --entrypoint=python kyokuheki/diffusers /getusers_passwd.py -
```


## get user list from cloud-config.yml

```shell
source /etc/os-release
sudo cat /var/lib/${ID}-install/user_data | docker run -i --entrypoint=python kyokuheki/diffusers /getusers_cloudconfig.py -
```
