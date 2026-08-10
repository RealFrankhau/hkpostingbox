import json

with open("mailpost_raw.json", "r", encoding="utf-8-sig") as f:
    data = json.load(f)

lines = []
lines.append("地區\t位置\tGPS\t郵筒號碼")

for region in data["region"]:
    for district in region["district"]:
        district_name = district.get("district_name_tc", "")
        if "sub_district" in district:
            for sub in district["sub_district"]:
                sub_name = sub.get("sub_district_name_tc", "")
                for box in sub.get("box", []):
                    location = box.get("box_addr_tc", "")
                    gps = f"{box.get('longitude', '')}, {box.get('latitude', '')}"
                    box_no = box.get("box_no", "")
                    lines.append(f"{district_name}\t{location}\t{gps}\t{box_no}")

with open("mailpost.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Extracted {len(lines)-1} records to mailpost.txt")
