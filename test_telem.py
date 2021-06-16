import socket

from f1_2020_telemetry.packets import unpack_udp_packet, PacketCarTelemetryData_V1, PacketHeader

udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_socket.bind(("", 20777))

while True:
    udp_packet = udp_socket.recv(2048)
    header = PacketHeader.from_buffer_copy(udp_packet)
    packet = unpack_udp_packet(udp_packet)
    # print("received", type(packet))
    player_id = header.playerCarIndex
    if isinstance(packet, PacketCarTelemetryData_V1):
        player = packet.carTelemetryData[player_id]
        print(header.sessionTime, player.throttle, player.speed)
    
