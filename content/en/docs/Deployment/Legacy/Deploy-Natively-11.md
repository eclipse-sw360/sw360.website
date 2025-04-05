**SW360 Installation Guide on Ubuntu 18.04 LTS with Java 11**

### Prerequisites
Ensure that your system is running **Ubuntu 18.04 LTS** and that you have **sudo** privileges.

### Step 1: Update the System
Run the following commands to update and upgrade your system:
```sh
sudo apt update && sudo apt upgrade -y
```

### Step 2: Install Java 11
SW360 requires Java 11. Install it using:
```sh
sudo apt install openjdk-11-jdk -y
```
Verify the installation:
```sh
java -version
```

### Step 3: Install Dependencies
Install the necessary dependencies:
```sh
sudo apt install curl wget unzip git -y
```

### Step 4: Install and Configure PostgreSQL
SW360 requires PostgreSQL. Install and configure it as follows:
```sh
sudo apt install postgresql postgresql-contrib -y
```
Switch to the PostgreSQL user and create a database:
```sh
sudo -u postgres psql
```
Run the following PostgreSQL commands:
```sql
CREATE DATABASE sw360;
CREATE USER sw360user WITH ENCRYPTED PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE sw360 TO sw360user;
\q
```

### Step 5: Install and Configure CouchDB
Install CouchDB using:
```sh
sudo apt install couchdb -y
```
Edit the CouchDB configuration file:
```sh
sudo nano /opt/couchdb/etc/local.ini
```
Modify the following lines under `[admins]`:
```
admin = your_secure_password
```
Save and restart CouchDB:
```sh
sudo systemctl restart couchdb
```
Verify CouchDB is running:
```sh
curl http://127.0.0.1:5984/
```

### Step 6: Install and Configure Elasticsearch
Download and install Elasticsearch:
```sh
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.10.2-amd64.deb
sudo dpkg -i elasticsearch-7.10.2-amd64.deb
```
Start and enable Elasticsearch:
```sh
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch
```
Verify installation:
```sh
curl -X GET "localhost:9200"
```

### Step 7: Clone SW360 Repository and Build
Clone the SW360 repository:
```sh
git clone https://github.com/eclipse/sw360.git
cd sw360
```
Build the project using Maven:
```sh
mvn clean install
```

### Step 8: Deploy SW360
After building, deploy SW360 using:
```sh
cd deployment
./deploy.sh
```

### Step 9: Start SW360 Services
Run the following command to start the services:
```sh
sudo systemctl start sw360
```
Enable the service to start on boot:
```sh
sudo systemctl enable sw360
```

### Step 10: Access SW360
Once everything is set up, access SW360 via:
```
http://localhost:8080
```

### Troubleshooting
If you face any issues:
- Check logs using:
  ```sh
  journalctl -u sw360 --no-pager -n 50
  ```
- Ensure all dependencies are installed properly.
- Restart services if needed:
  ```sh
  sudo systemctl restart sw360
  ```

### Conclusion
You have successfully installed and configured SW360 on Ubuntu 18.04 LTS with Java 11.

