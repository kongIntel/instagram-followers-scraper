thonimport json

class DataExporter:
    @staticmethod
    def export_to_json(data, filename="followers_data_exported.json"):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def export_to_csv(data, filename="followers_data_exported.csv"):
        import csv
        keys = data[0].keys() if data else []
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)