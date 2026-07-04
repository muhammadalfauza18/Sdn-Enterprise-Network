#!/usr/bin/python3

from datetime import datetime
from mininet.cli import CLI
from topology_perusahaan import topology


def test_ping(src, dst_name, dst_ip):
    """
    Melakukan pengujian ping dari src ke dst.
    Mengembalikan True jika berhasil.
    """

    print(f"\n[{src.name}] ---> [{dst_name}]")

    output = src.cmd(f"ping -c 2 {dst_ip}")

    success = ", 0% packet loss" in output

    if success:
        print("STATUS : SUCCESS")
    else:
        print("STATUS : FAILED")

    return success, output


def save_log(results):

    with open("hasil_pengujian.txt", "w") as f:

        f.write("=========================================\n")
        f.write(" HASIL AUTOMATED CONNECTIVITY TEST\n")
        f.write("=========================================\n\n")

        f.write(f"Waktu : {datetime.now()}\n\n")

        total = len(results)
        sukses = 0

        for item in results:

            host = item["host"]
            tujuan = item["tujuan"]
            status = item["status"]

            if status:
                sukses += 1

            f.write(
                f"{host} -> {tujuan} : "
                f"{'SUCCESS' if status else 'FAILED'}\n"
            )

        gagal = total - sukses

        f.write("\n=========================\n")
        f.write(f"Total Test : {total}\n")
        f.write(f"Success    : {sukses}\n")
        f.write(f"Failed     : {gagal}\n")
        f.write("=========================\n")


def main():

    print("\n=========================================")
    print(" AUTOMATED CONNECTIVITY TEST")
    print("=========================================\n")

    net = topology()

    server = net.get("server")

    hasil = []

    print("\n=== Pengujian Semua Host ke Server ===")

    for i in range(1, 10):

        host = net.get(f"h{i}")

        status, output = test_ping(
            host,
            "server",
            "10.0.0.100"
        )

        hasil.append({
            "host": host.name,
            "tujuan": "server",
            "status": status
        })

    print("\n=== Pengujian Antar Divisi ===")

    pasangan = [

        ("h1", "h4"),
        ("h4", "h7"),
        ("h2", "h8"),
        ("h3", "h9")

    ]

    for src_name, dst_name in pasangan:

        src = net.get(src_name)
        dst = net.get(dst_name)

        status, output = test_ping(
            src,
            dst_name,
            dst.IP()
        )

        hasil.append({
            "host": src_name,
            "tujuan": dst_name,
            "status": status
        })

    save_log(hasil)

    sukses = sum(1 for x in hasil if x["status"])
    gagal = len(hasil) - sukses

    print("\n=========================================")
    print(" HASIL AKHIR")
    print("=========================================")

    print(f"Total Test : {len(hasil)}")
    print(f"Success    : {sukses}")
    print(f"Failed     : {gagal}")

    print("\nLaporan disimpan pada : hasil_pengujian.txt")

    print("\nMasuk ke CLI Mininet...\n")

    CLI(net)

    net.stop()


if __name__ == "__main__":
    main()
