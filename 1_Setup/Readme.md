# Docker Installation on Ubuntu


## Easy Approach:


```
sudo apt-get update
```
```
sudo apt-get install curl
```
```
curl -fsSL https://get.docker.com -o get-docker.sh
```
```
sudo sh get-docker.sh
```
```
 sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```
sudo chmod +x /usr/local/bin/docker-compose
```
try running `docker-compose --version` if it fails saying command not found, run below command.
```
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
## Manual Approach:

https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository


## Reference:

https://docs.docker.com/engine/install/ubuntu/

---

&nbsp;

&nbsp;

#  Docker Installation on Windows 10


**Warning!!!**

The below steps are for Windows 10. Docker support on windows is only for 10 and above! Kindly proceed with caution.

---

Docker Desktop needs WSL2 to be installed. Below steps will help with the installation. You could either go over the instructions i have summarized below or go over the step by step guide provided by windows [here](https://docs.microsoft.com/en-us/windows/wsl/install-manual).

### 1. Verify that your version and build support installation of WSL 2

| Processor Architecure | Windows Version | Windows Build |
|----|----|---|
| x64 | >=1903 | >=18362 |
| ARM64 | >=2004 | >= 19041 |

### 2. Download the Docker Desktop app from below link and run the installation. It is necessary to run the installation as administrator.

- https://hub.docker.com/editions/community/docker-ce-desktop-windows

###  3. Pre WSL 2 Installation Setup

- Go to Windows search bar
- Type `Turn windows feature on or off`
- Click on the first result
- Ensure `Virtual Machine Platform` and `Windows Subsystem for Linux` checkboxes are enabled.



### 4. Continue to follow instructions from Step 4 and 5 in below link:
- https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package


---
**NOTE**
- If you face any error during this setup it is likely because Virutalization needs to be enabled on BIOS.
---

https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package


## Reference:
https://docs.microsoft.com/en-us/windows/wsl/install-manual

---
