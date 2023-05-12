import xml.etree.ElementTree as ET
import datetime
from typing import Tuple


def read_time_heart_rate(tcx_file: str) -> Tuple[list, list]:
    # Load TCX file
    tree = ET.parse(tcx_file)
    root = tree.getroot()

    # Namespace (may vary depending on the TCX file)
    namespace = {"ns": "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"}

    # Extract time and heart rate data
    time = []
    heart_rate_data = []
    for trackpoint in root.findall(".//ns:Trackpoint", namespace):
        time_element = trackpoint.find("ns:Time", namespace)
        heart_rate_element = trackpoint.find(".//ns:HeartRateBpm/ns:Value", namespace)

        if time_element is not None and heart_rate_element is not None:
            time_str = time_element.text
            time.append(datetime.datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S.%fZ"))
            heart_rate_data.append(int(heart_rate_element.text))

    return time, heart_rate_data
