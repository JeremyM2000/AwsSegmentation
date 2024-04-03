# AWS-segmentation

Ce projet permet d'uploader une image et de la ségmenter via un bouton "Ségmenter".

## Commandes d'installation dans l'instance EC2

### Etape 1 : Installation de Docker et Git
```
sudo yum install git -y
sudo yum install docker -y
```

### Etape 2 : Clonage du repository
```
git clone https://github.com/JeremyM2000/AwsSegmentation.git
```

### Etape 3 : Mouvement dans le répertoire du projet
```
cd AWS-segmentation/
```

### Etape 4 : Activer et démarrer Docker
```
sudo systemctl enable docker
sudo systemctl start docker
```

### Etape 5 : Build l'image docker
```
sudo docker build -t model-segm:latest .
```

### Etape 6.1 : Lancement du serveur Flask
```
sudo docker run -p 80:80 model-segm:latest
```

### Etape 6.2 : Lancement du serveur Flask au démarrage
```
sudo docker run -d --restart unless-stopped -p 80:80 model-segm:latest
```

## Outils

### Connexion ssh à l'instance EC2
Remarque : Se positionner dans le réperoire avec le fichier labuser.pem.
```
ssh -i labsuser.pem ec2-user@mon-ipv4
```

### Afficher les id des containers
```
sudo docker ps
```

### Arrêt d'un container
Remarque : Il est possible d'utiliser les premiers caractères de l'id seulement.
```
sudo docker stop id-container
```

### Afficher les images docker présentes
```
sudo docker images
```

### Suppression d'une image docker
```
sudo docker rmi id-image -f
```