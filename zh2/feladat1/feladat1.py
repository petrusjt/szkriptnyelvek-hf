#!/usr/bin/env python3

INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"


def main():
    with open(INPUT_FILENAME) as input_file:
        content = [line.strip() for line in input_file]
    print(f"-> {INPUT_FILENAME} beolvasva")

    output = []
    for i in range(len(content[0])):
        output_line = ""
        for j in range(len(content)):
            output_line += content[j][i]
        output.append(output_line)

    with open(OUTPUT_FILENAME, "w") as output_file:
        s = 0
        for line in output:
            print(line, file=output_file)
            s += int(line, 2)

        print("-" * 20, file=output_file)
        print(f"sum: {s}", file=output_file)
    
    print(f"-> {OUTPUT_FILENAME} létrehozva")
        

if __name__ == "__main__":
    main()
