import json
from pathlib import Path
from urllib.request import Request, urlopen


SOURCE_URL = (
    "https://webapp.hongkongpost.hk/"
    "api1/v1/postOffice/all-street-posting-box"
)
DATA_PATH = Path("data/post-boxes.json")
TEXT_PATH = Path("mailpost.txt")


def main():
    request = Request(
        SOURCE_URL,
        data=b"",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Origin": "https://webapp.hongkongpost.hk",
            "Referer": (
                "https://webapp.hongkongpost.hk/tc/about_us/network/"
                "street_posting_boxes2/index.html"
            ),
            "User-Agent": "Mozilla/5.0",
        },
        method="POST",
    )
    with urlopen(request, timeout=60) as response:
        source_data = json.load(response)

    boxes = []
    text_lines = ["地區\t位置\tGPS\t郵筒號碼"]
    for region in source_data.get("region", []):
        for district in region.get("district", []):
            for sub_district in district.get("sub_district", []):
                for box in sub_district.get("box", []):
                    record = {
                        "region_name_tc": region["region_name_tc"],
                        "district_name_tc": district["district_name_tc"],
                        "sub_district_name_tc": sub_district[
                            "sub_district_name_tc"
                        ],
                        "box_no": box["box_no"],
                        "longitude": box["longitude"],
                        "latitude": box["latitude"],
                        "box_addr_tc": box["box_addr_tc"],
                        "weekday_collection": box.get("weekday_collection"),
                        "sat_collection": box.get("sat_collection"),
                        "sun_collection": box.get("sun_collection"),
                        "ph_collection": box.get("ph_collection"),
                    }
                    boxes.append(record)
                    gps = f"{record['longitude']}, {record['latitude']}"
                    text_lines.append(
                        f"{record['district_name_tc']}\t"
                        f"{record['box_addr_tc']}\t{gps}\t{record['box_no']}"
                    )

    if not boxes:
        raise ValueError("Hongkong Post API returned no postal-box records")

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text(
        json.dumps(boxes, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    TEXT_PATH.write_text("\n".join(text_lines), encoding="utf-8")
    print(f"Updated {len(boxes)} postal-box records in {DATA_PATH}")


if __name__ == "__main__":
    main()
