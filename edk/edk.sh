#!/bin/bash

#--*--*--*--Easy-Docker--*--*--*--
contid=$1
sureop=$2

if [ "$contid" == "-h" ]; then
	echo 'edk.sh [-contid] -op'
	echo '-h            :Help'
	echo '-contid -s    :Only to stop and delete contid-docker'
	echo '-contid -a    :Stop and delete all dockers that use the same image as the speciified container,and delete the image'
	echo '-contid -sp   :Stop all dockers that use the same image as the specified container'
	echo '-contid -st   :Start all dockers that use the same image as the specified container'
	echo '-contid -re   :Restart the contid-docker'
	echo '-contid -in   :Enter the contid-docker'
	echo '-removealldo  :Stop and delete all running and stopped dockers'
	echo '-removeallim  :Stop and delete all running and stopped dockers, and delete all images'
	exit
fi

funremovealldo(){
	docker stop $(docker ps -a | awk '{print $1}' | tail -n +2)
	docker rm $(docker ps -a | awk '{print $1}' | tail -n +2)
	exit
}

funremoveallim(){
	docker stop $(docker ps -a | awk '{print $1}' | tail -n +2)
	docker rm $(docker ps -a | awk '{print $1}' | tail -n +2)
	docker rmi $(docker images | awk '{print $3}' | tail -n +2)
	exit
}

finddo(){
	if [ $contid == "-removealldo" ]; then
		funremovealldo
	elif [ $contid == "-removeallim" ]; then
		funremoveallim
	else
		sureid=$(docker ps -a | grep "^$contid")
		echo $sureid
		if [ -z "$sureid" ]; then
			echo "Can not find $contid"
			exit
		fi
	fi
}

funs(){
	docker stop $contid
	docker rm $contid
	exit
}

funa(){
	imagename=$(docker ps -a | grep "^$contid" | awk '{print $2}')
	contidall=$(docker ps -a | grep $imagename | awk '{print $1}')
	docker stop $contidall
	docker rm $contidall
	imageleft=${imagename%%:*}
	imageright=${imagename#*:}
	echo $imageleft
	echo $imageright
	imageid=$(docker image ls | grep "^$imageleft" | grep "$imageright" | awk '{print $3}')
	echo $imagename
	echo $imageid
	docker rmi $imageid
	echo $imagename
	echo "Del Success!"
	exit
}

funsp(){
	imagenamefunsp=$(docker ps -a | grep "^$contid" | awk '{print $2}')
	echo $imagenamefunsp
	contidfunsp=$(docker ps -a | grep $imagenamefunsp | awk '{print $1}')
	docker stop $contidfunsp
	exit
}

funst(){
	imagenamefunst=$(docker ps -a | grep "^$contid" | awk '{print $2}')
	echo $imagenamefunst
	contidfunst=$(docker ps -a | grep $imagenamefunst | awk '{print $1}')
	docker start $contidfunst
	exit
}

funre(){
	docker restart $contid
	exit
}

funin(){
	docker exec -it $contid /bin/bash
	exit	
}


if [ -n $sureop ]; then
	finddo
	case $sureop in
		"-s") funs
		;;
	"-a") funa
		;;
	"-sp") funsp
		;;
	"-st") funst
		;;
	"-re") funre
		;;
	"-in") funin
		;;
	*) echo "Illegal option! You can get help through -h"
		;;
esac
fi

#Write by LTLT
#Version 2.0
#Time 2021/7/5
#Check the logs please use: docker logs -f -t --since="2010-02-08" --tail=100 -contid
