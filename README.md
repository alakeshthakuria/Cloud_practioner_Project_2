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
