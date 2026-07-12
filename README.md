# 🌐 SDN Enterprise Network

Implementasi **Software Defined Networking (SDN)** menggunakan **Mininet** dan **Ryu Controller** untuk mensimulasikan jaringan perusahaan (Enterprise Network). Project ini dibuat sebagai tugas mata kuliah Manajemen Jaringan dengan tujuan memahami konsep SDN, OpenFlow, serta pemrograman jaringan menggunakan Python.

---

## 📖 Deskripsi

Software Defined Networking (SDN) merupakan arsitektur jaringan yang memisahkan **Control Plane** dan **Data Plane**, sehingga konfigurasi jaringan menjadi lebih fleksibel, terpusat, dan mudah dikelola.

Pada project ini dibuat sebuah simulasi jaringan perusahaan menggunakan:

- Mininet sebagai simulator jaringan
- Open vSwitch sebagai virtual switch
- Ryu sebagai SDN Controller
- OpenFlow 1.3 sebagai protokol komunikasi
- Python sebagai bahasa pemrograman

---

## 🎯 Tujuan Project

- Mempelajari konsep Software Defined Networking (SDN)
- Mengimplementasikan Enterprise Network menggunakan Mininet
- Menghubungkan switch dengan Ryu Controller
- Menguji konektivitas antar host
- Menganalisis performa jaringan menggunakan OpenFlow

---

## 🏗️ Topologi Jaringan

Topologi yang digunakan adalah **Tree Topology** dengan spesifikasi:

- 1 SDN Controller (Ryu)
- 3 OpenFlow Switch
- 9 Client Host
- 1 Server
- OpenFlow Version 1.3

Contoh struktur jaringan:

```
                Ryu Controller
                      │
                 OpenFlow 1.3
                      │
                  Switch 1
                 /         \
           Switch2       Switch3
          /   |   \      /   |   \
        h1   h2  h3    h4  h5  h6
                         |
                     Switch4
                   /   |   \
                 h7   h8   Server
```

---

## ⚙️ Teknologi

- Python
- Mininet
- Ryu SDN Framework
- Open vSwitch
- Ubuntu Linux
- OpenFlow 1.3

---

## 📂 Struktur Project

```
Sdn-Enterprise-Network/
│
├── controller/
│   ├── simple_switch.py
│   └── security_controller.py
│
├── topology/
│   └── enterprise_topology.py
│
├── screenshots/
│
├── README.md
└── requirements.txt
```

> Struktur dapat disesuaikan dengan isi repository.

---

## 🚀 Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/muhammadalfauza18/Sdn-Enterprise-Network.git
```

Masuk ke folder project

```bash
cd Sdn-Enterprise-Network
```

---

### 2. Install Mininet

```bash
sudo apt update
sudo apt install mininet
```

---

### 3. Install Ryu

```bash
pip install ryu
```

---

### 4. Jalankan Ryu Controller

```bash
ryu-manager controller/simple_switch.py
```

---

### 5. Jalankan Topologi

```bash
sudo python3 topology/enterprise_topology.py
```

---

### 6. Uji Konektivitas

Masuk ke CLI Mininet

```bash
pingall
```

---

## 📌 Fitur

- Implementasi Enterprise Network
- OpenFlow Switch
- Dynamic Flow Rule
- SDN Controller
- Tree Topology
- Ping Testing
- Host Management
- Python Automation

---

## 📊 Hasil Pengujian

Pengujian dilakukan menggunakan perintah:

```bash
pingall
```

Parameter yang diuji:

- Host Connectivity
- Packet Delivery
- Packet Loss
- Controller Response

---


## 📚 Konsep yang Dipelajari

- Software Defined Networking
- OpenFlow Protocol
- Network Programmability
- Controller Architecture
- Enterprise Network Design
- Virtual Network Simulation

---



## 📄 Lisensi

Project ini dibuat untuk keperluan pembelajaran dan akademik.

Silakan digunakan sebagai referensi dengan tetap mencantumkan sumber.

---

## ⭐ Dukungan

Jika repository ini bermanfaat, jangan lupa berikan ⭐ pada repository GitHub ini.
