#!/usr/bin/python3

def parse_input(filename: str) -> list:
    """
    Reads input from file for KickStart 2020 round A

    T: num of test cases to follow
    N K P:
        N: Number of stacks
        K: Number of plates in each stack
        P: Max number of plates
    N lines:
        beauty values
    
    TASK: maximise beauty value for each test case

    filename str: Name of input file
    returns: list( tuple( [N, P, K], list( stacks ) ) )
    returns: [ [(N, P, K), [stacks]], [...], ...]
    """
    with open(filename) as f:
        num_test_cases = int(f.readline())
        test_cases = []
        for _ in range(num_test_cases):
            stacks = []
            # Parse info about how many stack lines are incoming
            N, P, K = [int(token) for token in f.readline().split()]
            # read N lines and convert to list of ints
            stacks = [[int(token) for token in f.readline().strip().split()] for _ in range(N)]
            test_cases.append(((N, P, K), stacks))
    return test_cases


def write_output(filename: str, values: list) -> None:
    """
    Writes the data to file in correct format for KickStart 2020 round B

    filename str: Name of file to write output to
    values list[int]: List of sum of the top P beauty values for each test case
    """
    out_txt = [f"Case #{x+1}: {y}" for x, y in enumerate(values)]
    print("Output writing to file:")
    print("\n".join(out_txt))
    with open(filename, "w") as f:
        f.write("\n".join(out_txt))


def compare_result(truth_outfile: str, test_outfile: str) -> None:
    """
    Compares the correct output file with a user generated one.
    Use for testing new algorithms
    truth_outfile str: The known correct answers
    test_outfile str: The user generated answer file
    returns: None
        Prints mis-matches lines to stdout
    """
    truth = open(truth_outfile, "r")
    test = open(test_outfile, "r")
    i = 0
    while True:
        truth_line = truth.readline()
        test_line = test.readline()
        if (not truth_line) or (not test_line):
            break
        if truth_line != test_line:
            print(f"Line {i}: {truth_line.strip()} != {test_line.strip()}")
        i += 1
    truth.close()
    test.close()
    

def main() -> None:
    """
    To use, replace the file names and insert code to calculate beauty into calculate_result()
    """
    #########
    in_filename = "data/sample_test_set_1/sample_ts1_input.txt"
    truth_result_filename = "data/sample_test_set_1/sample_ts1_output.txt"
    out_filename = "sample_test_set_1.out"
    #########
    data = parse_input(in_filename)
    result = calculate_result(data)
    write_output(out_filename, result)
    compare_result(truth_result_filename, out_filename)


def example_calculate_result(data: list) -> list:
    """Simple function for testing"""
    example_output = []
    for tokens, stacks in data:
        example_output.append(sum(s[-1] for s in stacks))
    return example_output


def calculate_result(data: list) -> list:
    """Add custom algorithm here"""
    result = example_calculate_result(data)
    return result 


if __name__ == "__main__":
    main()

