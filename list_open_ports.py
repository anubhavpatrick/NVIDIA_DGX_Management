#A program to display open ports on a machine

def main():
    import socket
    import sys
    from optparse import OptionParser
    parser = OptionParser("usage: %prog [options] target")#target is localhost for local systems
    parser.add_option("-p", "--port", dest="port", type="int", default=80, help="port to scan")
    parser.add_option("-s", "--start", dest="start", type="int", default=1, help="start port")
    parser.add_option("-e", "--end", dest="end", type="int", default=65535, help="end port")
    (options, args) = parser.parse_args()
    if len(args) == 0:
        parser.error("Please specify a target")
    target = args[0]
    for port in range(options.start, options.end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
        

if __name__ == '__main__':
    main()
