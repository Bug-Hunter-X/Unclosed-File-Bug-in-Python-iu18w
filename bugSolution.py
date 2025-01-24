def function_with_unclosed_file_solution(filename):
    try:
        f = open(filename, 'w')
        # ... some code that might raise an exception ...
        f.write('some data')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        f.close()
        print('File closed')

# Example usage
function_with_unclosed_file_solution('my_file.txt')
