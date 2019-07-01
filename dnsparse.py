#!/usr/bin/python3

# I used this to convert my many zone files which were in a variety 
# of legal formats, but not all the same as multiple authors were
# involved.  Drop all the (forward only) zone files into a "zones"
# directory at the same level as this script.  In my case it looks
# like this:
#  /mycode/zones/zone_out
# this script runs from mycode and uses the files in "zones" to 
# generate .yml files of the entries that can then be used with the 
# ansible role "bertvv.bind."  This saves time when you have many
# zone files.

import os

file_content = ""

def parse_A(xline, xdivider):
    # print("length: ", str(xlijne.count(1)))
    hostname = ""
    zline = xline.replace("\t", "    ").replace("\t\t", "    ")
    if xdivider in zline:
        a = zline.split(xdivider)

        if len(a) >= 2:
            b = list(map(lambda s: s.strip().replace(" ", "").replace("A", "").replace("\t", ""), a))
            hostname += "          - name: " + b[0] + "\n"
            hostname += "            ip: " + b[1] + "\n"
    return hostname

zonedir = "zones"
zone_in_directory = os.fsencode(zonedir)

print("directory: ", zone_in_directory)

zone_out_dir = os.path.join(os.getcwd(), zonedir, "zone_out")

for zone_file in os.listdir(zone_in_directory):
    zone_path = (os.path.join(zone_in_directory, zone_file))

    if not ".net".encode() in zone_path:
        continue
    # print("file path after: ", zone_path)

    # Now parse each file
    f = open(zone_path, "r", encoding="ISO-8859-1")

    for line in f:
        line = line.strip()
        # print(line) -- just checking

        if ";" in line \
                or line.startswith(" ") \
                or line.startswith("@") \
                or line.startswith("corp") \
                or line.startswith("$TTL") \
                or "CNAME" in line \
                or not line:
            # print("rejected ===> ", line) -- just checking again
            continue

        if "$ORIGIN" in line:
            pass

        x = parse_A(line, " IN  A ")
        y = parse_A(line, " IN A ")
        z = parse_A(line, "   A   ")

        if "$ORIGIN" in line:
            pass

        file_content += x
        file_content += y
        file_content += z

    print(file_content)
    print("===========================================================", os.path.join(zone_out_dir, zone_file.decode()))
    this_file = open(os.path.join(zone_out_dir, zone_file.decode() + ".yml"), 'w')
    this_file.write(file_content)
    this_file.close()
    file_content = ""
