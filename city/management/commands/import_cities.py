import json
import os
from django.core.management.base import BaseCommand
from city.models import City

class Command(BaseCommand):
    help = "Import cities from a JSON file into the database"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help="Path to the JSON file")

    def handle(self, *args, **kwargs):
        json_file = kwargs["json_file"]

        if not os.path.exists(json_file):
            self.stdout.write(self.style.ERROR(f"File '{json_file}' not found!"))
            return

        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        for unloc_code, details in data.items():
            City.objects.update_or_create(
                unloc_code=unloc_code,
                defaults={
                    "name": details.get("name"),
                    "city": details.get("city"),
                    "country": details.get("country"),
                    "province": details.get("province"),
                    "timezone": details.get("timezone"),
                    "alias": details.get("alias", []),
                    "regions": details.get("regions", []),
                    "coordinates_lat": details["coordinates"][1] if "coordinates" in details else None,
                    "coordinates_lon": details["coordinates"][0] if "coordinates" in details else None,
                    "code": details.get("code"),
                },
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(data)} cities"))
