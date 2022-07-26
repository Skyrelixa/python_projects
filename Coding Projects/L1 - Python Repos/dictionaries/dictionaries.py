monthConversion = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}

print(monthConversion)
print(monthConversion["Nov"])
print(monthConversion.get("incorrect", "Not a valid key."))