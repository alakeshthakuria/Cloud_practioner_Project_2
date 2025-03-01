## Secure Azure-Based Web Application Architecture with Private Database Communication
<a href="" target="blank"><img align="center" src="https://github.com/alakeshthakuria/Cloud_practioner_Project_2/blob/main/project_architech_stage_initial.png" height="300" /></a>

### Project Architecture Description
This architecture represents a cloud-based deployment on Microsoft Azure, utilizing a Virtual Network (VNet) with two subnets: one for the Front-end Virtual Machine (VM) and another for the Database VM. Below is a breakdown of the design:
### 1. Client Access:
- The client connects to the Front-end VM over the internet via HTTP.
- The client accesses the front-end using the public IP assigned to the Front-end VM.
- The necessary Network Security Group (NSG) rules allow inbound HTTP traffic.
### 2. Azure Virtual Network (VNet):
- The deployment resides inside an Azure Virtual Network (VNet), ensuring secure communication between resources.
- The VNet contains two subnets, one for the Front-end and one for the Database.
- The NSG is configured to allow inbound HTTP traffic.
### 4. Database VM (Virtual Machine):
- The Database VM does not allow direct public access for security reasons.
- It only communicates with the Front-end VM through a private IP.
- This ensures secure, internal communication without exposing sensitive data to the internet.
### 5. Security Considerations:
- NSG rules are configured to restrict traffic to only necessary services.
- The Database VM is isolated from direct internet access.
- Private IP communication ensures security between the Front-end and Database VMs.

## Step-by-Step Guide for Deploying a Web Application on Azure VMs
### 1. Front-End VM Setup
#### 1.1 Create the Front-End Application
- Create an HTML form (form.html) - Version 1.0
- Start a simple HTTP server to serve the form: `python3 -m http.server 8000`

### 2. Database VM Setup
#### 2.1 Install and Configure MySQL Server
- Install MySQL Server: `sudo apt install mysql-server -y`
- Secure the MySQL installation: `sudo mysql_secure_installation`
- Allow remote access by modifying MySQL configuration: `sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf`
- Change bind-address from 127.0.0.1 to 0.0.0.0 or Private IP of front-end VM.
- Restart MySQL service:`sudo systemctl restart mysql`
#### 2.2 Configure Database and User
- Log into MySQL:`sudo mysql -u root`
- Create a new database:`CREATE DATABASE user_data;`
- Create a new user for the front-end VM:`CREATE USER 'frontend_user'@'<FRONTEND_VM_PRIVATE_IP>' IDENTIFIED BY 'StrongPassword123!';`
- Grant privileges to the user:`GRANT ALL PRIVILEGES ON user_data.* TO 'frontend_user'@'<FRONTEND_VM_PRIVATE_IP>';`
- Apply changes:
  ```
   FLUSH PRIVILEGES;
   EXIT;
  ```

### 3. Front-End VM Setup (Continued)
#### 3.1 Test Database Connection
- Verify that the front-end VM can connect to MySQL:`mysql -u frontend_user -h <MYSQL_VM_PRIVATE_IP> -p`
#### 3.2 Set Up Backend (Flask App)
- Install Python virtual environment support:`sudo apt install python3-venv -y`
- Create a virtual environment:
  ```
  python3 -m venv myenv
  source myenv/bin/activate
  ```
- Install required dependencies:`pip install flask mysql-connector-python`
- Create app.py (backend script to handle form submissions).
- Activate the virtual environment:`source myenv/bin/activate`
- Start the backend server:`python3 app.py`
#### 3.3 Update Front-End Form
- Update form.html to Version 1.1, modifying the form action:`<form id="registrationForm" action="http://20.15.112.217:5000/submit" method="POST" onsubmit="return validateForm()">`


### 4. Database VM Setup (Continued)
#### 4.1 Create a User Table
- Log in to MySQL:`sudo mysql -u root`
- Select the user_data database:`USE user_data;`
- Create the users table:
  ```
  CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL
  );
  ```



