#!/usr/bin/env python3

import json

INPUT_FILENAME = "primes.php"
OUTPUT_FILENAME = "primes.json"


def main():
    primes = []
    with open(INPUT_FILENAME) as input_file:
        for line in input_file:
            if "=>" in line:
                primes.append(int(line.split("=>")[1].strip().replace(",", "")))
    print(f"-> {INPUT_FILENAME} beolvasva")
    
    d = {
        "description": "list of prime numbers",
        "data": primes
    }

    output_json = json.dumps(d, indent=2)
    with open(OUTPUT_FILENAME, "w") as output_file:
        print(output_json, file=output_file)
    print(f"-> {OUTPUT_FILENAME} létrehozva")


if __name__ == "__main__":
    main()
