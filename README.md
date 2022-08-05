# OPT-general-models

Simple FLASK API that queries the hosted language model with a prompt and related parameters
and returns generated content as result.

## Command to run the app via docker
    ```
        docker-compose up
        
        OR
        
        sudo docker run -p 8000:8000 --gpus all <image-name> 
        [Note: w/o docker-compose.Run cmd inside flask_app]
    ```

## Steps to deploy model on ec2
1. Login into the server(See if SSH is allowed or not, and username)
   ```
   ssh -i yamak-dev-docker.pem ubuntu@3.110.147.92
   ```

2. Update the server
     ```
    sudo apt-get update
     ```
3. Install git
     ```
    sudo apt install git
     ```
4. Create public/private keys and add public key them to github
    ```
    cd ~/.ssh
    ssh-keygen -o -t rsa -C "rishabhb932@gmail.com"
   ```
5. Copy the publick key and it to github
    ```
    cat id_rsa.pub
    cd
    ```
6. Clone the repo 
    ```
    git clone <git url>
    ```
7. Install docker
    ```
    sudo apt-get install ca-certificates curl gnupg lsb-release
    
    sudo mkdir -p /etc/apt/keyrings

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

    echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    sudo apt install docker-compose
    ```

