if instance_date_raw:
            # Convert from "2024-04-30T00:00:00Z" to "30-04-2024"
            instance_date = datetime.strptime(instance_date_raw, "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%m-%Y")
        else:
            instance_date = ''
