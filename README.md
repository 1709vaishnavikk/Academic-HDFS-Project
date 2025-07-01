# ☁️ Private SaaS Cloud using HDFS

This project demonstrates how to build a **secure private SaaS cloud** over a LAN using **Hadoop Distributed File System (HDFS)** and **AES encryption** with Python scripting. It simulates a private cloud environment where users can upload/download encrypted files in a distributed manner.

---

## 🎯 Aim

To implement a secure private SaaS cloud using HDFS for distributed storage and AES encryption for secure data handling over a local network.

---

## 🔍 Objectives

- 🔐 Encrypt file data using AES before storage, ensuring confidentiality.
- 🗂️ Build a distributed cloud storage system for LAN users using HDFS.
- 💸 Provide a cost-effective and open-source solution.
- 🧪 Learn practical implementation of Hadoop, Python scripting, and encryption.

---

## 🧰 Tech Stack

| Component     | Tool / Library                     |
|---------------|------------------------------------|
| Language      | Python                             |
| Storage       | HDFS (Hadoop Distributed File System) |
| Encryption    | AES (CBC Mode, PyCryptodome)       |
| Environment   | WSL (Windows Subsystem for Linux), Java |

---

## 🏗️ System Architecture

1. User uploads a file
2. Python script splits the file and encrypts each block using AES-CBC
3. Blocks are stored in HDFS via command-line
4. File can be downloaded and decrypted later with the correct key

---

## ⚙️ How to Use

### 🔧 Setup Hadoop in Pseudo-Distributed Mode

1. Install Hadoop and configure `core-site.xml` and `hdfs-site.xml`
2. Enable passwordless SSH
3. Format namenode and start HDFS:
   ```bash
   hdfs namenode -format
   start-dfs.sh
