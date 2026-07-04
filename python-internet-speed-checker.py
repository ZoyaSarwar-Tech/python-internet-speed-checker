import speedtest

print("Checking Internet Speed...")
print()

st = speedtest.Speedtest()

print("Finding Best Server...")
st.get_best_server()

print("Calculating Download Speed...")
download = st.download() / 1_000_000

print("Calculating Upload Speed...")
upload = st.upload() / 1_000_000

ping = st.results.ping

print("\n------ RESULT ------")
print(f"Download Speed : {download:.2f} Mbps")
print(f"Upload Speed   : {upload:.2f} Mbps")
print(f"Ping           : {ping:.2f} ms")